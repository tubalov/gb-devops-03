user_seconds = int(input('Введите количество секунд: '))

if user_seconds > 0:
    hours = user_seconds // 3600
    minutes = (user_seconds - hours * 3600) // 60
    seconds = (user_seconds - hours * 3600) - minutes * 60
    print(f'{hours}:{minutes}:{seconds}')
else:
    print('Неверный ввод')