a = 2
b = 3

i = 1

while b > a:
    if i == 1:
        print(f'{i}-й день : {a:.2f}')
        i += 1
    else:
        a *= 1.1
        print(f'{i}-й день : {a:.2f}')
        i += 1

print(f'Ответ: на {i-1}-й день спортсмен достиг результата -не менее {b} км')