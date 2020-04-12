def from_str_to_list_of_number(str):
    str = str.split(' ')
    return str

def sum_of_number_in_list(list):
    b = 0
    for i in list:
        if i == '*':
            break
        else:
            a = int(i)
            b += a
    return b

growing_number = 0

while True:
    ask_numbers_row = input('Please input a row of numbers separating by space! Or input * to exit:...')
    if '*' in ask_numbers_row:
        my_list = from_str_to_list_of_number(ask_numbers_row)
        result = sum_of_number_in_list(my_list)
        growing_number += result
        print(growing_number)
        break
    else:
        my_list = from_str_to_list_of_number(ask_numbers_row)
        result = sum_of_number_in_list(my_list)
        growing_number += result
        print(growing_number)

