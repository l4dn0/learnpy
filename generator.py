def generate_python_code(parsed_frame):
    classes = {}  # {class_name: set(methods)}

    def recursive_search(items, current_data):
        """Рекурсивный поиск субъектов, действий и объектов"""
        if isinstance(items, list):
            for item in items:
                if isinstance(item, list):
                    # Обрабатываем элементы с тегами
                    if item and isinstance(item[0], str):
                        tag = item[0]
                        # Извлекаем субъект (класс)
                        if tag == ':sub':
                            for part in item:
                                if isinstance(part, list) and part[0] == ':prop_noun':
                                    class_name = part[2].replace(':', '').strip().capitalize()
                                    current_data['class'] = class_name
                                    if class_name not in classes:
                                        classes[class_name] = set()

                        # Извлекаем действие (глагол)
                        elif tag == ':act_VERB':
                            verb = item[1].replace(':', '').strip().lower()
                            current_data['verb'] = verb

                        # Извлекаем объект
                        elif tag == ':obj_name':
                            for part in item:
                                if isinstance(part, list) and part[0] == ':prop_noun':
                                    obj = part[2].replace(':', '').strip().lower()
                                    current_data['obj'] = obj

                    # Продолжаем рекурсивный поиск
                    recursive_search(item, current_data)

    # Обрабатываем все предложения
    for entry in parsed_frame:
        for sentence in entry:  # Входные данные имеют дополнительный уровень вложенности
            current_data = {'class': None, 'verb': None, 'obj': None}
            recursive_search(sentence, current_data)

            # Формируем метод
            if current_data['class'] and current_data['verb']:
                method = current_data['verb']
                if current_data['obj']:
                    method += '_' + current_data['obj']
                classes[current_data['class']].add(method)

    # Генерация кода
    code = ""
    for class_name, methods in classes.items():
        code += f"class {class_name}:\n    def init(self):\n        pass\n\n"
        for method in sorted(methods):
            code += f"    def {method}(self):\n        pass\n\n"

    return code


def generate_c_sharp_code(parsed_frame):
    classes = {}  # {class_name: set(methods)}

    def recursive_search(items, current_data):
        """Рекурсивный поиск субъектов, действий и объектов"""
        if isinstance(items, list):
            for item in items:
                if isinstance(item, list):
                    # Обрабатываем элементы с тегами
                    if item and isinstance(item[0], str):
                        tag = item[0]
                        # Извлекаем субъект (класс)
                        if tag == ':sub':
                            for part in item:
                                if isinstance(part, list) and part[0] == ':prop_noun':
                                    class_name = part[2].replace(':', '').strip().capitalize()
                                    current_data['class'] = class_name
                                    if class_name not in classes:
                                        classes[class_name] = set()

                        # Извлекаем действие (глагол)
                        elif tag == ':act_VERB':
                            verb = item[1].replace(':', '').strip().lower()
                            current_data['verb'] = verb
# Извлекаем объект
                        elif tag == ':obj_name':
                            for part in item:
                                if isinstance(part, list) and part[0] == ':prop_noun':
                                    obj = part[2].replace(':', '').strip().lower()
                                    current_data['obj'] = obj

                    # Продолжаем рекурсивный поиск
                    recursive_search(item, current_data)

    # Обрабатываем все предложения
    for entry in parsed_frame:
        for sentence in entry:  # Входные данные имеют дополнительный уровень вложенности
            current_data = {'class': None, 'verb': None, 'obj': None}
            recursive_search(sentence, current_data)

            # Формируем метод
            if current_data['class'] and current_data['verb']:
                method = current_data['verb']
                if current_data['obj']:
                    method += '_' + current_data['obj']
                classes[current_data['class']].add(method)

    # Генерация кода
    code = ""
    a = '{'
    b = '}'
    for class_name, methods in classes.items():
        code += f"class {class_name}{a}\n    public {class_name}(){a}\n        {b}\n\n"
        for method in sorted(methods):
            code += f"    void {method}(){a}\n        {b}\n\n"
    code += f"\n{b}"
    return code