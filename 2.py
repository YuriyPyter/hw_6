'''
Реализовать класс Road (дорога).
● определить атрибуты: length (длина), width (ширина);
● значения атрибутов должны передаваться при создании экземпляра класса;
● атрибуты сделать защищёнными;
● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
дороги асфальтом, толщиной в 1 см*число см толщины полотна;
● проверить работу метода
'''

class Road:

    # метод класса
    def __init__(self, length, width):
        self.lehgth = length
        self.width = width
        self.weight = 25
        self.thickness = 5
        print(f'Масса асфальта для покрытия {self.thickness} см полотна: {int(length * width * self.weight * self.thickness /1000)} т.')

weight_asfalt = Road(20, 5000)











