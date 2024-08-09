#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')

parser.add_argument(metavar='first_file', dest='first_file')
parser.add_argument(metavar='second_file', dest='second_file')
parser.add_argument("-f", "--format", metavar="FORMAT",
                    help="set format of output")

args = parser.parse_args()
print(args.accumulate(args.integers))
