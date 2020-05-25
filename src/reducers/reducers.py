from src.actions.action_types import SET_TEMPERATURE, SET_HUMIDITY
from src.store.action import Action


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
