from gendiff import generate_diff
import pytest
import os
import json


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


result = read(get_fixture_path('Expected_output_generate_diff.txt'))
file1 = json.load(open('tests/fixtures/file1.json'))
file2 = json.load(open('tests/fixtures/file2.json'))


def test_generate_diff():
    assert generate_diff(file1, file2) == result
