from typing import Callable
from rx.core.typing import Observable, Action

SideEffect = Callable[[None], None]
Epic = Callable[[Observable[Action]], Observable[Action]]
