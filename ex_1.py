list1 = [1,2,3]
list2 = [5,6,7]
list3 = [el for el in range(8,16)]
list4 = [el for el in range(16,25)]

class Matrix:
    def __init__(self,*args):
        self.args = args
        print(f'We got {args} list\'s of number for create a matrix!')

    def matrix(self):
        self.new_list = []
        for i in range(len(self.args)):
            for _ in self.args[i]:
                self.new_list.append(_)

        return self.new_list

    def __str__(self):
        self.string = ''
        for i in range(0,len(self.new_list)):
            if len(self.new_list[:(i+1)])%4==0 and i !=0:
                self.string = self.string +str(self.new_list[i])+'\n'

            else:
                self.string = self.string +str(self.new_list[i])+(' '*(7-(len(str(self.new_list[i])))))

        return self.string

    def __add__(self, other):

        self.add_matrix_list = []
        if len(self.new_list) > len(other.new_list):
            for i in range(len(self.new_list)):
                try:
                    self.el = self.new_list[i] + other.new_list[i]
                    self.add_matrix_list.append(self.el)

                except:
                    try:
                        self.el = self.new_list[i]
                        self.add_matrix_list.append(self.el)

                    except:
                        self.el = other.new_list[i]
                        self.add_matrix_list.append(self.el)
            return (Matrix(self.add_matrix_list))

        else:
            for i in range(len(other.new_list)):
                try:
                    self.el = self.new_list[i] + other.new_list[i]
                    self.add_matrix_list.append(self.el)

                except:
                    try:
                        self.el = self.new_list[i]
                        self.add_matrix_list.append(self.el)

                    except:
                        self.el = other.new_list[i]
                        self.add_matrix_list.append(self.el)

            return (Matrix(self.add_matrix_list))






ma = Matrix(list1,list2,list3,list4)
ma.matrix()
print(ma)
mb = Matrix(list1,list3)
mb.matrix()
print(mb)

mc = ma + mb
mc.matrix()
print(mc)