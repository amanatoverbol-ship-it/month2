#Родительский класс
class Car:
    pass
#Функции внутри классов наз-ся методами
    def __init__(self, color, model):
        self.color = color
        self.model=model
    def test(self):
        pass
    def drive_to(self, destination):
        print(f'Model: {self.model}, Color: {self.color}, Destination: {destination}')
    def change_color(self, new_color):
        self.color = new_color
#Инициализация обьектов
car1 = Car('белый', 'Марк2')
car2=Car('черный','BMW')
print(car1)
print(type(car1))
print(car1.color, car1.model)
print(car2.color, car2.model)
car1.drive_to('Каракол')

class Bus(Car):
    pass
class Truck(Car):
    pass
car3=Car('черный','BMW')
car3.change_color('серый')
bus_42=Bus('зеленый',  ' Mercedes')
print(bus_42.color, bus_42.model)
bus_42.drive_to('Сокулук')