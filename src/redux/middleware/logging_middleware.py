from redux.store import Store, Action
from redux.store.store import Dispatch


def logging_middleware():
    def with_store(store: Store):
        def with_dispatch(next_dispatch: Dispatch):
            def action_processor(action: Action) -> Action:
                print('Dispatching ' + action.type)
                print('Previous state: ', store.get_state())
                next_dispatch(action)
                print('New state:      ', store.get_state())
                print()
                return action

            return action_processor

        return with_dispatch

    return with_store