from typing import List

import rx

from src.epics.types import Epic
from src.redux.store.action import Action
from src.redux.store.store import Store, Dispatch


def epic_middleware(epics: List[Epic]):
    def s(store):
        def n(next_dispatch):
            def a(action):
                next_dispatch(action)
                for epic in epics:
                    epic(rx.of(action)).subscribe(lambda act: store.dispatch(act))

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
                return action

            return action_processor

        return with_dispatch

    return with_store
