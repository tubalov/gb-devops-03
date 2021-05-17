'''
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''

def sum_func(input_list):
    global user_sum
    input_list = list(map(int, input_list))
    user_sum += sum(input_list)
    print('Сумма чисел:', user_sum)

print('Введите значения через пробел, для выхода введите q ')
user_sum = 0
while True:
    user_input = input()
    input_list = user_input.split()
    if 'q' in input_list and len(input_list) == 1:
        break
    elif 'q' in input_list and len(input_list) > 1:
        input_list.remove('q')
        sum_func(input_list)
        break

    sum_func(input_list)