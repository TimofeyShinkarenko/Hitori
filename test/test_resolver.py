import unittest
from game.cell import Cell
from game.field import Field
from game.resolver import Resolver
from game.state import State


class TestResolver(unittest.TestCase):
    def test_find_solves_simple(self):
        cells = [
            [Cell(1, State.UNPAINTED), Cell(2, State.UNPAINTED)],
            [Cell(2, State.UNPAINTED), Cell(1, State.UNPAINTED)]
        ]
        field = Field(cells)

        resolver = Resolver(field=field, max_solves=2, num_components=1)

        solves = list(resolver.find_solves())

        self.assertGreaterEqual(len(solves), 1)


if __name__ == '__main__':
    unittest.main()