from game.field import Field

class Resolver:
    def __init__(self, field: Field, max_solves: int):
        self.field = field
        self.max_solves = max_solves

    def find_solves(self):
        """Возвращает решения переданной головоломки, пока не знаю как: итератором или списком"""
        pass