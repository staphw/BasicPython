# -*- coding: utf-8 -*-

# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
# При этом английские числительные должны заменяться на русские. 
# Новый блок строк должен записываться в новый текстовый файл.

numbers_dict = {'One': 'Один',\
                'Two': 'Два',\
                'Three': 'Три',\
                'Four': 'Четыре'}

def main():
    global numbers_dict
    out_file = open('l5_task4.txt', 'w', encoding='utf-8')
    with open ('text_4.txt', encoding='utf-8') as in_file:
        for line in in_file.readlines():
            out_line = line.split(' ')
            out_file.write('{0} {1}'.format(numbers_dict[out_line[0]], ' '.join(out_line[1:])))
    out_file.close()

if __name__ == '__main__':
    main()