def get_normalise_string(string):
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


def plain_dict(diff, path=''):
    differences = []
    for i in diff:
        nested_path = f"{path}.{i['key']}" if path else i['key']
        if i['meaning'] == 'dicts':
            differences.append(plain_dict(i['value'], nested_path))
        if i['meaning'] == 'update':
            differences.append(f"Property '{nested_path}' was updated. "
                               f"From {get_normalise_string(i['old'])} "
                               f"to {get_normalise_string(i['new'])}")
        if i['meaning'] == 'deleted':
            differences.append(f"Property '{nested_path}' was removed")
        if i['meaning'] == 'added':
            differences.append(f"Property '{nested_path}' was added "
                               f"with value: {get_normalise_string(i['new'])}")
    result = ''
    for item in differences:
        result += f'{item}\n'
    return result.replace('\n\n', '').rstrip('\n')
