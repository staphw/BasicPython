# -*- coding: utf-8 -*-

# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def main():
    with open('l5_task5.txt', 'w', encoding='utf-8') as out_file:
        print(input('Введите числа, разделенные пробелом: '), file=out_file)
    sum_numbers = 0
    with open('l5_task5.txt', encoding='utf-8') as in_file:
        for num in in_file.read().split(' '):
            try:
                sum_numbers += float(num)
            except ValueError:
                continue
    print('Сумма чисел равна', sum_numbers)

if __name__ == '__main__':
    main()