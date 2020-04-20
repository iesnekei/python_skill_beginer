with open('ex_6.txt','r') as f:
    my_dict = {}
    for i in f:
        my_list = i.split(' ')

        if ':' in my_list[0]:
            my_list[0] = my_list[0].replace(':','')

        if '(h)' in my_list[1]:
            my_list[1] = my_list[1].replace('(h)','')

        if '(hw)' in my_list[2]:
            my_list[2] = my_list[2].replace('(hw)','')


        if '(ex)' in my_list[3]:
            my_list[3] = my_list[3].replace('(ex)','')

        for i in my_list:
            if '\n' in i:
                my_list[my_list.index(i)] = my_list[my_list.index(i)].replace('\n','')

        for i in my_list:
            if '--' in i:
                my_list.pop(my_list.index('--'))
                my_list.pop(my_list.index('--'))

        a = 0

        for i in my_list:
            if i.isdigit():
                a += int(i)
        new_list = my_list[0:1]
        new_list.append(a)


        my_dict[new_list[0]] = new_list[1]


    print(my_dict)

