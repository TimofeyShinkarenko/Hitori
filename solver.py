import os
from game.resolver import Resolver
from game.parser import Parser
from interface.writer import Writer


class Solver:
    def __init__(self, filename: str, max_solves: int):
        with open(filename, 'r') as f:
            data = f.readlines()
            self.field = Parser.parse_lines_to_field(data)

        self.max_solves = max_solves

    @staticmethod
    def get_path(filename):
        if os.path.exists(filename):
            return filename
        else:
            return os.path.join(os.getcwd(), filename)

    def solve(self):
        for solve in Resolver.find_solves(self.field, self.max_solves):
            yield solve

    def print(self):
        for solve in self.solve():
            print(Writer.parse_field_to_text(solve), end='\n\n')
