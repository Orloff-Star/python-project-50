def format_value(string):
    if isinstance(string, bool):
        return str(string).lower()
    elif isinstance(string, int):
        return str(string)
    elif string is None:
        return 'null'
    else:
        return string


def convert_to_stylish(diff):
    differences = {}
    for item in diff:
        if item['meaning'] == 'dicts':
            differences[f"    {item['key']}"
                        ] = convert_to_stylish(item['value'])
        if item['meaning'] == 'identical':
            differences[f"    {item['key']}"
                        ] = format_value(item['value'])
        if item['meaning'] == 'update':
            differences[f"  - {item['key']}"
                        ] = format_value(item['old'])
            differences[f"  + {item['key']}"
                        ] = format_value(item['new'])
        if item['meaning'] == 'deleted':
            differences[f"  - {item['key']}"
                        ] = format_value(item['old'])
        if item['meaning'] == 'added':
            differences[f"  + {item['key']}"
                        ] = format_value(item['new'])
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
