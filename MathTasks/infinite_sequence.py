# Задача на бесконечную числовую последовательность:
#
#     Возьмём бесконечную цифровую последовательность, образованную склеиванием последовательных положительных
#  чисел: S = 123456789101112131415...
#     Определите первое вхождение заданной последовательности A в бесконечной последовательности S
# (нумерация начинается с 1).
#
#     Пример входных данных:
#     6789
#     111
#
#     Пример выходных данных:
#     6
#     12

# шаблон
# seq - str
# def find_sequence(seq):
#     #TODO
#     return 0


def place_in(n: int) -> int:
    """
    Вспомогательная функция вычисления порядкого номера по числу, которое образует последовательность.
    ...198199200... Аргумент: 199, значение: 487. Аргумент: 200, значение: 487+3=490 и т.д.
    :param n: число последовательности
    :return: положение в последовательности
    """
    n_len = len(str(n))
    place_out = 0
    for i in range(1, n_len):
        place_out += 9 * i * (10 ** (i - 1))
    place_out = place_out + n_len * (n - 10 ** (n_len - 1)) + 1
    return place_out


def find_sequence(seq: str) -> int:
    """
    Основная функция определения положения в бесконечной последовательности S = 123456789101112131415...
    :param seq: произвольный набор цифр от 0 до 9 включительно, в т.ч. нули в начале
    :return: положение искомой в заданной последовательности
    """
    if seq == '':
        return 0

    if int(seq) == 0:  # Если все нули
        return place_in(10 ** len(seq)) + 1
    zero_s = len(seq) - len(str(int(seq)))  # Кол-во нулей в начале числа

    # Создаём последовательность до n-значного числа
    n = 2  # Разряд разграничения
    if zero_s <= n:
        stop_1 = 10 ** (min(len(seq) + 1, n)) + len(seq) + 5
        # Создаём небольшой кусок последовательности, чтобы не возится с мелочью
        s = "".join([str(i) for i in range(1, stop_1)])
        res = s.find(seq) + 1
        if res > 0:
            return res

    n = max(n + 1, zero_s + 1)  # Начальный разряд числа
    res_list = []
    while not res_list:
        for i in range(zero_s, n):  # Не вышли за границы последовательности
            if seq[i] != '0':  # Число не может начитаться с нуля

                if i + n <= len(seq):  # В seq лежит число целиком
                    hyp = int(seq[i:(n + i)])
                    hyp_str = str(hyp - 1) + str(hyp)
                    j = 0

                    while len(hyp_str) <= len(seq) + n - i:
                        j += 1
                        hyp_str += str(hyp + j)

                    if hyp_str.find(seq) == (len(str(hyp - 1)) - i):
                        res_list.append(place_in(hyp) - i)

                else:  # В seq не лежит число целиком
                    temp = str(int(seq[0:i]) + 1)
                    hyp_1 = 'x' * (n - i)
                    if zero_s >= 1:
                        hyp_1 += '0' * (i - len(temp)) + temp
                    else:
                        hyp_1 += temp[len(temp) - i:len(temp)]
                    hyp_2 = seq[i:len(seq)] + 'x' * (n + i - len(seq))

                    if not any([hyp_1[j] != 'x' and hyp_2[j] != 'x' and hyp_1[j] != hyp_2[j] for j in range(n)]):
                        hyp_str = hyp_2[0:(n - i)] + hyp_1[(n - i):n]  # Сшиваем число
                        res_list.append(place_in(int(hyp_str)) - i)
        n += 1

    res = min(res_list)
    return res


print(find_sequence('956387183'))

# Проверка
zero_test = 0
finish = 10 ** 6
finish1 = 10 ** 4

# Создаём последовательность
s = ''.join([str(i) for i in range(1, finish + 2)])
# Проверка совпадений по двум методам
for i in range(1, finish1 + 1):
    if find_sequence('0' * zero_test + str(i)) - (s.index('0' * zero_test + str(i)) + 1) != 0:
        print(i)
        break
