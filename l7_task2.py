# -*- coding: utf-8 -*-

# Реализовать проект расчета суммарного расхода ткани на производство одежды. 
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. 
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). 
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, 
# проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric_expense(self):
        pass

    def __add__(self, other):
        return self.fabric_expense + other.fabric_expense

class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def fabric_expense(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def fabric_expense(self):
        return 2 * self.height + 0.3


def main():
    coat = Coat(52)
    print(coat.fabric_expense)
    suit = Suit(2)
    print(suit.fabric_expense)
    print(suit + coat)

if __name__ == '__main__':
    main()