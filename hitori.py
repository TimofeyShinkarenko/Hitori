#!/usr/bin/env python3
import argparse
from solver import Solver


def parse_arguments():
    hitori_parser = argparse.ArgumentParser(description='Hitori')

    hitori_parser.add_argument(
        "-m", "--max_solves",
        type=int,
        default=5,
        help='max number of solves'
    )
    hitori_parser.add_argument(
        "-c", "--num_components",
        type=int,
        default=1,
        help='number of connected components'
    )
    hitori_parser.add_argument(
        'filename',
        type=str,
        help='input filename'
    )

    return hitori_parser.parse_args()


def run():
    args = parse_arguments()

    solver = Solver(
        filename=args.filename,
        max_solves=args.max_solves,
        num_components=args.num_components
    )

    solver.print()


if __name__ == '__main__':
    run()
