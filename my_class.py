class Dog():
    """Simply model of dog"""
    def __init__(self,name,age):
        """Иницилизируем атрибуты. создаем имя и возраст"""
        self.name = name
        self.age = age
        print('Dog has been created')

    def sit(self):
        """Собака будет содиться по команде"""
        print(self.name.title() + " собака села")

    def jump(self):
        """Собака будет прыгать по команде"""
        print(self.name.title() + " собака прыгнула")


my_dog = Dog('Bobi',1)

my_dog_2 = Dog('Jass',4)

print(my_dog.name)
print(my_dog_2.name)

my_dog.jump()
