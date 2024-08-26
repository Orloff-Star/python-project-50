from gendiff.formarter.stylish import convert_to_stylish, get_all_keys
from gendiff.data.comparison_dict import comparison_dict
from gendiff.formarter.plain import convert_to_plain
from gendiff.formarter.json import convert_to_json
from gendiff.data.load_file import get_convert_file_to_dict


def generate_diff(path_1, path_2, formarter='stylish'):
    file_one = get_convert_file_to_dict(path_1)
    file_two = get_convert_file_to_dict(path_2)
    result = comparison_dict(file_one, file_two)
    if formarter == 'plain':
        return convert_to_plain(result)
    elif formarter == 'json':
        return convert_to_json(result)
    else:
        return get_all_keys(convert_to_stylish(result))
