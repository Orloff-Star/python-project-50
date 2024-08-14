#!/usr/bin/env python3
from  gendiff.scripts.search_diff import generate_diff
import argparse
import json

def parse():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')

    parser.add_argument(metavar='first_file', dest='first_file')
    parser.add_argument(metavar='second_file', dest='second_file')
    parser.add_argument("-f", "--format", metavar="FORMAT",
                    help="set format of output")

    return parser.parse_args()
#print(args.accumulate(args.integers))


file1 = json.load(open('gendiff/scripts/file1.json'))
file2 = json.load(open('gendiff/scripts/file2.json'))
def main():
    args = parse()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
