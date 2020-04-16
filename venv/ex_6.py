from itertools import count,cycle

start_from = 1  # here can be input
finish_on = 10  # here can be input

for x in count(start_from):
    if x > finish_on:
        break
    print(x)




list_to_repeat = ['l','o','l']

repeat_time = 3*len(list_to_repeat) #here can be input

i = 0

for x in cycle(list_to_repeat):
    if i >= repeat_time:
        break
    print(x)
    i += 1