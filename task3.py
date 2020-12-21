# -*- coding: utf-8 -*-

# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_number = input("Enter number: ")
sum_numbers = 0
counter = 1

while counter <= int(user_number):
    sum_numbers += int(counter * user_number)
    counter += 1

print("Sum of numbers is", sum_numbers)