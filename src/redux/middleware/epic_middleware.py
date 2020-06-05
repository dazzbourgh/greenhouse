from typing import List

import rx
from rx.scheduler import ThreadPoolScheduler

from epics import Epic
from redux.middleware.state_scheduler import state_scheduler


def epic_middleware(epics: List[Epic]):
    epic_scheduler = ThreadPoolScheduler(1)

    def s(store):
        def n(next_dispatch):
            def a(action):
                rx.of(action).subscribe(lambda act: next_dispatch(act),
                                        scheduler=state_scheduler)
                for epic in epics:
                    epic(rx.of(action)).subscribe(lambda act: store.dispatch(act),
                                                  scheduler=epic_scheduler)

            return a

        return n

    return s