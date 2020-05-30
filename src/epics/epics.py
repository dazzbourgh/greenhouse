from rx import operators as ops, Observable

# todo: add actual implementations
from actions import MEASURE_TEMPERATURE, set_temperature, MEASURE_HUMIDITY, set_humidity, MEASURE_CO2, set_co2


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
