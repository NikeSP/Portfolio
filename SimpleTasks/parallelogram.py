# Задача:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

import itertools


def test_parall(x_A: list, y_A: list):
    # Проверку производим из условия равенства противоположных сторон
    permut = list(itertools.permutations((2, 3, 4), 3))
    print('Комбинации вершин:\n', permut)
    for comb in permut:
        x = [None, x_A[1]] + [x_A[el] for el in comb]
        y = [None, y_A[1]] + [y_A[el] for el in comb]
        if (x[1] - x[2]) ** 2 + (y[1] - y[2]) ** 2 == (x[3] - x[4]) ** 2 + (y[3] - y[4]) ** 2 and \
                (x[1] - x[4]) ** 2 + (y[1] - y[4]) ** 2 == (x[3] - x[2]) ** 2 + (y[3] - y[2]) ** 2:
            return True
    return False


x_A = [None, 2, 1, 6, 5]
y_A = [None, 3, 1, 3, 1]
print(test_parall(x_A, y_A))
