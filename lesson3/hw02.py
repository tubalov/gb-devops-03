'''
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
'''

user_params = ['Jerry', 'Lee', '2000', 'New York', 'jerry_lee@gmail.com', '(812) 6546724']

def user_params_print(name, surname, year_birth, city, email, phone):
    print(f'Имя: {name}, фамилия: {surname}, год рождения: {year_birth}, город проживания: {city}, email: {email}, телефон: {phone}')

user_params_print(*user_params)