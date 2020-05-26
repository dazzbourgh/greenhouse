from typing import Callable

from src.actions.action_types import SET_TEMPERATURE
from src.redux.store.action import Action

Controller = Callable[[Action], None]

temperature_controller: Controller = lambda action: print('---Updating temp', action.payload[
    'temperature']) if action.type == SET_TEMPERATURE else None
