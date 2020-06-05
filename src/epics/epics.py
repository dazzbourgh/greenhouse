from typing import Callable

import rx
from rx import operators as ops, Observable

# todo: add actual implementations
from actions import MEASURE_TEMPERATURE, set_temperature, MEASURE_HUMIDITY, MEASURE_CO2, set_co2, set_humidity


def create_dht22_epic(get_data) -> Callable[[Observable], Observable]:
    def dht22_epic(action: Observable) -> Observable:
        return action.pipe(
            ops.filter(lambda a: a.type == MEASURE_TEMPERATURE or a.type == MEASURE_HUMIDITY),
            ops.map(get_data),
            ops.flat_map(lambda data: rx.of(set_temperature(data[1]), set_humidity(data[0])))
        )

    return dht22_epic


def co2_epic(action: Observable) -> Observable:
    return action.pipe(
        ops.filter(lambda a: a.type == MEASURE_CO2),
        ops.map(lambda a: set_co2(1000))
    )
