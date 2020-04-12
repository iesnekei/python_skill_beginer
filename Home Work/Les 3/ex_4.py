def x_raise_y(x,y):
    if y < 0:
        y = abs(y)
    if y == 0:
        x = 1
        a = 1
    else:
        a = x
        for z in range(1,y):
            a = a * x

    print(a)

x_raise_y(2,4)