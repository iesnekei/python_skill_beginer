def isfloat(Value):
    try:
        float(Value)
        return True
    except ValueError:
        return False


def division():
    ask_numerator = input('Input number for division:... ')

    if ask_numerator.isdigit():
        ask_numerator = int(ask_numerator)

    elif isfloat(ask_numerator):
        ask_numerator = float(ask_numerator)

    else:
        print('Input a number!')

    ask_denominator = input('Input number for division by it:... ')

    if ask_denominator.isdigit():
        ask_denominator = int(ask_denominator)

    elif isfloat(ask_denominator):
        ask_denominator = float(ask_denominator)

    else:
        print('Input a number!')

    try:
        result = ask_numerator / ask_denominator
        return result

    except ZeroDivisionError:
        print("Don't division by zero!")


print(division())