from game.field import Field


class Resolver:
    def __init__(self, field: Field, max_solves: int = 5,
                 num_components: int = 1):
        self.max_solves = max_solves
        self.num_components = num_components
        self.field = field
        self.solve_counter = 0

    def find_solves(self):
        yield from self._find_solves_recursive(self.field.copy(), 0, 0)

    def _find_solves_recursive(self, current_field: Field, x: int, y: int):
        if 0 < self.max_solves <= self.solve_counter:
            return

        if x >= current_field.width:
            if current_field.is_solve(self.num_components):
                self.solve_counter += 1
                yield current_field

            return

        next_x = x + 1
        next_y = y

        if next_x >= current_field.width:
            next_x = 0
            next_y = y + 1

            if next_y >= current_field.height:
                if current_field.is_solve(self.num_components):
                    self.solve_counter += 1
                    yield current_field

                return

        if current_field.cells[x][y].is_painted:
            yield from self._find_solves_recursive(current_field, next_x,
                                                       next_y)
            return

        can_be_painted = True
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < current_field.width and 0 <= ny < current_field.height:
                if current_field.cells[nx][ny].is_painted:
                    can_be_painted = False
                    break

        if can_be_painted:
            painted_field = current_field.copy()
            painted_field.cells[x][y].paint()

            yield from self._find_solves_recursive(painted_field, next_x,
                                                       next_y)

        unpainted_field = current_field.copy()
        yield from self._find_solves_recursive(unpainted_field, next_x,
                                                   next_y)
