def division(a,b):
    '''
    :param a: divident
    :param b: divisor
    :return:
    '''
    try:
        print(a / b)

    except ZeroDivisionError:
        print("Don't division by zero! B couldn't be 0 !")


while True:
    a = input('Input number a :... ')
    try:
        a = int(a)
    except ValueError:
        print('A must be a number!')
        continue

    while True:
        b = input('Input number b :... ')
        try:
            b = int(b)
            break
        except ValueError:
            print('B must be a number!')
            continue
    break

division(a,b)