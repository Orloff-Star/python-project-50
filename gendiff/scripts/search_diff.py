from gendiff.formarter.stylish import stylish_dict, get_all_keys
from gendiff.scripts.comparison_dict import comparison_dict
from gendiff.formarter.plain import plain_dict
from gendiff.formarter.json import json_dict
from gendiff.formarter.formarter_yaml import get_convert_file_to_dict


def generate_diff(path_1, path_2, formarter='stylish'):
    file_one = get_convert_file_to_dict(path_1)
    file_two = get_convert_file_to_dict(path_2)
    result = comparison_dict(file_one, file_two)
    if formarter == 'plain':
        return plain_dict(result)
    elif formarter == 'json':
        return json_dict(result)
    else:
        return get_all_keys(stylish_dict(result))
