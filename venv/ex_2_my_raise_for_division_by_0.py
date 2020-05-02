from time import sleep
class MyDivisonByZeroError(Exception):
        print('Stop wait a minute, in parallel galaxy is absolute normal! But for result we will wait info a light year! \n Please be patient and wait!')


i = 0
try:
    res = 100 / i
    if i == 0:
        raise MyDivisonByZeroError

except MyDivisonByZeroError:
    print('Ups, update you math skill!')

finally:
    for i in range(5):
        print(f'{4-i} sec')
        sleep(1)
    print('Ok. It\'s too long to wait let\'s give up and go take a coffee!')




