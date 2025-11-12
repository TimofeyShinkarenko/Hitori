import argparse
import os
import sys
from interface.interface import get_path, solve_file

hitori_parser = argparse.ArgumentParser(description='Hitori')

hitori_parser.add_argument('--open', required = True, help = 'open file')
hitori_parser.add_argument('--solve', action="store_true", help = 'solves hitori')

args = hitori_parser.parse_args()
path = None
if args.open:
    path = get_path(args.open)

if args.solve:
    print(solve_file(path))