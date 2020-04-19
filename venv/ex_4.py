with open('ex_4.txt','r') as f:
    my_str = f.readline()
    my_list = my_str.split(' ')
    my_list[0] = 'Один'
    my_str = ' '.join(my_list)
    with open('ex_4_out.txt','a') as fi:
        fi.write(my_str)
    my_str = f.readline()
    my_list = my_str.split(' ')
    my_list[0] = 'Два'
    my_str = ' '.join(my_list)
    with open('ex_4_out.txt', 'a') as fi:
        fi.write(my_str)
    my_str = f.readline()
    my_list = my_str.split(' ')
    my_list[0] = 'Три'
    my_str = ' '.join(my_list)
    with open('ex_4_out.txt', 'a') as fi:
        fi.write(my_str)
    my_str = f.readline()
    my_list = my_str.split(' ')
    my_list[0] = 'Четыре'
    my_str = ' '.join(my_list)
    with open('ex_4_out.txt', 'a') as fi:
        fi.write(my_str)

with open('ex_4.txt','r') as f:
    rus_numb = ["один","два","три","четыре"]
    count = 0
    for i in f:
        my_list = i.split(' ')
        my_list[0] = rus_numb[count]
        count += 1
        my_str = ' '.join(my_list)
        with open('ex_4_out.txt', 'a') as fi:
            fi.write(my_str)
# also it could be changed by if construction for working with information if we don't know what in ex_4.txt