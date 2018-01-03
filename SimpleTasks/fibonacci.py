# Задание:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fib_num(n):
    phi = (1 + 5 ** 0.5) / 2
    result = int((phi ** n - (-phi) ** (-n)) / (2 * phi - 1) + 0.5)
    return result


def fibonacci(n, m):
    fib = [fib_num(n), fib_num(n + 1)]
    for i in range(2, m - n + 2):
        fib.append(fib[i - 2] + fib[i - 1])
    if n > 1:
        fib.pop(0)
    return fib


print(fibonacci(1, 2))
print(fibonacci(2, 10))
print(fibonacci(9, 10))
print(fibonacci(20, 20))
