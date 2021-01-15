# -*- coding: utf-8 -*-

# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

import json

def main():
    sub_func = lambda x, y: x - y
    with open('text_7.txt', encoding='utf-8') as in_file:
        firms_dict = {line.split(" ")[0]: sub_func(int(line.split(" ")[2]), int(line.split(" ")[3])) for line in in_file.readlines()}
    profit = [value for value in firms_dict.values() if value > 0]
    with open('l5_task7.json', 'w', encoding='utf-8') as out_file:
        json.dump([firms_dict, {'average_profit': sum(profit) / len(profit)}], out_file, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    main()