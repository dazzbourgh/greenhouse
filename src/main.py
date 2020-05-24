from src.store.action import Action
from src.store.reducers import temperature
from src.store.store import Store

if __name__ == '__main__':
    store = Store({'temperature': 50}, [temperature])
    store.dispatch(Action('TEMP', {'temperature': 80}))
