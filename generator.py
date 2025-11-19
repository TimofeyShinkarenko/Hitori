#!/usr/bin/env python3
import argparse


def parse_arguments():
    generator_parser = argparse.ArgumentParser(description='Generator')

    generator_parser.add_argument(
        '-f', '--fields',
        type=int,
        default=1,
        help='number of fields to generate'
    )
    generator_parser.add_argument(
        '-h', '--height',
        type=int,
        help='height of the field'
    )
    generator_parser.add_argument(
        '-w', '--width',
        type=int,
        help='width of the field'
    )
    generator_parser.add_argument(
        "-m", "--max_solves",
        type=int,
        default=5,
        help='max number of solves'
    )
    generator_parser.add_argument(
        "-c", "--num_components",
        type=int,
        default=1,
        help='number of connected components'
    )

    return generator_parser.parse_args()


def run():
    pass


if __name__ == '__main__':
    run()
