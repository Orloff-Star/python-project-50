def get_normalise_string(string):
    if isinstance(string, bool):
        return str(string).lower()
    elif isinstance(string, str):
        return string.strip(' " " ')
    elif isinstance(string, int):
        return str(string)
    else:
        return string


def generate_diff(file_one, file_two):
    result = ''
    differences = {}
    if isinstance(file_one, dict):
        for key, val in file_one.items():
            if key not in file_two:
                key = f'  - {key}'
                differences[key] = get_normalise_string(val)
            elif val == file_two[key]:
                key = f'    {key}'
                differences[key] = get_normalise_string(val)
            elif val != file_two[key]:
                key1 = f'  - {key}'
                differences[key1] = get_normalise_string(val)
                key2 = f'  + {key}'
                differences[key2] = file_two.get(key)
    if isinstance(file_two, dict):
        for key, val in file_two.items():
            if key not in file_one:
                key = f'  + {key}'
                differences[key] = get_normalise_string(val)
    differenc = dict(sorted(differences.items(), key=lambda x: x[0][4]))
    for key, val in differenc.items():
        sub_result = f'\n{key}: {val}'
        result += sub_result
    return f'{{{result}\n}}'

'''import json
file1 = json.load(open('tests/fixtures/file1.json'))
file2 = json.load(open('tests/fixtures/file1.yaml'))

print(file1)
print(file2)'''