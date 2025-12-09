import sys
from PyQt5.QtWidgets import QApplication

from generate.field_generator import FieldGenerator
from solver import Solver
from gui.SolutionViewer import SolutionViewer


class Creator:
    def __init__(self, width: int, height: int, num_components: int,
                 max_solves: int, generate_fields: int = 1):
        self.width = width
        self.height = height

        self.num_components = num_components
        self.max_solves = max_solves
        self.generate_fields = generate_fields

        self.generator = FieldGenerator(self.width, self.height)

    def run_gui(self):
        app = QApplication(sys.argv)

        tasks_data = []
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
                tasks_data.append((field, solves))

        if tasks_data:
            window = SolutionViewer(tasks_data)
            window.show()
            sys.exit(app.exec_())
        else:
            print("Не удалось сгенерировать корректные поля.")