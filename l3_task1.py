# -*- coding: utf-8 -*-

# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error!"

first = float(input("Enter first number: "))
second = float(input("Enter second number: "))
print(division(first, second))
