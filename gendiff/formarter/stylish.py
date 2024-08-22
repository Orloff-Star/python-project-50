def get_normalise_string(string):
    if isinstance(string, bool):
        return str(string).lower()
    elif isinstance(string, int):
        return str(string)
    elif string is None:
        return 'null'
    else:
        return string


def stylish_dict(diff):
    differences = {}
    for i in diff:
        if i['meaning'] == 'dicts':
            differences[f"    {i['key']}"] = stylish_dict(i['value'])
        if i['meaning'] == 'identical':
            differences[f"    {i['key']}"] = get_normalise_string(i['value'])
        if i['meaning'] == 'update':
            differences[f"  - {i['key']}"] = get_normalise_string(i['old'])
            differences[f"  + {i['key']}"] = get_normalise_string(i['new'])
        if i['meaning'] == 'deleted':
            differences[f"  - {i['key']}"] = get_normalise_string(i['old'])
        if i['meaning'] == 'added':
            differences[f"  + {i['key']}"] = get_normalise_string(i['new'])
    return differences


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
