import re

import rx
from rx import operators as ops
from rx.scheduler import ThreadPoolScheduler

from actions import flip_scenario, FLIP_SCENARIO
from redux.middleware.state_scheduler import state_scheduler


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
