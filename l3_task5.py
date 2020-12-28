# -*- coding: utf-8 -*-

# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел. 
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. 
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. 
# Но если вместо числа вводится специальный символ, выполнение программы завершается. 
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def my_func(user_str):
    func_sum = 0
    for item in user_str.split():
        if 'q' in item:
            return func_sum, False
        try:
            func_sum += float(item)
        except ValueError:
            continue
    return func_sum, True

user_sum = 0
flag = True

while flag:
    num_sum, flag = my_func(input("Enter numbers separated by space or 'q' to exit: "))
    user_sum += num_sum
    print(f"Sum of numbers is {user_sum}")
