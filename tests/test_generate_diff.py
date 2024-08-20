from gendiff import generate_diff
import pytest
import os
import json
import yaml


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


result = read(get_fixture_path('Expected_output_generate_diff.txt'))
file1_json = json.load(open('tests/fixtures/file1.json'))
file2_json = json.load(open('tests/fixtures/file2.json'))
file1_yaml = yaml.safe_load(open('tests/fixtures/file1.yaml'))
file2_yaml = yaml.safe_load(open('tests/fixtures/file2.yaml'))

def test_generate_diff():
    assert generate_diff(file1_json, file2_json) == result
    assert generate_diff(file1_yaml, file2_yaml) == result


result_investment = read(get_fixture_path('Expected_result_of_investment.txt'))
file1_json_investment = json.load(open('tests/fixtures/file1-big.json'))
file2_json_investment = json.load(open('tests/fixtures/file2-big.json'))
file1_yaml_investment = yaml.safe_load(open('tests/fixtures/file1-big.yaml'))
file2_yaml_investment = yaml.safe_load(open('tests/fixtures/file2-big.yaml'))


def test_generate_diff_2():
    assert generate_diff(file1_yaml_investment, file2_yaml_investment) == result_investment
    assert generate_diff(file1_json_investment, file2_json_investment) == result_investment