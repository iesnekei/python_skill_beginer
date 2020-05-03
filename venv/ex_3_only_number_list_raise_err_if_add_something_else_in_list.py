class NotNumberErr(Exception):
   print('It\'s not a number')




if __name__ == '__main__':
    list = []

    while True:
        a = input('For exit press exit. Else press a number:  ')
        if a.lower() == 'exit':
            break
        try:
            if a.isdigit() == False:
                raise NotNumberErr
        except NotNumberErr:
            print('Ups! Write a nubmer! Please!')
        else:
            a = int(a)
            list.append(a)
    print(list)







