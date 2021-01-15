# -*- coding: utf-8 -*-

# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. 
# Об окончании ввода данных свидетельствует пустая строка.

def main():
    f = open("l5_task1.txt", "w")
    while 1:
        user_string = input("Введите текст: ")
        if user_string == "":
            break
        print(user_string, file=f)

if __name__ == '__main__':
    main()