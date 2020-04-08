# Узнайте у пользователя число n.Найдите сумму
# чисел n + nn + nnn.Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

while True:
    print('Для выхода напишите выход, для счета введите целое число')
    ask_number = input('Введите целое число:\n')
    num_one = ask_number
    num_twice = ask_number * 2
    num_trinity = ask_number * 3
    print(num_one, num_twice, num_trinity)
    if ask_number == 'выход': break
    if ask_number.isdigit():
        print(int(num_one)+int(num_twice)+int(num_trinity))
    else:
        print('Ввведите целое число')
        continue



