import argparse
from gendiff.scripts.Parsing import parsing
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain


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
    formatter = args.format
    file1, file2 = parsing(path_to_file1, path_to_file2)
    if formatter:
        generate_diff(file1, file2, formatter)
    else:
        generate_diff(file1, file2)


def generate_diff(file1, file2, formatter="stylish"):
    result = ''
    match formatter:
        case "stylish":
            result = stylish(diff(file1, file2))
        case "plain":
            result = plain(diff(file1, file2))
    print(result)
    return result


def diff(diff_file1, diff_file2):
    def item_only_in_one(inner_key, inner_value, tag=' '):
        inner_result = dict()
        if type(inner_value) is dict:
            inner_result["tag"] = tag
            inner_result["key"] = inner_key
            inner_result['value'] = []
            for inner_key, inner_value in inner_value.items():
                inner_result['value'].append(item_only_in_one(inner_key,
                                                              inner_value))
        else:
            inner_result["tag"] = tag
            inner_result["key"] = inner_key
            inner_result['value'] = inner_value
        return inner_result

    result = []
    for key, value in diff_file1.items():
        if key in diff_file2:
            if diff_file1[key] == diff_file2[key]:
                result.append(item_only_in_one(key, value))
            else:
                if type(diff_file1[key]) is dict and \
                        type(diff_file2[key]) is dict:
                    temp_dict = dict()
                    temp_dict['tag'] = ' '
                    temp_dict['key'] = key
                    temp_dict['value'] = diff(diff_file1[key], diff_file2[key])
                    result.append(temp_dict)
                else:
                    result.append(item_only_in_one(key, value, '-'))
                    result.append(item_only_in_one(key, diff_file2[key], '+'))
        else:
            result.append(item_only_in_one(key, value, '-'))

    for key, value in diff_file2.items():
        if key in diff_file1:
            continue
        else:
            result.append(item_only_in_one(key, value, '+'))
    return result


if __name__ == '__main__':
    main()
