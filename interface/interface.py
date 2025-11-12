import argparse
import os
import sys
from game.cell import Cell
from game.field import Field
from game.resolver import Resolver
from game.state import State

def parse_lines_to_field(lines):
    field = []
    width = -1
    for line in lines:
        line = line.strip()
        numbers = list(map(lambda x: Cell(int(x), State.UNPAINTED), line.split()))
        if width == -1:
            width = len(numbers)
        else:
            if len(numbers) != width:
                raise ValueError("incorrect input")
        field.append(numbers)
    return Field(field)

def parse_field_to_text(field):
    text = ""
    for line in field.cells:
        text += ' '.join(str(cell.value) if cell.is_unpainted else "#" for cell in line)
        text += '\n'
    return text


def get_path(filename):
    if os.path.exists(filename):
        return filename
    else:
        return os.path.join(os.getcwd(), filename)

def solve(field):
    solutions = list()
    print("Solving...")
    for s in Resolver.find_solves(field, max_solves = 2):
        print("found!")
        solutions.append(parse_field_to_text(s))
    return solutions

def solve_file(filename):
    field = parse_lines_to_field(open(get_path(filename)).readlines())
    solutions = solve(field)
    print('\n'.join(solutions))
