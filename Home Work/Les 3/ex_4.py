def x_raise_y(x,y):
    result = x **y
    print(f'{result:.4f}')

x_raise_y(2.2,-4)

def x_raise_y_2(x,y):
    if y >= 0:
        z = x
        for i in range(0,(y-1)):
            x *= z
        return x
    if y < 0:
        z = x
        for i in range(0,(abs(y)-1)):
            x *= z
    result = 1 / x
    return result


print(f'{x_raise_y_2(2.2,-4):.4f}')