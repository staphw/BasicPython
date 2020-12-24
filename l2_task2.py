# -*- coding: utf-8 -*-

# Для списка реализовать обмен значений соседних элементов, 
# т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
# При нечетном количестве элементов последний сохранить на своем месте. 
# Для заполнения списка элементов необходимо использовать функцию input().

user_list = []

while True:
    user_input = input("Enter new element of list or press enter to exit: ")
    if user_input != "":
        user_list.append(user_input)
    else:
        break

reusut_list = user_list.copy()

for index, item in enumerate(reusut_list):
    if index % 2 != 0:
        reusut_list.insert(index - 1, item)
        reusut_list.pop(index + 1)

print(f'{user_list}\n{reusut_list}')