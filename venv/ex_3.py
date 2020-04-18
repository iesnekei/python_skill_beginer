with open('salary_of_worker.txt') as data_of_worker:
    all_salary_for_pay = 0
    employee_numb = []
    for employee in data_of_worker:
        a = employee.split()
        employee_numb.append(a[0])
        all_salary_for_pay += int(a[1])
        if int(a[1]) < 20000:
            print(f'{a[0]} has a salary under 20000 USD.')
    average_salary = all_salary_for_pay / len(employee_numb)
    print(f'\nAverage salary for employee is {average_salary}')