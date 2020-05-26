import sched
import time

from src.actions.actions import measure_temperature, measure_co2, measure_humidity
from src.epics.epics import temperature_epic, humidity_epic, co2_epic
from src.hardware.controllers.controllers import temperature_controller
from src.reducers.reducers import temperature, humidity, co2
from src.redux.middleware.middleware import logging_middleware, epic_middleware, controller_middleware
from src.redux.store.store import create_store, Store, apply_middleware

if __name__ == '__main__':
    store: Store = create_store(
        {
            'temperature': 60,
            'humidity': 10,
            'co2': 200
        },
        [temperature, humidity, co2],
        apply_middleware([
            logging_middleware(),
            epic_middleware([temperature_epic, humidity_epic, co2_epic]),
            controller_middleware([temperature_controller])
        ]))
    scheduler = sched.scheduler(time.time, time.sleep)
    while True:
        scheduler.enter(5, 1, lambda: store.dispatch(measure_temperature()))
        scheduler.enter(5, 1, lambda: store.dispatch(measure_humidity()))
        scheduler.enter(5, 1, lambda: store.dispatch(measure_co2()))
        scheduler.run()
