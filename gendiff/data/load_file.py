import yaml
import os
import json


def format_yaml(file_path):
    with open(file_path, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data


def format_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def get_convert_file_to_dict(file_path):
    result = ''
    file_name = os.path.basename(file_path)
    if file_name[-4:] == '.yml' or file_name[-5:] == '.yaml':
        result = format_yaml(file_path)
    elif file_name[-5:] == '.json':
        result = format_json(file_path)
    return dict(result)
