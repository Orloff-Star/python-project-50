#from gendiff import parser
import json


#file1 = json.load(open('gendiff/scripts/file1.json'))
#file2 = json.load(open('gendiff/scripts/file2.json'))

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


'''def generate_diff(file_one, file_two):
    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)'''


#print(generate_diff(file1, file2))




