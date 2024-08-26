def format_value(string):
    if isinstance(string, dict):
        return '[complex value]'
    elif isinstance(string, bool):
        return str(string).lower()
    elif isinstance(string, int):
        return str(string)
    elif string is None:
        return 'null'
    else:
        return f"'{string}'"


def convert_to_plain(diff):
    def inner(object, path=''):
        differences = []
        for item in object:
            nested_path = f"{path}.{item['key']}" if path else item['key']
            if item['meaning'] == 'dicts':
                differences.append(inner(item['value'], nested_path))

            if item['meaning'] == 'update':
                differences.append(f"Property '{nested_path}' was updated. "
                                   f"From {format_value(item['old'])} "
                                   f"to {format_value(item['new'])}")
            if item['meaning'] == 'deleted':
                differences.append(f"Property '{nested_path}' was removed")
            if item['meaning'] == 'added':
                differences.append(f"Property '{nested_path}' was added "
                                   f"with value: {format_value(item['new'])}")
        result = '\n'.join(differences)
        return result
    return inner(diff)
