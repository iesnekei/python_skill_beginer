import random

ask_str_list = []

i = 1

while i <= random.randint(1,3):

    ask_str = input('Введите какое нибудь слово:\n')

    if ask_str.isdigit():
        print('Введите слово а не число')
        continue

    else:
        ask_str_list.append(ask_str)
        i += 1

print(ask_str_list)

ask_int_list = []

def isfloat(value):

    try:
        float(value)
        return True

    except ValueError:
        return False
i = 1

while i <= random.randint(1,3):
    ask_int = input('Введите какое нибудь число :\n')
    if isfloat(ask_int):
        ask_int_list.append(ask_int)
        i += 1
    else:
        print('Введите число!')
        continue

print(ask_int_list)
