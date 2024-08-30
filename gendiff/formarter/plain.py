def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, int):
        return str(value)
    elif value is None:
        return 'null'
    else:
        return f"'{value}'"


def build_path(diff, path=''):
    differences = []
    for item in diff:
        nested_path = f"{path}.{item['key']}" if path else item['key']
        if item['meaning'] == 'dicts':
            differences.append(build_path(item['value'], nested_path))
        if item['meaning'] == 'update':
            differences.append(f"Property '{nested_path}' was updated. "
                               f"From {format_value(item['old'])} "
                               f"to {format_value(item['new'])}")
        if item['meaning'] == 'deleted':
            differences.append(f"Property '{nested_path}' was removed")
        if item['meaning'] == 'added':
            differences.append(f"Property '{nested_path}' was added "
                               f"with value: {format_value(item['new'])}")
    result = '\n'.join(str(x) for x in differences)
    return result


def convert_to_plain(diff):
    result = build_path(diff)
    return result
