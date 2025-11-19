import random
from game.cell import Cell
from game.state import State
from game.field import Field


class FieldGenerator:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    @staticmethod
    def generate_cell():
        return Cell(random.randint(0, 100), State.UNPAINTED)

    def generate_field(self):
        cells = []

        for y in range(self.height):
            row = []

            for x in range(self.width):
                row.append(self.generate_cell())

            cells.append(row)

        return Field(cells)
