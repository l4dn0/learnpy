import ast
def str_to_list(data):

    print("Получение " + data)
    print(type(data))
    text = data

    text = text.replace("(", "['")

    text = text.replace(")", "']")

    text = text.replace(" ", "', '")

    text = text.replace("'[", "['")

    text = text.replace("]'", "']")

    text = text.replace("'',", "")

    text = text.replace("]']", "]]")

    text = text.replace("['[", "[[")

    text = text.replace("''", "'")

    text = text.replace("]']", "]]")

    parsed_list = ast.literal_eval(text)
    print("Конвертация успешна:")


    print(parsed_list)
    print(type(parsed_list))
    return parsed_list