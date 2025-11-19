from game.field import Field
from generate.field_generator import FieldGenerator
from solver import Solver
from interface.writer import Writer


class Creator:
    def __init__(self, width: int, height: int, num_components: int,
                 max_solves: int, generate_fields: int = 1):
        self.width = width
        self.height = height

        self.num_components = num_components
        self.max_solves = max_solves
        self.generate_fields = generate_fields

        self.generator = FieldGenerator(self.width, self.height)

    def create(self):
        counter = 0

        while counter < self.generate_fields:
            field = self.generator.generate_field()
            solver = Solver(
                field=field,
                num_components=self.num_components,
                max_solves=self.max_solves,
            )

            solves = list(solver.solve())
            if solves:
                counter += 1

                self.print_task_and_solution(field, solves)

    @staticmethod
    def print_task_and_solution(field: Field, solves: list[Field]):
        print(Writer.parse_field_to_text(field), end='\n\n')

        for solve in solves:
            print(Writer.parse_field_to_text(solve), end='\n')

        print('---')
