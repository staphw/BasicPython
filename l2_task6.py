# -*- coding: utf-8 -*-

# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. 
# Каждый кортеж хранит информацию об отдельном товаре. 
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). 
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. 
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а 
# значение — список значений-характеристик, например список названий товаров.

wares = []
product_info = {"name": "", "price": "", "quant": "", "units": ""}
number = 1

while True:
    choice = input("""
Menu:
1. New
2. Analysis
0. Exit
Select: """)

    if choice == '1':
        product_info['name'] = input("Enter the name of product: ")
        product_info['price'] = int(input("Enter the price of product: "))
        product_info['quant'] = int(input("Enter the quantity of product: "))
        product_info['units'] = input("Enter the units of measurement of product: ")
        wares.append((number, product_info.copy()))
        number += 1

    elif choice == '2':
        analysis_result = {"name": [], "price": [], "quant": [], "units": []}
        for item in wares:
            for key, value in item[1].items():
                analysis_result[key].append(value)
            analysis_result['units'] = list(set(analysis_result['units']))
        print(analysis_result)

    elif choice == '0':
        break

    else:
        print("Error! Incorrect selection.")
