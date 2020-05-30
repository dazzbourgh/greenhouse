from typing import Callable

from actions import SET_TEMPERATURE
from redux.store import Action

Controller = Callable[[Action], None]

temperature_controller: Controller = lambda action: print('---Updating temp', action.payload[
    'temperature']) if action.type == SET_TEMPERATURE else None
