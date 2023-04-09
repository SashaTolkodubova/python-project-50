import argparse
import json


def main():
    parser = argparse.ArgumentParser(
        'Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        help='FORMAT'
    )
    args = parser.parse_args()
    path_to_file1 = args.first_file
    path_to_file2 = args.second_file
    generate_diff(path_to_file1, path_to_file2)


def generate_diff(file_path1, file_path2):

    with open(file_path1, 'r') as file1_json:
        file1 = json.load(file1_json)
    with open(file_path2, 'r') as file2_json:
        file2 = json.load(file2_json)

    keys1 = list(file1.keys())
    keys2 = list(file2.keys())
    keys = list(set(keys1 + keys2))
    keys.sort()
    result = "{"
    for key in keys:
        if key in file1 and key in file2:
            if file1[key] == file2[key]:
                result += f"\n    {key}: {file1[key]}"
            else:
                result += f"\n  - {key}: {file1[key]}"
                result += f"\n  + {key}: {file2[key]}"
        elif key in file1:
            result += f"\n  - {key}: {file1[key]}"
        elif key in file2:
            result += f"\n  + {key}: {file2[key]}"
    result += "\n}"
    return result


if __name__ == '__main__':
    main()
