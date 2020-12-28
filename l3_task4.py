# -*- coding: utf-8 -*-

# Программа принимает действительное положительное число x и целое отрицательное число y. 
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). 
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. 
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

pow_math = lambda x, y: x ** y

def pow_cycle(x, y):
    result = 1
    for _ in range(0, abs(y)):
        result *= x
    return 1 / result    

message = "Incorrect input."

try:
    first = float(input("Enter real positive number: "))
    second = int(input("Enter integer negative number: "))
    if first <= 0 or second >= 0:
        raise ValueError
    else:
        print(pow_math(first, second))
        print(pow_cycle(first, second))
except ValueError:
    print(message)
