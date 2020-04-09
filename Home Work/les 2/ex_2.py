# Для списка реализовать обмен значений соседних элементов, т.е. Значениями
# обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве
# элементов последний сохранить на своем месте. Для заполнения списка элементов
# необходимо использовать функцию input().

my_list = []


while True:
    ask_number_of_element = input('Сколько элементов вы хотите создать в списке : \n... ')

    if ask_number_of_element.isdigit():
        ask_number_of_element = int(ask_number_of_element)

        if ask_number_of_element < 3:
            print('Укажите число больше 3, это нужно для чистоты эксперимента!')
        else:
            break
    else:
        print('Введите целое число!')
        continue

i = 0
while ask_number_of_element != i:

    ask_element = input('Введите элементы поочередно и подвердите вводе элемента  : \n... ')
    my_list.append(ask_element)
    i += 1


print(my_list)


i = 0
while ask_number_of_element != i:
    if i > len(my_list):
        break
    else:
        my_list[i],my_list[i+1] = my_list[i+1],my_list[i]
        i += 2



print(my_list)