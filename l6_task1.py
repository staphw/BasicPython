# -*- coding: utf-8 -*-

# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). 
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. 
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. 
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). 
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.


import time


class TrafficLight:
    __color = ('Red', 'Yellow', 'Green')
    delay_time = (7, 2, 3)

    def running(self):
        count = 0
        while count < 2:
            for i, _ in enumerate(self.__color):
                if self.__color[i] == 'Red' and self.__color[i - 1] == 'Green':
                    print(self.__color[i])
                elif self.__color[i] == 'Yellow' and self.__color[i - 1] == 'Red':
                    print(self.__color[i])
                elif self.__color[i] == 'Green' and self.__color[i - 1] == 'Yellow':
                    print(self.__color[i])
                else:
                    print('Incorrect colors.')
                    count = 2
                    break
                time.sleep(self.delay_time[i])

            count += 1

    def change_color(self, color):
        self.__color = color


def main():
    tl = TrafficLight()
    tl.running()
    tl.change_color(('Yellow', 'Red', 'Green'))
    tl.running()

if __name__ == '__main__':
    main()
