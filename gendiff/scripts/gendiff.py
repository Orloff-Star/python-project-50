#!/usr/bin/env python3
from gendiff.scripts.search_diff import generate_diff
from gendiff.scripts.parser import parse


def main():
    args = parse()
    print(generate_diff(args.first_file,
          args.second_file, args.format))


if __name__ == '__main__':
    main()
