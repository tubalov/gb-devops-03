'''
6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:

[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:

{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
'''

products = []

user_attr = (input('Введите через пробел характеристики товаров]: ')).split(' ')


prod_amount = input('Введите количество товаров для ввода: ')
if prod_amount.isdigit() and int(prod_amount) > 0:

    for i in range(int(prod_amount)):
        user_inp = (input('Введите через пробел название, цену, количество и ед. измерения: ')).split(' ')
        if len(user_inp) == 4 and user_inp[1].isdigit() and user_inp[2].isdigit():
            # Сравнить длину списка с атрибутами user_attr и длину списка значений user_inp.
            # Если ок, то сделать промежуточный список и вложить его в кортеж при формировании


            products.append((i+1, {'название': user_inp[0], 'цена': int(user_inp[1]), 'количество': int(user_inp[2]), 'ед': user_inp[3]}))
        else:
            print('Неверный формат ввода')
            continue

print(products)

prod_attr = {}




