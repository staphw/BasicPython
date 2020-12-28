# -*- coding: utf-8 -*-

# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: 
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. 
# Реализовать вывод данных о пользователе одной строкой.

def print_user_data(name, surname, birth_year, town, email, phone):
    return f"{name} {surname}, {birth_year}, {town}, {email}, {phone}"

user_data ={"name": "John", "surname": "Smith", "birth_year": 1991, "town": "Haarlem", "e-mail": "johnsmith@mail.com", "phone": "9876543210"}

print(print_user_data(phone=user_data["phone"], email=user_data["e-mail"], town=user_data["town"], birth_year=user_data["birth_year"], surname=user_data["surname"], name=user_data["name"]))