'''
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
'''

def int_func(user_string):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for word in user_string:
        wrong_sym = []
        for letter in word:
            if letter not in letters:
                wrong_sym.append(letter)
        if len(wrong_sym) == 0:
            print(word.capitalize(), end=' ')

user_string = input('Введите слова из маленьких латинских букв через пробел: ')
user_list = user_string.split()

int_func(user_list)