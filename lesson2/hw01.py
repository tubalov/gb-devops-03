'''
1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
'''

types_list = [677, 'текст', True, None, [1, 2, 'элемент'], {'a', 'b', 'c'}, {'модель': '620', 'мощность': 400}]

for element in types_list:
    print(f'Элемент {element} - тип {str(type(element))[8:-2]}')