from actions import MEASURE_TEMPERATURE, SET_TEMPERATURE, SET_LIGHTING, SET_HUMIDITY, SET_CO2, MEASURE_HUMIDITY, \
    MEASURE_CO2, FLIP_SCENARIO
from redux.store import Action


def measure_temperature():
    return Action(MEASURE_TEMPERATURE)


def measure_humidity():
    return Action(MEASURE_HUMIDITY)


def measure_co2():
    return Action(MEASURE_CO2)


def set_temperature(temp):
    return Action(
        SET_TEMPERATURE,
        {
            'temperature': temp
        }
    )


def set_humidity(humidity):
    if humidity < 0 or humidity > 100:
        raise ValueError('Humidity should be between 0 and 100')
    return Action(
        SET_HUMIDITY,
        {
            'humidity': humidity
        }
    )


def set_lighting(lighting):
    if lighting < 0 or lighting > 100:
        raise ValueError('Lighting should be between 0 and 100')
    return Action(
        SET_LIGHTING,
        {
            'lighting': lighting
        }
    )


def set_co2(co2):
    return Action(
        SET_CO2,
        {
            'co2': co2
        }
    )


def flip_scenario():
    return Action(FLIP_SCENARIO)
