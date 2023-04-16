import json
import os

import yaml


def parsing(file_path1, file_path2):
    file1_name, file1_extension = os.path.splitext(file_path1)
    file2_name, file2_extension = os.path.splitext(file_path2)
    if file1_extension == '.json' and file2_extension == '.json':
        with open(file_path1, 'r') as file1_json:
            file1 = json.load(file1_json)
        with open(file_path2, 'r') as file2_json:
            file2 = json.load(file2_json)
        return file1, file2
    elif file1_extension == '.yml' and file2_extension == '.yml' \
            or file1_extension == '.yaml' and file2_extension == '.yaml':
        with open(file_path1, 'r') as file1_yml:
            file1 = yaml.safe_load(file1_yml)
        with open(file_path2, 'r') as file2_yml:
            file2 = yaml.safe_load(file2_yml)
        return file1, file2
