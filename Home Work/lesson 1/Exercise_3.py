def under_zero(value):

    try:
        int(value)
        return True

    except ValueError:
        return False


while True:

    print('Для выхода напишите выход, для счета введите целое число')

    ask_number = input('Введите целое число:\n')

    if ask_number == 'выход': break

    if ask_number.isdigit() or under_zero(ask_number):

        if int(ask_number) > 0:
            num_one = ask_number
            num_twice = ask_number * 2
            num_trinity = ask_number * 3
            print(num_one, num_twice, num_trinity)
            print(int(num_one) + int(num_twice) + int(num_trinity))

        elif int(ask_number) < 0:
            num_one = ask_number
            num_one = ask_number
            num_twice = ask_number* 2
            num_trinity = ask_number * 3
            print(num_one, num_twice, num_trinity)
            num_twice = int(ask_number) + int(ask_number)
            num_trinity = int(ask_number) + int(ask_number) + int(ask_number)
            print(int(num_one) + int(num_twice) + int(num_trinity))

        elif int(ask_number) == 0:
            print('0','00','000')
            print(0)
    else:
        print('Ввведите целое число')
        continue