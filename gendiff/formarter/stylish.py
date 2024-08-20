def get_normalise_string(string):
    if isinstance(string, bool):
        return str(string).lower()
    elif isinstance(string, int):
        return str(string)
    elif string is None:
        return 'null'
    else:
        return string


def comparison_dict(file_one, file_two):
    keys = file_one.keys() | file_two.keys()
    differences = {}
    for key in keys:
        if key in file_one and key in file_two:
            if isinstance(file_one[key], dict) and isinstance(
                    file_two[key], dict):
                differences[f'    {key}'] = comparison_dict(
                    file_one[key], file_two[key])
            else:
                if file_one[key] == file_two[key]:
                    differences[f'    {key}'] = get_normalise_string(
                        file_one[key])
                if file_one[key] != file_two[key]:
                    key1 = f'  - {key}'
                    differences[key1] = get_normalise_string(file_one[key])
                    key2 = f'  + {key}'
                    differences[key2] = get_normalise_string(file_two[key])
        if key in file_one and key not in file_two:
            differences[f'  - {key}'] = get_normalise_string(file_one[key])
        if key not in file_one and key in file_two:
            differences[f'  + {key}'] = get_normalise_string(file_two[key])
    differences_sort = dict(sorted(
        differences.items(), key=lambda x: (x[0][4:])))
    return differences_sort


def get_format_dict(my_dict, depth=0):
    if isinstance(my_dict, dict):
        result = '{\n'
        for key, val in my_dict.items():
            result += f"{'    '*depth}{key}: "
            result += get_format_dict(val, depth + 1) + '\n'
        result += '    ' * (depth) + '}'
    else:
        result = str(my_dict)
    return result


def get_all_keys(my_dict):
    if isinstance(my_dict, dict):
        for key in my_dict.copy():
            if not isinstance(my_dict[key], dict):
                name = str(key)
                if name[0:2] != '  ':
                    my_dict[f'    {key}'] = my_dict.pop(key)
            else:
                get_all_keys(my_dict[key])
                name = str(key)
                if name[0:2] != '  ':
                    my_dict[f'    {key}'] = my_dict.pop(key)
    return get_format_dict(my_dict)
