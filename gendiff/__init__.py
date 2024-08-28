from gendiff.data.search_diff import generate_diff
from gendiff.data.load_file import convert_file_to_dict
from gendiff.data.parser import parse_args
from gendiff.formarter.stylish import convert_to_stylish
from gendiff.formarter.plain import convert_to_plain
from gendiff.formarter.json import convert_to_json


__all__ = (
    'generate_diff',
    'convert_file_to_dict',
    'parse_args',
    'convert_to_stylish',
    'convert_to_plain',
    'convert_to_json'
)
