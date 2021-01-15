# -*- coding: utf-8 -*-

# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, 
# практических и лабораторных занятий по этому предмету и их количество. 
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

def main():
    with open('text_6.txt', encoding='utf-8') as in_file:
        lessons_dict = {line.split(" ")[0][:-1]: line.split(" ")[1:] for line in in_file.readlines()}
        print(lessons_dict)
    for key, value in lessons_dict.items():
        sum_hours = sum([int(num[:num.find('(')]) for num in value if num.find('(') != -1])
        lessons_dict[key] = sum_hours
    print(lessons_dict)

if __name__ == '__main__':
    main()
