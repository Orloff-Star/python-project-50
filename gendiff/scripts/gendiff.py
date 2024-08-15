#!/usr/bin/env python3
from gendiff.scripts.search_diff import generate_diff
import argparse
import json


def parse():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file', metavar='first_file')
    parser.add_argument('second_file', metavar='second_file')
    parser.add_argument("-f", "--format", metavar="FORMAT",
                        help="set format of output")

    return parser.parse_args()


def main():
    args = parse()
    print(generate_diff(
        json.load(open(args.first_file)), json.load(open(args.second_file))
    ))


if __name__ == '__main__':
    main()
