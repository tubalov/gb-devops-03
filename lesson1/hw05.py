revenue = float(input('Введите значение выручки: '))
cost = float(input('Введите значение издержек: '))


profit = revenue - cost
print(profit)
if profit <= 0:
    print('Фирма отработала с убытком:', profit)
else:
    print('Фирма отработала с прибылью:', profit)
    profit_margin = profit / revenue * 100
    print(profit_margin)
    emp_num = int(input('Введите количество сотрудников: '))
    emp_profit = profit / emp_num
    print('Прибыль на сотрудника: ', emp_profit)
