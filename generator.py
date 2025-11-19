#!/usr/bin/env python3
import argparse
from creator import Creator


def parse_arguments():
    generator_parser = argparse.ArgumentParser(description='Field Generator')

    generator_parser.add_argument(
        '-f', '--fields',
        type=int,
        default=1,
        help='Number of fields to generate'
    )
    generator_parser.add_argument(
        '-H', '--height',
        type=int,
        required=True,
        help='Height of the field (required)'
    )
    generator_parser.add_argument(
        '-W', '--width',
        type=int,
        required=True,
        help='Width of the field (required)'
    )
    generator_parser.add_argument(
        "-m", "--max_solves",
        type=int,
        default=5,
        help='Max number of solves'
    )
    generator_parser.add_argument(
        "-c", "--num_components",
        type=int,
        default=1,
        help='Number of connected components'
    )

    return generator_parser.parse_args()


def run():
    args = parse_arguments()

    creator = Creator(
        width=args.width,
        height=args.height,
        max_solves=args.max_solves,
        num_components=args.num_components,
        generate_fields=args.fields,
    )

    creator.create()


if __name__ == '__main__':
    run()
