class OfficeStaff:
    printer_count = 0
    table_count = 0
    all_staff = {}
    def __init__(self,name,model,year,cost):
        self.name = name
        self.model = model
        self.year = year
        self.cost = cost


    def what_is_it(self):
        print(f'It\'s {self.name} model {self.model} buy in {self.year} cost {self.cost}')

class Printer(OfficeStaff):
    OfficeStaff.printer_count += 1
    hand_off = ['Don\'t touch when it work','Don\'t put in water']

    def __str__(self):
        return f'It\'s a printer {self.name} model {self.model} buy in {self.year} cost {self.cost} usd'

    def where_use_it(self):
        if self.year > 2019:
            return  'It\'s new we will give it to executive manager!'
        elif 2019 > self.year > 2010:
            return 'Give it to office worker!'
        else:
            return 'It\'s too old, put in in storehouse'

    def get_to_storehouse(self):
        OfficeStaff.all_staff['printer'] = self.name



class Table(OfficeStaff):
    OfficeStaff.table_count +=1
    tabels_by_m2 = []
    def __str__(self):
        return f'It\'s a table {self.name}, model {self.model} cm, buy in {self.year}, cost {self.cost} usd'
    def square(self,width,lenth):
        Table.tabels_by_m2.append(width*lenth/1000)
        return width * lenth / 1000

    def get_to_storehouse(self):
        OfficeStaff.all_staff['table'] = self.name



if __name__ == '__main__':

    a = Printer('Brother','XWD2000',2015,2000)
    b = Table('Simple',"Ikea 90*60",2019,400)
    b.square(90,60)
    a.get_to_storehouse()
    b.get_to_storehouse()
    print(a)
    print(a.hand_off)
    print(a.where_use_it())
    print(a.printer_count)
    print(b)
    print(b.tabels_by_m2)
    print(b.table_count)
    print(OfficeStaff.all_staff)