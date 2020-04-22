def del_symbol(el,i):
    if el in my_list[i]:
        my_list[i] = my_list[i].replace(el, '')



if __name__ == '__main__':
    with open('ex_6.txt', 'r') as f:
        my_dict = {}


        for i in f:
            my_list = i.split(' ')

            del_symbol(':', 0)
            del_symbol('(h)', 1)
            del_symbol('hw', 2)
            del_symbol('ex', 3)


            for i in my_list:
                if '\n' in i:
                    my_list[my_list.index(i)] = my_list[my_list.index(i)].replace('\n', '')

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

