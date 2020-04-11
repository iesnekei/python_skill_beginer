my_list = [9, 5, 6, 8, 1]

while True:
    ask_new_element = input('Write a number :\n ...')
    if ask_new_element.isdigit():
        ask_new_element = int(ask_new_element)
        my_list.append(ask_new_element)
        my_list.sort(reverse = True)
        print(my_list)
        break
    else:
        print('Please write a NUMBER')
        continue