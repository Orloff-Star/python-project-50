from gendiff.formarter.stylish import comparison_dict, get_all_keys


def generate_diff(file_one, file_two, formarter='stylish'):
    result = comparison_dict(file_one, file_two)
    if formarter == 'stylish':
        return get_all_keys(result)
