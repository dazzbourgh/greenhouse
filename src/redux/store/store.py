import copy
from typing import Callable, List

from redux.store import Action


class Store:
    def __init__(self, state, reducers: []):
        self.__state = state
        self.__reducers = reducers

    def dispatch(self, action):
        state_copy = copy.deepcopy(self.__state)
        for reducer in self.__reducers:
            name = reducer.__name__
            state_copy[name] = reducer(action, state_copy[name])
        self.__state = state_copy

    def get_state(self):
        return copy.deepcopy(self.__state)


ActionProcessor = Callable[[Action], Action]
Dispatch = Callable[[Action], None]
Dispatcher = Callable[[Dispatch], ActionProcessor]
Middleware = Callable[[Store], Dispatcher]


def create_store(initial_state, reducers, middleware):
    store = Store(initial_state, reducers)
    middleware(store)
    return store


def apply_middleware(middlewares: List[Middleware]):
    def with_store(store):
        dispatch = store.dispatch
        for middleware in middlewares:
            dispatch = middleware(store)(dispatch)
        store.dispatch = dispatch

    return with_store
