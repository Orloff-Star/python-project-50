from gendiff.formarter.stylish import stylish_dict, get_all_keys
from gendiff.scripts.comparison_dict import comparison_dict
from gendiff.formarter.plain import plain_dict


def generate_diff(file_one, file_two, formarter='stylish'):
    result = comparison_dict(file_one, file_two)
    if formarter == 'stylish':
        return get_all_keys(stylish_dict(result))
    if formarter == 'plain':
        return plain_dict(result)
