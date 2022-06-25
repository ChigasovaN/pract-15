'''
Практическая №15
Вариант №32
1. Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE.
'''
matrix = [[1, 3, -6],
          [-8, 19, 41],
          [23, 1, -6]]


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > 0:
            print('TRUE')
        else:
            print('FALSE')

        break
    break
