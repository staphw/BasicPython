# -*- coding: utf-8 -*-

# Создать текстовый файл (не программно), сохранить в нем несколько строк, 
# выполнить подсчет количества строк, количества слов в каждой строке.

def main():
    with open("l5_task1.txt") as f:
        str_from_file = f.readlines()
    print("Количество строк в файле: ", len(str_from_file))
    for index, item in enumerate(str_from_file, 1):
        print("В строке {}: {} слов.".format(index, len(item.split(" "))))

if __name__ == '__main__':
    main()