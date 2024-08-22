def comparison_dict(file_one, file_two):
    keys = sorted(
        list(set(file_one.keys() | file_two.keys())))
    differences = []
    for key in keys:
        if key in file_one and key in file_two:
            if isinstance(file_one[key], dict) and isinstance(
                    file_two[key], dict):
                child = comparison_dict(
                    file_one[key], file_two[key])
                differences.append({'key': key,
                                    'meaning': 'dicts',
                                    'value': child})
            else:
                if file_one[key] == file_two[key]:
                    differences.append({'key': key,
                                        'meaning': 'identical',
                                        'value': file_one[key]})
                if file_one[key] != file_two[key]:
                    differences.append({'key': key,
                                        'meaning': 'update',
                                        'old': file_one[key],
                                        'new': file_two[key]})
        if key in file_one and key not in file_two:
            differences.append({'key': key,
                                'meaning': 'deleted',
                                'old': file_one[key]})
        if key not in file_one and key in file_two:
            differences.append({'key': key,
                                'meaning': 'added',
                                'new': file_two[key]})
    return differences
