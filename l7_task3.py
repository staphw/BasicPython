# -*- coding: utf-8 -*-

# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. 
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). 
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно. 
# В методе деления должно осуществляться округление значения до целого числа.


class Cage():
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return Cage(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity - other.quantity > 0:
            return Cage(self.quantity - other.quantity)
        else:
            print("Error")

    def __mul__(self, other):
        return Cage(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cage(self.quantity // other.quantity)

    def __str__(self):
        return f'{self.quantity} {type(self)}'

    def make_order(self, cells):
        count = self.quantity
        string = ''
        while count > 0:
            string += '*' * cells + '\n' if count - cells > 0 else '*' * count
            count -= cells
        return string


def main():
    cage_1 = Cage(12)
    cage_2 = Cage(15)
    cage_3 = Cage(6)
    print(cage_1 + cage_2)
    print(cage_1 - cage_2)
    print(cage_1 - cage_3)
    print(cage_1 * cage_3)
    print(cage_2 / cage_3)
    print(cage_1.make_order(5))
    print(cage_2.make_order(5))

if __name__ == '__main__':
    main()