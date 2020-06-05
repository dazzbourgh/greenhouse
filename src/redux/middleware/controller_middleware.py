from typing import List

import rx
from rx.scheduler import ThreadPoolScheduler

from controllers.controllers import Controller
from redux.middleware.state_scheduler import state_scheduler


def controller_middleware(controllers: List[Controller]):
    controller_scheduler = ThreadPoolScheduler(1)

    def s(store):
        def n(next_dispatch):
            def a(action):
                rx.of(action).subscribe(lambda act: next_dispatch(act),
                                        scheduler=state_scheduler)
                for controller in controllers:
                    rx.of(action).subscribe(lambda act: controller(act, store.get_state()),
                                            scheduler=controller_scheduler)

            return a

        return n

    return s
