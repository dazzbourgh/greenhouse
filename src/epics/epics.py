from rx import operators as ops, Observable

from src.actions.action_types import MEASURE_TEMPERATURE, SET_TEMPERATURE, MEASURE_HUMIDITY, SET_HUMIDITY
from src.store.action import Action


def temperature_epic(action: Observable) -> Observable:
    return action.pipe(
        ops.filter(lambda a: a.type == MEASURE_TEMPERATURE),
        ops.map(lambda a: Action(SET_TEMPERATURE, {'temperature': 100}))
    )


def humidity_epic(action: Observable) -> Observable:
    return action.pipe(
        ops.filter(lambda a: a.type == MEASURE_HUMIDITY),
        ops.map(lambda a: Action(SET_HUMIDITY, {'humidity': 70}))
    )
