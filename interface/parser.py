from game.cell import Cell
from game.field import Field
from game.state import State


class Parser:
    @staticmethod
    def parse_lines_to_field(lines):
        cells = []
        width = -1

        for line in lines:
            line = line.strip()
            numbers = list(
                map(lambda x: Cell(int(x), State.UNPAINTED), line.split()))

            if width == -1:
                width = len(numbers)
            elif len(numbers) != width:
                raise ValueError("incorrect input")

            cells.append(numbers)

        return Field(cells)
