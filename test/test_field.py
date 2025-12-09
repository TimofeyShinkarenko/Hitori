import unittest
from game.cell import Cell
from game.field import Field
from game.state import State


class TestField(unittest.TestCase):
    @staticmethod
    def create_test_field():
        cells = [
            [Cell(1, State.UNPAINTED), Cell(2, State.UNPAINTED)],
            [Cell(3, State.UNPAINTED), Cell(4, State.UNPAINTED)]
        ]
        return Field(cells)

    def test_paint_over(self):
        field = self.create_test_field()
        field.paint_over(0, 0)
        self.assertTrue(field.cells[0][0].is_painted)

        field.paint_over(0, 0)
        self.assertTrue(field.cells[0][0].is_unpainted)

    def test_paint_over_invalid_coords(self):
        field = self.create_test_field()
        field.paint_over(-1, -1)
        field.paint_over(100, 100)

    def test_has_no_painted_neighbors(self):
        field = self.create_test_field()
        self.assertTrue(field.has_no_painted_neighbors())

        field.cells[0][0].paint()
        self.assertTrue(field.has_no_painted_neighbors())

        field.cells[0][1].paint()
        self.assertFalse(field.has_no_painted_neighbors())

    def test_count_unpainted_components(self):
        field = self.create_test_field()

        self.assertTrue(field.count_unpainted_components(1))

        field.cells[0][0].paint()
        self.assertTrue(field.count_unpainted_components(1))

    def test_are_unpainted_values_unique(self):
        cells = [
            [Cell(1, State.UNPAINTED), Cell(2, State.UNPAINTED)],
            [Cell(1, State.UNPAINTED), Cell(3, State.UNPAINTED)]
        ]
        field = Field(cells)

        self.assertFalse(field.are_unpainted_values_unique())

    def test_is_solve(self):
        field = self.create_test_field()
        self.assertTrue(field.is_solve(num_components=1))

    def test_copy(self):
        field = self.create_test_field()
        field_copy = field.copy()

        self.assertEqual(field.width, field_copy.width)
        self.assertEqual(field.height, field_copy.height)

        field_copy.cells[0][0].paint()
        self.assertTrue(field_copy.cells[0][0].is_painted)
        self.assertTrue(field.cells[0][0].is_unpainted)


if __name__ == '__main__':
    unittest.main()