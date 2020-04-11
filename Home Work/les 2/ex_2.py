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
for step in range(0,ask_number_of_element-1,2):
        my_list[step], my_list[step+1] = my_list[step+1], my_list[step]



print(my_list)