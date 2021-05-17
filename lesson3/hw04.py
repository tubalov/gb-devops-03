'''
4. Программа принимает действительное положительное число x и целое отрицательное число y. 
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
** Подсказка:** попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''

# Способ 1 — возведение в степень с помощью оператора **
def my_func(x, y):
    z = x ** y
    print('Способ 1', z)

x = 10
y = -7

my_func(x, y)

# Способ 2 - использование цикла
def my_func(x, y):
    z = 1
    for i in range(abs(y)):
        z = z / x
    print('Способ 2', z)

x = 10
y = -7

my_func(x, y)

