from src.actions.action_types import MEASURE_TEMPERATURE, MEASURE_HUMIDITY
from src.epics.epics import temperature_epic, humidity_epic
from src.reducers.reducers import temperature, humidity
from src.redux.middleware.middleware import logging_middleware, epic_middleware
from src.redux.store.action import Action
from src.redux.store.store import create_store, Store, apply_middleware

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
