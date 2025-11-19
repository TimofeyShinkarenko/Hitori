import copy
from collections import deque
from game.cell import Cell


class Field:
    def __init__(self, cells: list[list[Cell]]):
        self.cells = cells

    @property
    def width(self):
        return len(self.cells)

    @property
    def height(self):
        return len(self.cells[0])

    def paint_over(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            cell = self.cells[x][y]

            if cell.is_unpainted:
                cell.paint()
            else:
                cell.unpaint()

    def has_no_painted_neighbors(self) -> bool:
        for x in range(self.width):
            for y in range(self.height):

                if self.cells[x][y].is_painted:
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < self.width and 0 <= ny < self.height:
                            if self.cells[nx][ny].is_painted:
                                return False
        return True

    def count_unpainted_components(self, num_components: int) -> bool:
        visited = set()
        components = 0

        for x in range(self.width):
            for y in range(self.height):

                if self.cells[x][y].is_unpainted and (x, y) not in visited:
                    components += 1

                    q = deque([(x, y)])
                    visited.add((x, y))

                    while q:
                        curr_x, curr_y = q.popleft()

                        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nx, ny = curr_x + dx, curr_y + dy
                            neighbor = (nx, ny)

                            if (0 <= nx < self.width and
                                    0 <= ny < self.height and
                                    self.cells[nx][ny].is_unpainted and
                                    neighbor not in visited):
                                visited.add(neighbor)
                                q.append(neighbor)

        return components == num_components

    def are_unpainted_values_unique(self) -> bool:
        for y in range(self.height):
            seen_in_row = set()

            for x in range(self.width):
                cell = self.cells[x][y]

                if cell.is_unpainted:
                    if cell.value in seen_in_row:
                        return False

                    seen_in_row.add(cell.value)

        for x in range(self.width):
            seen_in_column = set()

            for y in range(self.height):
                cell = self.cells[x][y]

                if cell.is_unpainted:
                    if cell.value in seen_in_column:
                        return False

                    seen_in_column.add(cell.value)

        return True

    def find_equal_cells(self, row_i: int, col_i: int) -> list[
        tuple[int, int]]:
        equal_cells_indexes = []
        target_cell = self.cells[row_i][col_i]
        target_value = target_cell.value

        for y in range(self.height):
            if y == col_i:
                continue

            current_cell = self.cells[row_i][y]
            if current_cell.is_unpainted and current_cell.value == target_value:
                equal_cells_indexes.append((row_i, y))

        for x in range(self.width):
            if x == row_i:
                continue

            current_cell = self.cells[x][col_i]
            if current_cell.is_unpainted and current_cell.value == target_value:
                equal_cells_indexes.append((x, col_i))

        return equal_cells_indexes

    def is_solve(self, num_components: int) -> bool:
        return self.count_unpainted_components(num_components) and self.are_unpainted_values_unique() and self.has_no_painted_neighbors()

    def copy(self):
        new_cells = [[copy.deepcopy(cell) for cell in row] for row in
                     self.cells]
        return Field(new_cells)
