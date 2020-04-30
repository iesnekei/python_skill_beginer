class Cell:
    def __init__(self,sections):
        self.sections = sections
        print(f'In laboratory we got cell with {self.sections} sections')

    def __add__(self, other):
        print(f'In this experiment we try to add section from one cell into another cell, in result we must get cell with section equal parents sec ')
        return Cell(self.sections + other.sections)

    def __sub__(self, other):
        print(f'In this experiment we try afflict one cell by another to destroy, in result we got cells will destroyed secitons.')
        return Cell(self.sections - other.sections)
    def __mul__(self, other):
        print(f'In this experiment we try multiply cells, in result we got  cell with multi sections.'
              )
        return Cell(self.sections*other.sections)

    def __truediv__(self, other):
        print(f'In this experiment we try slice cell sections by another cell sections, in result we must get a part of origin cell.'
              )
        return Cell(self.sections//other.sections)
    def make_order(self):
        self.string = ''
        for i in range(1,(self.sections+1)):
            if i%5==0:
                self.string = self.string +'*' + "\n"
            else:
                self.string = self.string +'*'
        print(self.string)







prototype_cell_1 = Cell(8)
prototype_cell_2 = Cell(12)
prototype_cell_3 = prototype_cell_1 + prototype_cell_2
prototype_cell_4 = prototype_cell_2 - prototype_cell_1
prototype_cell_5 = prototype_cell_2*prototype_cell_3
prototype_cell_6 = prototype_cell_5/prototype_cell_2

prototype_cell_1.make_order()
print('\n')
prototype_cell_2.make_order()
print('\n')
prototype_cell_3.make_order()
print('\n')
prototype_cell_4.make_order()
print('\n')
prototype_cell_5.make_order()
print('\n')
prototype_cell_6.make_order()



