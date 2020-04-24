# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен
# быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker():
    def __init__(self,name,surname,salary,position):
        self.name = name
        self.surname = surname
        self._salary = salary
        self.position = position

class Position(Worker):

    def get_full_name(self):
        print(f'Name: {self.name} \nSurname: {self.surname}\nPosition: {self.position}')

    def get_total_income(self):
        total_income = self._salary['wage'] + self._salary['bonus']
        print(total_income)


worker_1 = Position('kensei','smart',{'wage':1000,'bonus':100},'junior')
worker_1.get_full_name()
worker_1.get_total_income()

worker_2 = Position('Wolf','Martin',{'wage':99999,'bonus':66666},'middle')
worker_2.get_full_name()
worker_2.get_total_income()