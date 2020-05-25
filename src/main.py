import sched
import time

from rx.scheduler import ThreadPoolScheduler

from src.actions.actions import measure_temperature, measure_co2, measure_humidity
from src.epics.epics import temperature_epic, humidity_epic
from src.reducers.reducers import temperature, humidity
from src.redux.middleware.middleware import logging_middleware, epic_middleware
from src.redux.store.store import create_store, Store, apply_middleware

if __name__ == '__main__':
    state_executor = ThreadPoolScheduler(1)
    store: Store = create_store(
        {
            'temperature': 60,
            'humidity': 10
        },
        [temperature, humidity],
        apply_middleware([
            logging_middleware(),
            epic_middleware([temperature_epic, humidity_epic], state_executor)
        ]))
    scheduler = sched.scheduler(time.time, time.sleep)
    while True:
        scheduler.enter(5, 1, lambda: store.dispatch(measure_temperature()))
        scheduler.enter(5, 1, lambda: store.dispatch(measure_humidity()))
        scheduler.enter(5, 1, lambda: store.dispatch(measure_co2()))
        scheduler.run()
