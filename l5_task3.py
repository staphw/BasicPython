# -*- coding: utf-8 -*-

# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
# Выполнить подсчет средней величины дохода сотрудников.

def main():
    with open("text_3.txt", encoding='utf-8') as f:
        personal_dict = {item.split(" ")[0]: float(item.split(" ")[1]) for item in f.readlines()}
    personal_less_dict = {key: value for key, value in personal_dict.items() if value < 20000}
    print("Сотрудники с окладом менее 20000: {}".format(", ".join(sorted(personal_less_dict.keys()))))
    print("Средняя величина дохода сотрудников: {:.2f}".format(sum(personal_dict.values())/len(personal_dict)))

if __name__ == '__main__':
    main()