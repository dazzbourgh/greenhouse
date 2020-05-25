from typing import Callable

from rx import Observable

Epic = Callable[[Observable], Observable]
