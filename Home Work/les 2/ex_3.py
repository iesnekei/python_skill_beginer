while True:
    user_choose_month = input('Please write a number of month from 1 to 12: \n... ')
    if user_choose_month.isdigit():
        user_choose_month = int(user_choose_month)
        if 0 < user_choose_month <= 12:
            break
        else:
            print('Please input number from 1 to 12')
            continue

list_of_winter = [12,1,2]
list_of_spring = [3,4,5]
list_of_summer = [6,7,8]
list_of_autumn = [9,10,11]

if user_choose_month in list_of_winter:
    print('List method say : You chose winter month')
elif user_choose_month in list_of_spring:
    print('List method say : You chose spring month')
elif user_choose_month in list_of_summer:
    print('List method say : You chose summer month')
else:
    print('List method say : You chose autumn month')


time_of_year = {
                'list_of_winter':[12,1,2],
                'list_of_spring':[3,4,5],
                'list_of_summer':[6,7,8],
                'list_of_autumn':[9,10,11]
                }


if user_choose_month in time_of_year['list_of_winter']:
    print('Dict method say : You chose winter month')
elif user_choose_month in time_of_year['list_of_spring']:
    print('Dict method say : You chose spring month')
elif user_choose_month in time_of_year['list_of_summer']:
    print('Dict method say : You chose summer month')
else:
    print('Dict method say : You chose autumn month')
