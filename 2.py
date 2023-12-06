#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def transliterate(t, chars=" !?"):
    def decorator(func):
        def wrapper(s):
            # Преобразование строки в нижний регистр
            s_lower = s.lower()

            # Замена русских букв на латинские с использованием словаря t
            for cyrillic, latin in t.items():
                s_lower = s_lower.replace(cyrillic, latin)

            # Замена символов chars на дефис
            for char in chars:
                s_lower = s_lower.replace(char, '-')

            # Приведение подряд идущих дефисов к одному
            s_lower = '-'.join(filter(None, s_lower.split('-')))

            # Вызов и возврат результата функции
            return func(s_lower)

        return wrapper

    return decorator

@transliterate({'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'})
def transform_string(s):
    return s

if __name__ == "__main__":
    input_string = "Привет, мир! Как дела?"
    result = transform_string(input_string)
    print("Результат преобразования:", result)


