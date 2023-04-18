def stylish(doc, level=0):
    def inner(inner_doc, inner_level):
        inner_doc = sorted(inner_doc, key=lambda x: x['key'])
        print("{", end='')
        for i in inner_doc:
            if type(i['value']) is list:
                print(f"\n{'    ' * inner_level}  "
                      f"{i['tag']} {i['key']} ", end='')
                stylish(i['value'], inner_level + 1)
            else:
                print(f"\n{'    ' * inner_level}  {i['tag']} "
                      f"{i['key']}: {i['value']}", end='')
        print(f"\n{'    ' * inner_level}{'}'}", end='')

    def returner(returner_doc, returner_level):
        returner_doc = sorted(returner_doc, key=lambda x: x['key'])
        result = ''
        result += '{'
        for i in returner_doc:
            if type(i['value']) is list:
                result += f"\n{'    ' * returner_level}  " \
                          f"{i['tag']} {i['key']}: "
                result += returner(i['value'], returner_level + 1)
            else:
                if i['value'] == '':
                    result += f"\n{'    ' * returner_level}  " \
                              f"{i['tag']} {i['key']}:"
                else:
                    result += f"\n{'    ' * returner_level}  " \
                              f"{i['tag']} {i['key']}: {i['value']}"
        result += f"xxx\n{'    ' * returner_level}{'}'}"
        return result
    return returner(doc, level)
