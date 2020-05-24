class Store:
    def __init__(self, state, reducers: []):
        self.__state = state
        self.__reducers = reducers

    def dispatch(self, action):
        for reducer in self.__reducers:
            name = reducer.__name__
            self.__state[name] = reducer(action, self.__state[name])
