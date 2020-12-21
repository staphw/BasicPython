# -*- coding: utf-8 -*-

# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. 
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. 
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров. 
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

first_res = float(input("Enter first result: "))
final_res = float(input("Enter final result: "))
progress_in_percent = 10
progress = (100 + progress_in_percent) / 100
days = 1

while first_res < final_res:
    days += 1
    first_res *= progress

print(f"On day {days} the athlete reached the final result.")
