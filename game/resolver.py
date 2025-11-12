from game.field import Field


class Resolver:
    @staticmethod
    def find_solves(field: Field, max_solves: int = 5):
        solve_counter = [0]
        yield from Resolver._find_solves_recursive(field.copy(), 0, 0,
                                                   max_solves,
                                                   solve_counter)

    @staticmethod
    def _find_solves_recursive(current_field: Field, x: int, y: int,
                               max_solves: int,
                               solve_counter: list[int]):
        if 0 < max_solves <= solve_counter[0]:
            return

        if x >= current_field.width:
            if current_field.is_solve():
                solve_counter[0] += 1
                yield current_field

            return

        next_x = x + 1
        next_y = y

        if next_x >= current_field.width:
            next_x = 0
            next_y = y + 1

            if next_y >= current_field.height:
                if current_field.is_solve():
                    solve_counter[0] += 1
                    yield current_field

                return

        if current_field.cells[x][y].is_painted:
            yield from Resolver._find_solves_recursive(current_field, next_x,
                                                       next_y,
                                                       max_solves,
                                                       solve_counter)
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

            yield from Resolver._find_solves_recursive(painted_field, next_x,
                                                       next_y,
                                                       max_solves,
                                                       solve_counter)

        unpainted_field = current_field.copy()
        yield from Resolver._find_solves_recursive(unpainted_field, next_x,
                                                   next_y,
                                                   max_solves,
                                                   solve_counter)