# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_number = input('Введите целое положительное число, не жалейте цифр ,\n чем больше тем лучше :\n => ')
i = 0
max_numb = 0
while len(user_number) > i:
    if int(user_number[i]) > max_numb:
        max_numb = int(user_number[i])
    i += 1
print(max_numb)