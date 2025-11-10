from game.cell import Cell


class Field:
    def __init__(self, cells: list[list[Cell]]):
        self.cells = cells

    def paint_over(self, x, y):
        pass
