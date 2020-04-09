while True:

    print('Для выхода напишите выход, для счета введите целое число')

    user_sec = input('Напишите сколько секунд вы хотите перевести в формат чч:мм:сс :\n')

    if user_sec.lower() == 'выход':break

    if user_sec.isdigit():

        user_sec = int(user_sec)

        if user_sec < 60:
            print(f'00:00:{user_sec}')

        elif 60 <= user_sec < 3600:
            user_min = user_sec // 60
            user_sec = user_sec % 60
            print(f'00:{user_min:>02}:{user_sec:>02}')

        else:
            hour = user_sec // 3600
            minutes = (user_sec - hour * 3600) // 60
            user_sec = (user_sec - hour * 3600) % 60
            print(f'{hour:>02}:{minutes:>02}:{user_sec:>02}')

    else:
        print('Вы ввели не верный формат , введите количество секуннд в цифрах')