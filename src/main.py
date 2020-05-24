from src.actions.action_types import SET_TEMPERATURE
from src.middleware.middleware import logging_middleware
from src.reducers.reducers import temperature
from src.store.action import Action
from src.store.store import Store, create_store, apply_middleware

if __name__ == '__main__':
    store: Store = create_store(
        {
            'temperature': 60
        },
        [temperature],
        apply_middleware([logging_middleware()]))
    store.dispatch(Action(SET_TEMPERATURE, {'temperature': 80}))
