# -*- coding: utf-8 -*-

# Реализовать формирование списка, используя функцию range() и возможности генератора. 
# В список должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

def multi(prev_item, item):
    return prev_item * item

my_list = [i for i in range(100, 1001) if i % 2 == 0]

print(reduce(multi, my_list))