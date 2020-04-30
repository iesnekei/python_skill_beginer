from abc import abstractmethod

class Cloth:
    mat = 0
    unit = 0
    def __init__(self,V=None,H=None):

        if V != None:
            Cloth.unit += 1
            Cloth.mat += V/6.5 + 0.5
        else:
            Cloth.mat += 2*H + 0.3
            Cloth.unit += 1
        self.V = V
        self.H = H
        print(f'We used {Cloth.mat:.2f} m2 of material for create {Cloth.unit} items')

    @abstractmethod
    def material(self):
        self.use_mat_1 = self.V/6.5 + 0.5
        return  self.use_mat_1

    @abstractmethod
    def material(self):
        self.use_mat_2 = 2 * self.H + 0.3
        return self.use_mat_2


class Suit(Cloth):
    @property
    def material(self):
        self.use_mat_1 = self.V/6.5 + 0.5
        print(f'To create {__class__.__name__} item we used {self.use_mat_1:.2f} m2 of material')

class Coat(Cloth):
    @property
    def material(self):
        self.use_mat_2 = 2 * self.H + 0.3
        print(f'To create {__class__.__name__} item we used {self.use_mat_2:.2f} m2 of material')


suit_1 = Suit(V=30)
suit_2 = Suit(V=40)
suit_3 = Suit(V=50)
coat_1 = Coat(H=30)
coat_2 = Coat(H=40)
coat_3 = Coat(H=50)


suit_1.material
suit_2.material
suit_3.material
coat_1.material
coat_2.material
coat_3.material