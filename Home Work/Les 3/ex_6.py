def func(text):
    text = text[:]
    text = text[0].capitalize() + text[1:]
    return text
print(func('text'))
print(func('hahah'))

str_to_change = input('Input a string with several word and only small letter:... ')

list_of_str = str_to_change.split(' ')

b = 0


for i in list_of_str:
    a = func(i)
    list_of_str[b] = a
    b += 1


list_of_str = ' '.join(list_of_str)

print(list_of_str)