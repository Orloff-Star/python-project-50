from gendiff.formarter.stylish import convert_to_stylish
from gendiff.data.comparison_dict import comparison_dict
from gendiff.formarter.plain import convert_to_plain
from gendiff.formarter.json import convert_to_json
from gendiff.data.load_file import convert_file_to_dict


def generate_diff(path_1, path_2, formarter='stylish'):
    file_one = convert_file_to_dict(path_1)
    file_two = convert_file_to_dict(path_2)
    result = comparison_dict(file_one, file_two)
    if formarter == 'plain':
        return convert_to_plain(result)
    elif formarter == 'json':
        return convert_to_json(result)
    elif formarter == 'stylish':
        return convert_to_stylish(result)
