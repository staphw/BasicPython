# -*- coding: utf-8 -*-

# Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

var_1 = "Var 1"
var_2 = 2020

print("Varriable 1 - {}, Varriable 2 - {}".format(var_1, var_2))

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print("Hello, %s! Your age is %d" % (user_name, user_age))