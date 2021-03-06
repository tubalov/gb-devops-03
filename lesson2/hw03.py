'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''
user_month = input('Введите месяц в виде целого числа от 1 до 12: ')

if not user_month.isdigit():
    print('Неверный формат ввода')
    exit()
elif int(user_month) < 1 or int(user_month) > 12:
    print('Введите целое число от 1 до 12')
    exit()

# Вариант через list
season_list = [['зима', 1, 2, 12], ['весна', 3, 4, 5], ['лето', 6, 7, 8], ['осень', 9, 10, 11]]
for season in season_list:
    if int(user_month) in season:
        print(season[0])

# Вариант через dict
season_dict = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето',
9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}

print(season_dict[int(user_month)])