def division():
    '''
    :param a: divident
    :param b: divisor
    :return:
    '''

    while True:
        a = input('Input a number a :... ')
        if a.isdigit():
            a = int(a)
        else:
            print('A is not a number , please try again and input a number')
            continue

        b = input('Input a number b :... ')
        if b.isdigit():
            b = int(b)
        else:
            print('B is not a number , please try again and input a number')
            continue

        try:
            print(a / b)
            break
        except ZeroDivisionError:
            print("Don't division by zero! B couldn't be 0 !")
            continue


division()