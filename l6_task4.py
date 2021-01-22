# -*- coding: utf-8 -*-

# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. 
# Для классов TownCar и WorkCar переопределите метод show_speed. 
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'{self.name} поехала')

    def stop(self):
        self.speed = 0
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость {self.name} {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print('Скорость {self.name} превышена, {self.speed}')
        else:
            super().show_speed()


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость {self.name} превышена, {self.speed}')
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


def main():
    town_car = TownCar(70, 'black', 'Lada')
    town_car.show_speed()
    town_car.turn('налево')
    print(town_car.name, town_car.color, town_car.speed, town_car.is_police)
    town_car.stop()
    town_car.show_speed()
    town_car.go(50)
    town_car.show_speed()

    sport_car = SportCar(100, 'white', 'Moscvich')
    sport_car.show_speed()
    sport_car.turn('направо')
    print(sport_car.name, sport_car.color, sport_car.speed, sport_car.is_police)
    sport_car.stop()
    sport_car.show_speed()
    sport_car.go(80)
    sport_car.show_speed()

    work_car = WorkCar(35, 'black', "Gazel'")
    work_car.show_speed()
    work_car.turn('налево')
    print(work_car.name, work_car.color, work_car.speed, work_car.is_police)
    work_car.stop()
    work_car.show_speed()
    work_car.go(50)
    work_car.show_speed()

    police_car = PoliceCar(80, 'blue-white', 'UAZ')
    police_car.show_speed()
    police_car.turn('направо')
    print(police_car.name, police_car.color, police_car.speed, police_car.is_police)
    police_car.stop()
    police_car.show_speed()
    police_car.go(90)
    police_car.show_speed()

if __name__ == '__main__':
    main()
