import copy

from actions import SET_TEMPERATURE, SET_HUMIDITY, SET_LIGHTING, SET_CO2, FLIP_SCENARIO
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


def scenarios(action: Action, state=None) -> dict:
    if state is None:
        state = {}
    if action.type == FLIP_SCENARIO:
        new_state = copy.deepcopy(state)
        master = state['master']
        current_scenario_entry = next(
            scenario_entry for scenario_entry in master if scenario_entry['name'] == state['current'])
        current_scenario_index = master.index(current_scenario_entry)
        next_scenario_index = current_scenario_index + 1 if current_scenario_index < len(state['master']) - 1 else 0
        next_scenario_name = list(state['individual'])[next_scenario_index]
        new_state['current'] = next_scenario_name
        return new_state
    else:
        return state
