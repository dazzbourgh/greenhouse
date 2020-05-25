from rx import operators as ops, Observable

from src.actions.action_types import MEASURE_TEMPERATURE, MEASURE_HUMIDITY, MEASURE_CO2
from src.actions.actions import set_co2, set_humidity, set_temperature


# todo: add actual implementations


def temperature_epic(action: Observable) -> Observable:
    return action.pipe(
        ops.filter(lambda a: a.type == MEASURE_TEMPERATURE),
        ops.map(lambda a: set_temperature(40))
    )


def humidity_epic(action: Observable) -> Observable:
    return action.pipe(
        ops.filter(lambda a: a.type == MEASURE_HUMIDITY),
        ops.map(lambda a: set_humidity(70))
    )


def co2_epic(action: Observable) -> Observable:
    return action.pipe(
        ops.filter(lambda a: a.type == MEASURE_CO2),
        ops.map(lambda a: set_co2(1000))
    )
