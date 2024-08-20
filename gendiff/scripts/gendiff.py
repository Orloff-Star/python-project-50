#!/usr/bin/env python3
from gendiff.scripts.search_diff import generate_diff
from gendiff.formarter.formarter_yaml import get_convert_file_to_dict
from gendiff.scripts.parser import parse


def main():
    args = parse()
    print(generate_diff(
        get_convert_file_to_dict(args.first_file),
        get_convert_file_to_dict(args.second_file)
    ))


if __name__ == '__main__':
    main()
