class DroneState:
    @staticmethod
    def run(context):
        assert False, "run not implemented"

    @staticmethod
    def next_state(context):
        return None


class DroneStateMachine:
    def __init__(self, initial_state):
        self.__state = initial_state
        self.__context = {}

    def get_context(self):
        return self.__context

    def set_context(self, key, value):
        self.__context[key] = value

    def run(self):
        current_state = self.__state
        while current_state is not None:
            current_state.run(self.__context)
            current_state = current_state.next_state(self.__context)
