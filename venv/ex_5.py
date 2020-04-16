from functools import reduce

def myultiply(prev_el,el):
    return prev_el * el

sum_range = [x for x in range(100,1001) if x % 2 == 0]

print(reduce(myultiply,sum_range))