from game.field import Field


class Resolver:
    @staticmethod
    def find_solves(field: Field, max_solves: int = 5):
        solve_counter = [0]
        yield from Resolver._find_solves_recursive(field.copy(),
                                                          max_solves,
                                                          solve_counter)

    @staticmethod
    def _find_solves_recursive(current_field: Field, max_solves: int,
                               solve_counter: list[int]):
        if 0 < max_solves <= solve_counter[0]:
            return

        try:
            x, y = next((r, c) for r in range(current_field.width) for c in
                        range(current_field.height) if
                        current_field.cells[r][c].is_unpainted)
        except StopIteration:
            if current_field.is_solve():
                solve_counter[0] += 1
                yield current_field
            return

        next_field_unpainted = current_field.copy()
        yield from Resolver._find_solves_recursive(
            next_field_unpainted.cells[x][y].paint() or next_field_unpainted,
            max_solves, solve_counter)

        equals = current_field.find_equal_cells(x, y)

        if equals:
            next_field_painted = current_field.copy()
            next_field_painted.cells[x][y].paint()

            for i, j in equals:
                next_field_painted.cells[i][j].paint()

            yield from Resolver._find_solves_recursive(
                next_field_painted, max_solves, solve_counter)
