from actions import SET_TEMPERATURE, SET_HUMIDITY, SET_LIGHTING, SET_CO2
from redux.store import Action


def temperature(action: Action, state=70) -> int:
    if action.type == SET_TEMPERATURE:
        return action.payload['temperature']
    else:
        return state


def humidity(action: Action, state=50) -> int:
    if action.type == SET_HUMIDITY:
        return action.payload['humidity']
    else:
        return state


def lighting(action: Action, state=100) -> int:
    if action.type == SET_LIGHTING:
        return action.payload['lighting']
    else:
        return state


def co2(action: Action, state=1000) -> int:
    if action.type == SET_CO2:
        return action.payload['co2']
    else:
        return state
