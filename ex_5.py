class Stationery():
    title = None
    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print('I have a PEN ! ')
class Pencil(Stationery):
    def draw(self):
        print('I have a PENCIL ! ')
class Handle(Stationery):
    def draw(self):
        print('Wooooo PENCILPEN !')

obj_pen = Pen()
obj_pencil = Pencil()
obj_handle = Handle()

obj_pen.draw()
obj_pencil.draw()
obj_handle.draw()