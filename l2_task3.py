# -*- coding: utf-8 -*-

# Пользователь вводит месяц в виде целого числа от 1 до 12. 
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
# Напишите решения через list и через dict.

seasons_list = ["", "winter", \
                    "winter", \
                    "spring", \
                    "spring", \
                    "spring", \
                    "summer", \
                    "summer", \
                    "summer", \
                    "autumn", \
                    "autumn", \
                    "autumn", \
                    "winter"]

seasons_dict = {"1": "winter", \
                "2": "winter", \
                "3": "spring", \
                "4": "spring", \
                "5": "spring", \
                "6": "summer", \
                "7": "summer", \
                "8": "summer", \
                "9": "autumn", \
                "10": "autumn", \
                "11": "autumn", \
                "12": "winter"}

user_num = input("Enter positive integer number from 1 to 12: ")

while True:
    try:
        print("Season from list is {}.\nSeason from dict is {}.".format(seasons_list[int(user_num)], seasons_dict[user_num]))
        break
    except ValueError:
        user_num = input("Error. You entered not positive integer number. Enter the number from 1 to 12: ")
    except LookupError:
        user_num = input("Error. The number must be from 1 to 12: ")