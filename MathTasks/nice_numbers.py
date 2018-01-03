# Задача замечательные числа:
# В некоторых числах можно найти последовательности цифр, которые в сумме дают 10.
# К примеру, в числе 3523014 целых четыре таких последовательности, обозначены'':
# '352'3014
# 3'523'014
# 3'5230'14
# 35'23014'
#
# Можно найти и такие замечательные числа, каждая цифра которых входит
# в по крайней мере одну такую последовательность.
# Например, 3523014 является замечательным числом,
# а 28546 — нет (в нём нет последовательности цифр, дающей в сумме 10 и при этом включающей 5).
#
# Найдите количество этих замечательных чисел в интервале [1, 9100000] (обе границы — включительно).

import timeit


def magic_check(number: int) -> bool:
    a = [0] + [int(l) for l in str(number)]
    # Проверка с конца (ускорение работы для больших чисел)
    b = a[-1] + a[-2]
    i = -3
    while b < 10 and len(a) + i >= 0:
        b += a[i]
        i -= 1
    if b != 10:
        return False

    for i in range(1, len(a)):
        a[i] += a[i - 1]
        # Проверка с начала (ускорение работы для больших чисел)
        if a[i] > 10 > a[i - 1]:
            return False
        elif a[i] == 10:
            max_i = i

    for i in range(1, len(a) - 2):
        if i > max_i:
            return False
        for j in range(i + 1, len(a)):
            if a[j] - a[i] > 10:
                break
            elif a[j] - a[i] == 10:
                max_i = j
    return True


def zam_chis(min_number=1, max_number=100):
    count = 0
    for i1 in range(min_number, max_number + 1):
        if magic_check(i1):
            count += 1
    print('Кол-во чисел:', count)
    print('Примерный порядок результата:', (max_number - min_number) // 11)
    print('Разница, раз:', round((max_number - min_number) / 11 / count, 2))
    return count


print("время выполнения, сек:", round(timeit.timeit('zam_chis(1,9100)', globals=globals(), number=1), 2))

'''
Результаты выполнения:

Интервал: [1, 9 100 000]
Кол-во чисел: 152 409
Время выполнения, сек: 147.37

Интервал: [1, 910 000]
Кол-во чисел: 22 722
Время выполнения, сек: 14.2

Интервал: [1, 91 000]
Кол-во чисел: 3 349
Время выполнения, сек: 3.52

Интервал: [1, 9 100]
Кол-во чисел: 488
Время выполнения, сек: 0.07
'''