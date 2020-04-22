with open('my_file_for_work_with_it.txt') as f_change:
    i = 0
    for str in f_change:
        i += 1
    print(f'Opened file has {i} strings.\n')


with open('my_file_for_work_with_it.txt') as f_change:
    i = 1
    for str in f_change:
        print(f'String {i} has {len(str)} symbols.')
        i += 1

print('\nAnother way to do it \n')

f_change = open('my_file_for_work_with_it.txt','r')
i = 0
b = 1
for str in f_change:
    i += 1
    print(f'sString {i} has {len(str)} symbols.')
    b += 1
print(f'\nOpened file has {i} strings.\n')

f_change.close()