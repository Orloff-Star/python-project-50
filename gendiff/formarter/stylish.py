def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, int):
        return str(value)
    elif value is None:
        return 'null'
    else:
        return value


def build_diff(diff):
    differences = {}
    for item in diff:
        differences.update(search_fo_item(item))
    return differences


def search_fo_item(item):
    differences = {}
    if item['meaning'] == 'dicts':
        differences[f"    {item['key']}"
                    ] = build_diff(item['value'])
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
            result += f"{'    ' * depth}{key}: "
            result += get_format_dict(val, depth + 1) + '\n'
        result += '    ' * (depth) + '}'
    else:
        result = str(my_dict)
    return result


def get_all_keys(my_dict):
    if isinstance(my_dict, dict):
        for key, _ in list(my_dict.items()):
            if not isinstance(my_dict[key], dict):
                name = str(key)
                if name[0:2] != '  ':
                    my_dict[f'    {key}'] = my_dict[key]
                    del my_dict[key]
            else:
                get_all_keys(my_dict[key])
                name = str(key)
                if name[0:2] != '  ':
                    my_dict[f'    {key}'] = my_dict[key]
                    del my_dict[key]
    return get_format_dict(my_dict)


def convert_to_stylish(diff):
    return get_all_keys(build_diff(diff))
