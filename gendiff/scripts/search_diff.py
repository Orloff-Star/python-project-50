#from gendiff import parser
import json
import ast


file1 = json.load(open('gendiff/scripts/file1.json'))
file2 = json.load(open('gendiff/scripts/file2.json'))


def print_dictionary_row_by_row(dictionary):
    for key, value in dictionary.items():
        return f"{key}: {value}"


def generate_diff(file_one, file_two):
    
    differences = {}
    for key, value in file_one.items():
        if key not in file_two:
            key = f'- {key}'
            differences[key] = value
        elif value == file_two[key]:
            key = f'  {key}'
            differences[key] = value
        elif value != file_two[key]:
            key1 = f'- {key}'
            differences[key1] = value
            key2 = f'+ {key}'
            differences[key2] = file_two.get(key)
    for key, value in file_two.items():
        if key not in file_one:
            key = f'+ {key}'
            differences[key] = value
    differences = ast.literal_eval(str(differences).replace('"', "'"))


    return differences

    #return print_dictionary_row_by_row(differences)
print(generate_diff(file1, file2))
