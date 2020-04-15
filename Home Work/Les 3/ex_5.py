def sum_of_number_in_list(list):
    b = 0
    for i in list:
        if i == '*':
            break
        else:
            try:
                a = int(i)
                b += a
            except ValueError:
                print("Don't input letter or more that 1 space between numbers or space in the end!!!\n"
                      "Or * without space before!!!")

    return b

growing_number = 0

while True:
    ask_numbers_row = input('Please input a row of numbers separating by space! Or input * to exit:... ')

    if '*' in ask_numbers_row:
        my_list = ask_numbers_row.split(' ')
        result = sum_of_number_in_list(my_list)
        growing_number += result
        print(growing_number)
        break

    else:
        my_list = ask_numbers_row.split(' ')
        result = sum_of_number_in_list(my_list)
        growing_number += result
        print(growing_number)

