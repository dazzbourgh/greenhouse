from typing import Callable
from rx.core.typing import Observable

from src.store.action import Action

SideEffect = Callable[[None], None]
Epic = Callable[[Observable[Action]], Observable[Action]]
