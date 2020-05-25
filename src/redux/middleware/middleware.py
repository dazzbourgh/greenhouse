import multiprocessing
from typing import List

import rx
from rx.scheduler import ThreadPoolScheduler

from src.epics.types import Epic
from src.redux.store.action import Action
from src.redux.store.store import Store, Dispatch


def epic_middleware(epics: List[Epic], state_scheduler: ThreadPoolScheduler):
    optimal_thread_count = multiprocessing.cpu_count()
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


def logging_middleware():
    def with_store(store: Store):
        def with_dispatch(next_dispatch: Dispatch):
            def action_processor(action: Action) -> Action:
                print('Dispatching ' + action.type)
                print('Previous state: ', store.get_state())
                next_dispatch(action)
                print('New state: ', store.get_state())
                print()
                return action

            return action_processor

        return with_dispatch

    return with_store
