def isfloat(Value):
    try:
        float(Value)
        return True
    except ValueError:
        return False

def bigest_number_of_3():

    a = input('Input a number!')
    try:
        if a.isdigit():
            a = int(a)

        elif isfloat(a):
            a = float(a)

    except ValueError:
        print('Input a number!')

    b = input('Input a number!')
    try:
        if b.isdigit():
            b = int(b)

        elif isfloat(b):
            b = float(b)

    except ValueError:
        print('Input a number!')

    c = input('Input a number!')
    try:
        if c.isdigit():
            c = int(c)

        elif isfloat(c):
            c = float(c)

    except ValueError:
        print('Input a number!')

    max_number_1 = max(a,b)
    max_number_2 = max(b,c)
    sum_of_numb = max_number_2 + max_number_1
    return sum_of_numb

print(bigest_number_of_3())
