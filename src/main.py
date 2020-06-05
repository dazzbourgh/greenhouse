import asyncio

from actions.actions import measure_temperature, measure_humidity, measure_co2
from controllers import temperature_controller, humidity_controller, co2_controller, lighting_controller
from epics import create_dht22_epic, co2_epic
from hardware.sensors import get_dht22_data
from reducers import humidity, temperature, co2, scenarios
from redux.middleware import logging_middleware, epic_middleware, controller_middleware, scenario_middleware
from redux.store import Store, create_store
from redux.store.store import apply_middleware
from scenarios import scenarios as scenarios_dict

if __name__ == '__main__':
    initial_state = {
        'temperature': 60,
        'humidity': 10,
        'co2': 200,
        'scenarios': {
            'master': scenarios_dict['master'],
            'current': scenarios_dict['master'][0]['name'],
            'individual': {**scenarios_dict['individual']}
        }
    }
    store: Store = create_store(
        initial_state,
        [temperature, humidity, co2, scenarios],
        apply_middleware([
            logging_middleware(),
            scenario_middleware(),
            epic_middleware([create_dht22_epic(lambda: get_dht22_data(4)),
                             co2_epic]),
            controller_middleware([temperature_controller,
                                   humidity_controller,
                                   co2_controller,
                                   lighting_controller])
        ]))


    async def measurements():
        while True:
            store.dispatch(measure_temperature())
            store.dispatch(measure_humidity())
            store.dispatch(measure_co2())
            await asyncio.sleep(10)


    loop = asyncio.get_event_loop()
    asyncio.ensure_future(measurements())
    loop.run_forever()
