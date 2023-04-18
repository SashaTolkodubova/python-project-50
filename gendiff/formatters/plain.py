def plain(doc):
    result = list()

    def first(i, path):
        if type(i['value']) is list:
            path += f".{i['key']}"
            inner(i['value'], path)
        else:
            return

    def for_other(doc_other, path):
        for i in doc_other:
            i = i[0]
            if i['tag'] == ' ':
                first(i, path)
            elif i['tag'] == '-':
                temp = "Property " + "'" + (path + "." + i['key'])[1:] + \
                       "' was removed"
                result.append(temp)
            elif i['tag'] == '+':
                temp = "Property " + "'" + (path + "." + i['key'])[1:] \
                       + f"' was added with value: " \
                         f"{is_value_complex(i['value'])}"
                result.append(temp)

    def for_updates(doc_updates, path):
        for item1, item2 in doc_updates:
            temp = "Property " + "'" + (path + "." + item1['key'])[1:] \
                   + f"' was updated. From " \
                     f"{is_value_complex(item1['value'])} " \
                     f"to {is_value_complex(item2['value'])}"
            result.append(temp)

    def inner(doc_inner, path=''):
        doc_inner = sorted(doc_inner, key=lambda x: x['key'])
        updated, other_inner = is_updated(doc_inner)
        for_other(other_inner, path)
        for_updates(updated, path)

    inner(doc)
    result = sorted(result, key=take_path)
    result = make_string(result)
    result = result[:-1]
    return result


def make_string(array):
    result_str = ''
    for item in array:
        result_str += item + "\n"
    return result_str


def is_updated(doc_upd):
    result_inner = list()
    for i in doc_upd:
        result_inner.append([x for x in doc_upd if i['key'] == x['key']])
    more_one = list(filter(lambda x: len(x) > 1, result_inner))
    less_one = list(filter(lambda x: len(x) < 2, result_inner))
    uniq = []
    uniq_result = [x for x in more_one if x not in uniq and not uniq.append(x)]
    return uniq_result, less_one


def is_value_complex(i):
    if type(i) is list:
        return '[complex value]'
    elif i == 'false' or i == 'true' or i == 'null' or type(i) == int:
        return i
    else:
        return f"'{i}'"


def take_path(sentence):
    word = ''
    flag = False
    for char in sentence:
        if char == "'":
            flag = not flag
        if flag:
            word += char
    return word


