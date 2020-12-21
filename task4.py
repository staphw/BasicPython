# -*- coding: utf-8 -*-

# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

user_number = int(input("Enter number: "))
max_number = 0

while user_number != 0:
    if max_number < user_number % 10:
        max_number = user_number % 10
    user_number //= 10

print(f"Max number is {max_number}")