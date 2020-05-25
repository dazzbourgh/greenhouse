from src.actions.action_types import MEASURE_TEMPERATURE
from src.epics.temperature_epic import temperature_epic
from src.middleware.middleware import logging_middleware, epic_middleware
from src.reducers.reducers import temperature
from src.store.action import Action
from src.store.store import Store, create_store, apply_middleware

if __name__ == '__main__':
    store: Store = create_store(
        {
            'temperature': 60
        },
        [temperature],
        apply_middleware([
            logging_middleware(),
            epic_middleware([temperature_epic])
        ]))
    store.dispatch(Action(MEASURE_TEMPERATURE))
