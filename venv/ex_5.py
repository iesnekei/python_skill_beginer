from random import randint
with open('ex_5.txt','w') as f:
    my_list = [i for i in range(randint(1,1000))]
    print(f'In my file {len(my_list)} numbers')
    for i in my_list:
        f.write(str(i)+' ')

with open('ex_5.txt','r') as f:
    my_str = f.read()
    my_list = my_str.split(' ')
    result = 0
    for i in my_list:
        if not i.isdigit():
            my_list.pop(my_list.index(i))
    for i in my_list:
        result += int(i)
    print(f'Sum of all numbers are {result}.')