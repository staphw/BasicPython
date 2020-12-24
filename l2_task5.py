# -*- coding: utf-8 -*-

# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. 
# У пользователя необходимо запрашивать новый элемент рейтинга. 
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

rating_list = [7, 5, 3, 3, 2]
err_message = 'Error! You entered not positive integer number.'

while True:
    user_number = input("Enter positive integer number or press enter to exit: ")
    if user_number == "":
        break
    try:
        user_number = int(user_number)
        if user_number <= 0:
            print(err_message)
            continue
        if user_number in rating_list:
            index = len(rating_list) - rating_list[::-1].index(user_number)
            rating_list.insert(index, user_number)
        else:
            for index, item in enumerate(rating_list):
                if user_number > item:
                    rating_list.insert(index, user_number)
                    break
            if user_number not in rating_list:
                rating_list.append(user_number)
    except ValueError:
        print(err_message)

print(rating_list)