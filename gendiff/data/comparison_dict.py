def comparison_dict(file_one, file_two):
    keys = sorted(
        list(set(file_one.keys() | file_two.keys())))
    differences = []
    for key in keys:
        differences.append(serch_fo_key(file_one, file_two, key))
    return differences


def serch_fo_key(file_one, file_two, key):
    result = {}
    if key not in file_two:
        result = {'key': key,
                  'meaning': 'deleted',
                  'old': file_one[key]}
    elif key not in file_one:
        result = {'key': key,
                  'meaning': 'added',
                  'new': file_two[key]}
    elif isinstance(file_one[key], dict) and isinstance(
            file_two[key], dict):
        child = comparison_dict(
            file_one[key], file_two[key])
        result = {'key': key,
                  'meaning': 'dicts',
                  'value': child}
    elif file_one[key] == file_two[key]:
        result = {'key': key,
                  'meaning': 'identical',
                  'value': file_one[key]}
    elif file_one[key] != file_two[key]:
        result = {'key': key,
                  'meaning': 'update',
                  'old': file_one[key],
                  'new': file_two[key]}
    return result
