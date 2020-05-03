class ComplexNumb(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.c = complex(a,b)

    def __str__(self):
        return f'{self.c}'

    def __add__(self, other):
        return complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return complex(self.a * other.a, self.b * other.b)





if __name__ == '__main__':
    print(type(complex(1,3)))
    a = ComplexNumb(1,2)
    print(a)
    b = ComplexNumb(3,4)
    c = a + b
    d = a * b

    print(c)
    print(d)