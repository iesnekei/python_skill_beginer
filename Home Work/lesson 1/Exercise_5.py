def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


while True:

    income = input('Запишите значение выручки в этом месяце: ')

    if income.isdigit() or isfloat(income):
        income = int(income)

    else:
        print('Введите значение выручки в цифрах.')
        continue

    outcome = input('Запишите значение издержек в этом месяце: ')

    if outcome.isdigit() or isfloat(outcome):
        outcome = int(outcome)

    else:
        print('Введите значение выручки в цифрах.')
        continue

    current = input('В какой валюте вы ведете бизнес: ')

    profit = income - outcome

    if profit >= 0:
        profitability = (profit / income) * 100
        print(f'Прибыль вашего бизнеса {profit} {current}, рентабельность {profitability:.2f} % .')
        break

    else:
        print(f'У вас убыток {profit} {current}.')
        break


workers = input('Сколько у вас работников :')

while True:

    if workers.isdigit():

        workers = int(workers)

        if profit >= 0:
            print(f'Ваша прибыль {(profit / workers):.2f} {current}на работника.')
            break

        else:
            print(f'Вашу убыток {(profit / workers):.2f} {current} на работника.')
            break
    else:
        print('Количесвто работников должно быть записанно в цифрах.')