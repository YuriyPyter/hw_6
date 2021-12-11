'''
Реализуйте базовый класс Car.
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
'''

class Car:
    # методы класса:
    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police


    def go(self):
        print(f'{self.name}: старт')


    def stop(self):
        print(f'{self.name}: стоп')


    def turn(self):
        print(f'{self.name}: поворот')


    def show_speed(self):
        print(f'Текущая скорость {self.name}: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name}: превысила скорость!')
        else:
            print(f'Скорость {self.name} допустимая.')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name}: превысила скорость!')
        else:
            print(f'Скорость {self.name} допустимая.')


class PoliceCar(Car):
    pass


bmw = TownCar('BMW', 200, 'Чёрная', False)
bmw.go(), bmw.show_speed(), bmw.turn(), bmw.stop()
tayota = SportCar('TAYOTA', 150, 'Синяя', False)
tayota.go(), tayota.show_speed(), tayota.turn(), tayota.stop()
kamaz = WorkCar('КАМАЗ', 30, 'Белый', False)
kamaz.go(), kamaz.show_speed(), kamaz.turn(), kamaz.stop()
vaz = PoliceCar('ВАЗ', 60, 'Жёлтый', True)
vaz.go(), vaz.show_speed(), vaz.turn(), vaz.stop()





