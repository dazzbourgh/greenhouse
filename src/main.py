import asyncio

from rx.scheduler import CurrentThreadScheduler

from src.actions.actions import measure_temperature, measure_humidity, measure_co2, flip_scenario
from src.epics.epics import temperature_epic, humidity_epic, co2_epic
from src.hardware.controllers.controllers import temperature_controller
from src.reducers.reducers import temperature, humidity, co2
from src.redux.middleware.middleware import logging_middleware, epic_middleware, controller_middleware
from src.redux.store.store import create_store, Store, apply_middleware

if __name__ == '__main__':
    scheduler = CurrentThreadScheduler()
    initial_state = {
        'temperature': 60,
        'humidity': 10,
        'co2': 200,
        'scenario': 'day'
    }
    store: Store = create_store(
        initial_state,
        [temperature, humidity, co2],
        apply_middleware([
            logging_middleware(),
            epic_middleware([temperature_epic, humidity_epic, co2_epic]),
            controller_middleware([temperature_controller])
        ]))


    async def measurements():
        while True:
            store.dispatch(measure_temperature())
            store.dispatch(measure_humidity())
            store.dispatch(measure_co2())
            await asyncio.sleep(1)


    async def flip_scenario_work():
        while True:
            await asyncio.sleep(60 * 60 * 18)
            store.dispatch(flip_scenario())
            await asyncio.sleep(60 * 60 * 6)
            store.dispatch(flip_scenario())


    loop = asyncio.get_event_loop()
    asyncio.ensure_future(measurements())
    asyncio.ensure_future(flip_scenario_work())
    loop.run_forever()
