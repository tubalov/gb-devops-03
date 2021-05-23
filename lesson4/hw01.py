'''
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''

import sys

try:
    file, hours, rate, bonus = sys.argv
except ValueError:
    print('Неверные аргументы')
    exit()

def salary_calc(hours, rate, bonus):
    try:
        salary = (hours * rate) + bonus
        return salary
    except TypeError:
        return

print('Зарплата сотрудника:', salary_calc(int(hours), int(rate), int(bonus)))