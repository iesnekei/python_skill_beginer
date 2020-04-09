user_long_string = input('Please write a sentence : \n... ')
user_long_string = user_long_string.split()

# or use enumerate (but output would be not such friendly)

i = 1
for element in user_long_string:
    print(f'{i} {element:.10}')
    i += 1