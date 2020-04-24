class Car():
    def __init__(self,speed,color,name,is_polise):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_polise

    def go(self):
        print('This car start go')

    def stop(self):
        print('Car were stoped.\n')

    def turn(self,direction):
        self.direction = direction
        print(f'Car was turned {direction}')

    def show_speed(self):
        print(f'Speed now is {self.speed} km/h')
        if self.speed > 80:
            print('Speed is too high! Please reduce your speed ! Your speed limit is 80 km/h!')


class TownCar(Car):
    def show_speed(self):
        print(f'Speed now is {self.speed} km/h')
        if self.speed > 60:
            print('Speed is too high! Please reduce your speed! Your speed limit is 60 km/h!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Speed now is {self.speed} km/h')
        if self.speed > 40:
            print('Speed is too high! Please reduce your speed! Your speed limit is 40 km/h!')


class PoliceCar(Car):
    pass

resident_car = TownCar(90,'white','Toyota Camry',False)
print(f'Resident car is {resident_car.name}')
print(f'Resident car color is {resident_car.color}')
print(f'Is it police car: {resident_car.is_polise}')
resident_car.go()
resident_car.show_speed()
resident_car.turn('left')
resident_car.stop()

sport_car = SportCar(100,'red',"Jaguar FX",False)
print(f'Sport car is {sport_car.name}')
print(f'Sport car color is {sport_car.color}')
print(f'Is it police car: {sport_car.is_polise}')
sport_car.go()
sport_car.show_speed()
sport_car.turn('right')
sport_car.stop()

work_car = WorkCar(50,'blue',"toyota Probox",False)
print(f'Work car is {work_car.name}')
print(f'Work car color is {work_car.color}')
print(f'Is it police car: {work_car.is_polise}')
work_car.go()
work_car.show_speed()
work_car.turn('around')
work_car.stop()

police_car = PoliceCar(240,'black',"Nissan Patrol",True)
print(f'Police car is {police_car.name}')
print(f'Police car color is {police_car.color}')
print(f'Is it police car: {police_car.is_polise}')
police_car.go()
police_car.show_speed()
police_car.turn('aside')
police_car.stop()