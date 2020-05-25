class Action:
    def __init__(self, type: str, payload=None):
        if payload is None:
            payload = {}
        self.type = type
        self.payload = payload
