'''
Реализовать базовый класс Worker (работник).
● определить атрибуты: name, surname, position (должность), income (доход);
● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
● создать класс Position (должность) на базе класса Worker;
● в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
● проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
'''

class Worker:

    # метод класса
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus} #_income - защищенный
        print(f'{name} {surname}, {position}, оклад: {wage}, премия: {bonus}')


class Possition(Worker):

    # Метод получения полного имени сотруднка
    def get_full_name(self):
        return print(f'{self.name} {self.surname}')


    # Метод получения дохода с учётом премии
    def get_total_income(self):
        return print(f'Премия с окладом: {(self._income["wage"] + self._income["bonus"])}')

instance1 = Possition('Иван', 'Петров', 'инженер', 12000, 23000)
instance2 = Possition('Дмитрий', 'Сидоров', 'строитель', 10000, 30000)
instance1.get_full_name()
instance1.get_total_income()
instance2.get_full_name()
instance2.get_total_income()

