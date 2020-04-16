def fact(n):
    x = 1
    for i in range(x,n+1):
        x *= i
        yield x
        i += 1

for el in fact(4):
    print(el)


