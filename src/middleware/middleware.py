from src.store.action import Action
from src.store.store import Middleware, Store, Dispatcher, Dispatch, ActionProcessor


def epic_middleware(epics) -> Middleware:
    def with_store(store: Store) -> Dispatcher:
        def with_dispatch(next_dispatch: Dispatch) -> ActionProcessor:
            def action_processor(action: Action) -> Action:
                side_effects = []
                for epic in epics:
                    side_effects.append(epic(store.dispatch)(action))
                next_dispatch(action)
                for side_effect in side_effects:
                    side_effect()
                return action

            return action_processor

        return with_dispatch

    return with_store


def logging_middleware() -> Middleware:
    def with_store(store: Store) -> Dispatcher:
        def with_dispatch(next_dispatch: Dispatch) -> ActionProcessor:
            def action_processor(action: Action) -> Action:
                print('Dispatching ' + action.type)
                print('Previous state: ', store.get_state())
                next_dispatch(action)
                print('New state: ', store.get_state())
                return action

            return action_processor

        return with_dispatch

    return with_store
