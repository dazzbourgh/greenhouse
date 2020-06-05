from typing import Callable

from actions import SET_TEMPERATURE
from redux.store import Action

State = dict
Controller = Callable[[Action, State], None]

temperature_controller: Controller = lambda action, state: print('---Updating temp', action.payload[
    'temperature']) if action.type == SET_TEMPERATURE else None


def humidity_controller(action, state):
    pass


def co2_controller(action, state):
    pass


def lighting_controller(action, state):
    pass
