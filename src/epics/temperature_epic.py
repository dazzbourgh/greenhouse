from typing import Callable

from src.actions.action_types import MEASURE_TEMPERATURE, SET_TEMPERATURE
from src.epics.types import SideEffect
from src.store.action import Action


def temperature_epic(dispatch) -> Callable[[Action], SideEffect]:
    def temp(action) -> SideEffect:
        if action.type == MEASURE_TEMPERATURE:
            print('requesting temperature')
            measured_temperature = 100

            def set_temperature():
                dispatch(Action(SET_TEMPERATURE,
                                {
                                    'temperature': 100
                                }))

            return set_temperature
        else:
            def nop():
                pass
            return nop
    return temp
