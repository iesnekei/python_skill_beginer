class Date:
    def __init__(self,dd_mm_yy:str):
        self.dd_mm_yy = dd_mm_yy

    @staticmethod
    def ddmmyy_as_numb(dd_mm_yy:str):
        #day,month,year must be separate bu '-' or '.' like everywhere in real life
        if '.' in dd_mm_yy:
            new_int_list = [int(i) for i in dd_mm_yy.split('.') if i.isdigit()]

        if '-' in dd_mm_yy:
            new_int_list = [int(i) for i in dd_mm_yy.split('-') if i.isdigit()]
            print(f'Day is {new_int_list[0]}, month is {new_int_list[1]}, year is {new_int_list[2]}.')


    @staticmethod
    def ddmmyy_validation(dd_mm_yy):
        if '.' in dd_mm_yy:
            new_int_list = [int(i) for i in dd_mm_yy.split('.') if i.isdigit()]

        if '-' in dd_mm_yy:
            new_int_list = [int(i) for i in dd_mm_yy.split('-') if i.isdigit()]
            print(f'Day is {new_int_list[0]}, month is {new_int_list[1]}, year is {new_int_list[2]}.')

        if type(dd_mm_yy) != str:
            print('You must write a string.')
            raise TypeError
        elif '.' not in dd_mm_yy and '-' not in dd_mm_yy:
            print('Please write down correct date separated by \'.\' or \'-\' .')
            raise TypeError

        elif len(new_int_list) < 3:
            print('Your data is short! Please write data in dd-mm-yy format')
            raise TypeError

        elif len(new_int_list) > 3:
            print('Your data is long! Please write data in dd-mm-yy format')
            raise TypeError


        else:
            print('Everything rigth with dd_mm_yy!')
            raise TypeError





if __name__ == '__main__':
    Date.ddmmyy_as_numb('02-5-2020')
    Date.ddmmyy_validation('22-05-3000')
    # Date.ddmmyy_validation(2205300)
    # Date.ddmmyy_validation('02052020')
    Date.ddmmyy_validation('01-03-03-04')