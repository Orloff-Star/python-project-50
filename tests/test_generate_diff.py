from gendiff import generate_diff
import os
import pytest

def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result

result = read(get_fixture_path('Expected_output_generate_diff.txt'))
result_stylish = read(get_fixture_path('Expected_result_of_investment.txt'))
result_plain = read(get_fixture_path('Expected_output_plain.txt'))
result_json = read(get_fixture_path('Expected_output_json.txt'))
file1_json = 'tests/fixtures/file1.json'
file2_json = 'tests/fixtures/file2.json'
file1_yaml = 'tests/fixtures/file1.yaml'
file2_yaml = 'tests/fixtures/file2.yaml'
file1_json_investment = 'tests/fixtures/file1-big.json'
file2_json_investment = 'tests/fixtures/file2-big.json'
file1_yaml_investment = 'tests/fixtures/file1-big.yml'
file2_yaml_investment = 'tests/fixtures/file2-big.yml'


@pytest.mark.parametrize("file_1, file_2, formarter, expected_output",
                         [
                            (   
                                file1_json,
                                file2_json,
                                'stylish',
                                result
                            ),
                            (
                                file1_yaml,
                                file2_yaml,
                                'stylish',
                                result
                            ),
                            (
                                file1_json_investment,
                                file2_json_investment,
                                'stylish',
                                result_stylish
                            ),
                            (
                                file1_yaml_investment,
                                file2_yaml_investment,
                                'stylish',
                                result_stylish
                            ),
                            (
                                file1_json_investment,
                                file2_json_investment,
                                'plain',
                                result_plain
                            ),
                            (
                                file1_yaml_investment,
                                file2_yaml_investment,
                                'plain',
                                result_plain
                            ),
                            (
                                file1_json_investment,
                                file2_json_investment,
                                'json',
                                result_json
                            ),
                            (
                                file1_yaml_investment,
                                file2_yaml_investment,
                                'json',
                                result_json
                            )
                            
                        ]
                        )


def test_generate_diff(file_1, file_2, formarter, expected_output):
    assert generate_diff(file_1, file_2, formarter) == expected_output
