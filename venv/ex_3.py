with open('salary_of_worker.txt') as data_of_worker:
    all_salary_for_pay = 0
    employee_numb = []

    for employee in data_of_worker:
        try:
            a = employee.split()
            employee_numb.append(a[0])
            all_salary_for_pay += int(a[1])

            if int(a[1]) < 20000:
                print(f'{a[0]} has a salary under 20000 USD.')


        except ValueError:
            print('Wrong data type in file!Please check it out!')
            break

    try:
        average_salary = all_salary_for_pay / len(employee_numb)
    except ZeroDivisionError:
        print("You don't have any employee.")
    print(f'\nAverage salary for employee is {average_salary}')

