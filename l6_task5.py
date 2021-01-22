# -*- coding: utf-8 -*-

# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка). 
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение. 
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title}. Запуск отрисовки. {type(self)}.')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title}. Запуск отрисовки. {type(self)}.')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title}. Запуск отрисовки. {type(self)}.')


def main():
    stat = Stationery('Parent')
    stat.draw()
    pen = Pen('Ручка')
    pen.draw()
    pencil = Pencil('Карандаш')
    pencil.draw()
    handle = Handle('Маркер')
    handle.draw()

if __name__ == '__main__':
    main()
