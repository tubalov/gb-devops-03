'''
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
'''

inp_list = [2, 2, 2, 7, 23, 1, 44, 44, 2, 3, 2, 10, 7, 14, 14, 8, 4, 11]
out_list = [x for x in inp_list if (inp_list.count(x) == 1)]

print(inp_list)
print(out_list)