import yaml
import os
import json


def download_yaml(file_path):
    with open(file_path, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data


def download_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def convert_file_to_dict(file_path):
    result = ''
    file_name = os.path.basename(file_path)
    _, ext = os.path.splitext(file_name)
    if ext == '.yml' or ext == '.yaml':
        result = download_yaml(file_path)
    elif ext == '.json':
        result = download_json(file_path)
    return dict(result)
