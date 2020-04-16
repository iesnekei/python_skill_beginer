# several different method to get all element from origin list if element > previous element

origin_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 53]
result = [12, 44, 4, 10, 78, 123]

new_list = []

i = 1


while i < len(origin_list):
    if origin_list[i] > origin_list[i-1]:
        new_list.append(origin_list[i])
        i += 1
    else:
        i += 1

print(new_list)


new_list = []
a = 1
for i in origin_list[:-1]:
    if i < origin_list[a]:
        new_list.append(origin_list[a])
        a += 1
    else:
        a += 1

print(new_list)

a = 0
new_list = [i for i in origin_list[1:] if i > origin_list[origin_list.index(i)-1]]

print(new_list)



