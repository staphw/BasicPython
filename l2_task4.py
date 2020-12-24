# -*- coding: utf-8 -*-

# Пользователь вводит строку из нескольких слов, разделённых пробелами. 
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать. 
# Если в слово длинное, выводить только первые 10 букв в слове.

user_str = input("Enter the string: ")

for index, item in enumerate(user_str.split(" ")):
    print("{}. {}".format(index + 1, item if len(item) < 10 else item[:10]))