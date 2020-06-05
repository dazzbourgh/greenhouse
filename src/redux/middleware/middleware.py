import multiprocessing
import re
from typing import List

import rx
from rx import operators as ops
from rx.scheduler import ThreadPoolScheduler

from actions import FLIP_SCENARIO, flip_scenario
from epics import Epic
from hardware.controllers import Controller
from redux.store import Store, Action
from redux.store.store import Dispatch

state_scheduler = ThreadPoolScheduler(1)
optimal_thread_count = int(multiprocessing.cpu_count() / 2)


def controller_middleware(controllers: List[Controller]):
    controller_scheduler = ThreadPoolScheduler(optimal_thread_count - 1)

    def s(_):
        def n(next_dispatch):
            def a(action):
                rx.of(action).subscribe(lambda act: next_dispatch(act),
                                        scheduler=state_scheduler)
                for controller in controllers:
                    rx.of(action).subscribe(lambda act: controller(act),
                                            scheduler=controller_scheduler)

            return a

        return n

    return s


def epic_middleware(epics: List[Epic]):
    epic_scheduler = ThreadPoolScheduler(optimal_thread_count)

    def s(store):
        def n(next_dispatch):
            def a(action):
                rx.of(action).subscribe(lambda act: next_dispatch(act),
                                        scheduler=state_scheduler)
                for epic in epics:
                    epic(rx.of(action)).subscribe(lambda act: store.dispatch(act),
                                                  scheduler=epic_scheduler)

            return a

        return n

    return s


def scenario_middleware():
    scenario_scheduler = ThreadPoolScheduler(1)

    def s(store):
        def n(next_dispatch):
            def flip():
                delay = get_delay()
                rx.of(flip_scenario()) \
                    .pipe(ops.delay(parse_time(delay))) \
                    .subscribe(lambda act: store.dispatch(act), scheduler=scenario_scheduler)

            def get_delay():
                state = store.get_state()
                scenarios = state['scenarios']
                current_scenario_name = scenarios['current']
                master = scenarios['master']
                current = next(sc for sc in master if sc['name'] == current_scenario_name)
                delay = current['length']
                return delay

            flip()

            def a(action):
                rx.of(action).subscribe(lambda act: next_dispatch(act),
                                        scheduler=state_scheduler)
                if action.type == FLIP_SCENARIO:
                    flip()

            return a

        return n

    return s


def parse_time(length):
    regex = '(\\d+)([hms])'
    match = re.search(regex, length, re.IGNORECASE)
    number = int(match[1])
    unit = match[2]
    if unit == 'h':
        number *= 60 * 60
    elif unit == 'm':
        number *= 60
    return number


def logging_middleware():
    def with_store(store: Store):
        def with_dispatch(next_dispatch: Dispatch):
            def action_processor(action: Action) -> Action:
                print('Dispatching ' + action.type)
                print('Previous state: ', store.get_state())
                next_dispatch(action)
                print('New state:      ', store.get_state())
                print()
                return action

            return action_processor

        return with_dispatch

    return with_store
