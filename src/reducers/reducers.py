from src.actions.action_types import SET_TEMPERATURE
from src.store.action import Action


def temperature(action: Action, state=70) -> int:
    if action.type == SET_TEMPERATURE:
        return action.payload['temperature']
    else:
        return state
