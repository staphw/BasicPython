# -*- coding: utf-8 -*-

# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), 
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). 
# Результатом сложения должна быть новая матрица.


class Matrix:
    def __init__(self, m):
        self.matrix = m

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, string)) for string in self.matrix])

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError('Нельзя складывать матрицы разных размеров!')
        result = []
        for i in range(len(self.matrix)):
            tmp = []
            for j in range(len(self.matrix[0])):
                tmp.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(list(tmp))
        return Matrix(result)


def main():
    matrix1 = Matrix([[2, 3, 4], [3, 2, 1]])
    print(matrix1, '\n')
    matrix2 = Matrix([[5, 5, 5], [5, 5, 5]])
    matrix3 = Matrix([[5, 5, 5, 5], [5, 5, 5, 5]])
    print(matrix2, '\n')
    print(matrix1 + matrix2)
    try:
        print(matrix2 + matrix3)
    except ValueError as ex:
        print(ex)

if __name__ == '__main__':
    main()
