# -*- coding: utf-8 -*-

# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    return sum((a, b, c)) - min((a, b, c))
    
print(my_func(9, 7, 8))
print(my_func(5, 6, 5))