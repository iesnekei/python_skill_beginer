def salary(name,work_hours,price_for_hours,bonus):
    result = (work_hours*price_for_hours) + bonus
    print(f'{name} will get {result} CNY in this month.')

import ex_1_data

salary(
       (ex_1_data.worker_info['name'][1]),
       (ex_1_data.worker_info['work_hours'][1]),
       (ex_1_data.worker_info['price_for_hours'][1]),
       (ex_1_data.worker_info['bonus'][1]),
    )
