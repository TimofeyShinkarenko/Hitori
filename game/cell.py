from game.state import State


class Cell:
    def __init__(self, value: int, state: State):
        self.value = value
        self.state = state

    def is_painted(self):
        return self.state == State.PAINTED

    def is_unpainted(self):
        return self.state == State.UNPAINTED

    def paint(self):
        self.state = State.PAINTED