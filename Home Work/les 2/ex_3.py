while True:
    user_choose_month = input('Please write a number of month from 1 to 12: \n... ')
    if user_choose_month.isdigit():
        user_choose_month = int(user_choose_month)
        if 0 < user_choose_month <= 12:
            break
        else:
            print('Please input number from 1 to 12')
            continue

list_of_winter = [1,2,3]
list_of_spring = [4,5,6]
list_of_summer = [7,8,9]
list_of_autumn = [10,11,12]

if user_choose_month in list_of_winter:
    print('List method say : You chose winter month')
elif user_choose_month in list_of_spring:
    print('List method say : You chose spring month')
elif user_choose_month in list_of_summer:
    print('List method say : You chose summer month')
else:
    print('List method say : You chose autumn month')


time_of_year = {
                'list_of_winter':[1,2,3],
                'list_of_spring':[4,5,6],
                'list_of_summer':[7,8,9],
                'list_of_autumn':[10,11,12]
                }


if user_choose_month in time_of_year['list_of_winter']:
    print('Dict method say : You chose winter month')
elif user_choose_month in time_of_year['list_of_spring']:
    print('Dict method say : You chose spring month')
elif user_choose_month in time_of_year['list_of_summer']:
    print('Dict method say : You chose summer month')
else:
    print('Dict method say : You chose autumn month')
