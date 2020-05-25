from src.actions.action_types import MEASURE_TEMPERATURE, MEASURE_HUMIDITY
from src.epics.epics import temperature_epic, humidity_epic
from src.middleware.middleware import logging_middleware, epic_middleware
from src.reducers.reducers import temperature, humidity
from src.store.action import Action
from src.store.store import Store, create_store, apply_middleware

if __name__ == '__main__':
    store: Store = create_store(
        {
            'temperature': 60,
            'humidity': 10
        },
        [temperature, humidity],
        apply_middleware([
            logging_middleware(),
            epic_middleware([temperature_epic, humidity_epic])
        ]))
    store.dispatch(Action(MEASURE_TEMPERATURE))
    store.dispatch(Action(MEASURE_HUMIDITY))
