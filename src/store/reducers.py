from src.store.action import Action


def temperature(action: Action, state=70):
    if action.type == 'TEMP':
        return action.payload['temperature']
    else:
        return state
