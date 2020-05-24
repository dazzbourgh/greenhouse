from src.store.action import Action
from src.store.store import Middleware, Store, Dispatcher, Dispatch, ActionProcessor


# todo
def epic_middleware() -> Middleware:
    pass


def logging_middleware() -> Middleware:
    def with_store(store: Store) -> Dispatcher:
        def with_dispatch(dispatch: Dispatch) -> ActionProcessor:
            def action_processor(action: Action) -> Action:
                print('Dispatching ' + action.type)
                print('Previous state: ', store.get_state())
                dispatch(action)
                print('New state: ', store.get_state())
                return action

            return action_processor

        return with_dispatch

    return with_store
