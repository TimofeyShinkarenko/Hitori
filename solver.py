import os
import sys
from PyQt5.QtWidgets import QApplication

from game.field import Field
from game.resolver import Resolver
from interface.parser import Parser
from gui.SolutionViewer import SolutionViewer


class Solver:
    def __init__(self, max_solves: int, num_components: int,
                 filename: str = None, field: Field = None):
        if filename is not None:
            with open(filename, 'r') as f:
                data = f.readlines()
                self.field = Parser.parse_lines_to_field(data)

        else:
            self.field = field

        self.max_solves = max_solves
        self.num_components = num_components

    @staticmethod
    def get_path(filename):
        if os.path.exists(filename):
            return filename
        else:
            return os.path.join(os.getcwd(), filename)

    def solve(self):
        hitori_solver = Resolver(
            num_components=self.num_components,
            field=self.field,
            max_solves=self.max_solves,
        )

        for solve in hitori_solver.find_solves():
            yield solve

    def show_gui(self):
        app = QApplication(sys.argv)
        solutions = list(self.solve())
        data = [(self.field, solutions)]

        window = SolutionViewer(data)
        window.show()
        sys.exit(app.exec_())