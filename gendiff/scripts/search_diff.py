#from gendiff import parser
import json


file1 = json.load(open('gendiff/scripts/file1.json'))
file2 = json.load(open('gendiff/scripts/file2.json'))

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
    for key, value in file_one.items():
        if key not in file_two:
            key = f'- {key}'
            differences[key] = get_normalise_string(value)
        elif value == file_two[key]:
            key = f'  {key}'
            differences[key] = get_normalise_string(value)
        elif value != file_two[key]:
            key1 = f'- {key}'
            differences[key1] = get_normalise_string(value)
            key2 = f'+ {key}'
            differences[key2] = file_two.get(key)
    for key, value in file_two.items():
        if key not in file_one:
            key = f'+ {key}'
            differences[key] = get_normalise_string(value)
    differenc = dict(sorted(differences.items(), key=lambda x: x[0][2]))
    for key, value in differenc.items():
        sub_result = f'\n{key}: {value}'
        result += sub_result
    return f'{{{result}\n}}'
    
print(generate_diff(file1, file2))


