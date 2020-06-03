import asyncio

from rx.scheduler import CurrentThreadScheduler

from actions.actions import measure_temperature, measure_humidity, measure_co2, flip_scenario
from epics import create_dht22_epic, co2_epic
from hardware.controllers import temperature_controller
from hardware.sensors import get_dht22_data
from reducers import humidity, temperature, co2
from redux.middleware import logging_middleware, epic_middleware, controller_middleware
from redux.store import Store, create_store
from redux.store.store import apply_middleware
from scenario import get_scenarios

if __name__ == '__main__':
    scheduler = CurrentThreadScheduler()
    scenarios = get_scenarios()
    initial_state = {
        'temperature': 60,
        'humidity': 10,
        'co2': 200,
        'scenarios': {
            'master': scenarios['master'],
            'scenarios': scenarios['scenarios'],
            'current': scenarios['master'][0]
        }
    }
    store: Store = create_store(
        initial_state,
        [temperature, humidity, co2],
        apply_middleware([
            logging_middleware(),
            epic_middleware([create_dht22_epic(lambda: get_dht22_data(4)), co2_epic]),
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
