import yaml
import os
import json


def format_yaml(file_path):

    with open(file_path, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data


def get_convert_file_to_dict(file):
    file_name = os.path.basename(file)
    if file_name[-4:] == '.yml' or file_name[-5:] == '.yaml':
        return format_yaml(file)
    elif file_name[-5:] == '.json':
        return json.load(open(file))
