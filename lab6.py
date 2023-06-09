# Дана квадратная матрица. Сформировать все возможные варианты данной матрицы путем
# перестановки строк и столбцов, в которых диагональный элемент равен нулю.


import random
import copy


def number_check(n):
    while True:
        try:
            k = int(input(n))
            if k > 0:
                return k
            else:
                print('Введенное число отрицательное.')

        except ValueError:
            print('Введенное значение не является числом.')


def print_matrix(matrix):
    print()
    for row in matrix:
        for elem in row:
            print('{:4}'.format(elem), end=' ')
        print()
    print()


def F_rec(matrix, row, column, count, n, exist=[[], []]):
    if row == len(matrix):
        return
    F_rec(copy.deepcopy(matrix), row + 1, column + 1, count, n)

    if matrix[row][row] == 0 and row not in exist[0]:
        exist[0].append(row)
        new_matrix = copy.deepcopy(matrix)
        for i in range(len(matrix)):
            new_matrix[row][i], new_matrix[i][column] = new_matrix[i][column], new_matrix[row][i]
        print_matrix(new_matrix)
        count[0] += 1
    if matrix[row][n - row] == 0 and row != len(matrix) // 2 and row not in exist[1]:
        exist[1].append(row)
        new_matrix = copy.deepcopy(matrix)
        for i in range(len(matrix)):
            new_matrix[row][i], new_matrix[n - i][n - column] = new_matrix[n - i][n - column],  new_matrix[row][i]
        print_matrix(new_matrix)
        count[0] += 1
    F_rec(matrix, row + 1, column + 1, count, n, exist)


def F_iter(matrix):
    count = 0
    exist=[[], []]
    stack = [(copy.deepcopy(matrix), 0, 0)]
    k = n - 1
    while stack:
        matrix, row, column = stack.pop()
        if row == len(matrix):
            count += 1
            continue
        stack.append((copy.deepcopy(matrix), row + 1, column + 1))

        if matrix[row][row] == 0 and row not in exist[0]:
            exist[0].append(row)
            new_matrix = copy.deepcopy(matrix)
            for i in range(len(matrix)):
                new_matrix[row][i], new_matrix[i][column] = new_matrix[i][column], new_matrix[row][i]
            print_matrix(new_matrix)
            stack.append((matrix, row + 1, column + 1))
        if matrix[row][k - row] == 0 and row != len(matrix) // 2 and row not in exist[1]:
            exist[1].append(row)
            new_matrix = copy.deepcopy(matrix)
            for i in range(len(matrix)):
                new_matrix[row][i], new_matrix[k - i][k - column] = new_matrix[k - i][k - column],  new_matrix[row][i]
            print_matrix(new_matrix)
            stack.append((matrix, row + 1, column + 1))
    print('Общее количество вариантов: ', count - 1)


count = [0]
n = number_check('Размер матрицы: ')
array = [[random.randint(0, 5) for i in range(n)] for j in range(n)]
print('Начальная матрица:')
print_matrix(array)

print('Рекурсивный перебор возможных вариантов.')
F_rec(array, 0, 0, count, n - 1)
print('Общее количество вариантов: ', count[0])

print('Итеративный перебор возможных вариантов.')
F_iter(array)


cr = count[0]-1
if cr == 0:
    print('Проверяемый массив не подошел под условия.')