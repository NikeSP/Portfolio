# Задача о 8-ми ферзях:
# Расставить на стандартной 64-клеточной шахматной доске 8 ферзей так,
# чтобы ни один из них не находился под боем другого»
# Вывести все варианты
import itertools

main_list = []
# В начале создаём список клеток - вся доска, куда мы можем поставить ферзя:
place_start = list(itertools.product([1, 2, 3, 4, 5, 6, 7, 8], repeat=2))


def list_queen(queen_list=list(), place_list=place_start):
    global main_list
    if len(queen_list) == 8:
        main_list.append(queen_list[:])
        return True
    elif not place_list:
        return False
    x_act = len(queen_list) + 1
    for y in range(1, 9):
        if (x_act, y) in place_list:
            new_place_list = []
            for (xp, yp) in place_list:
                # Проверка клеток: верт, гориз, 1ая и 2ая диагональ
                if xp != x_act and yp != y and abs(x_act - xp) != abs(y - yp):
                    new_place_list.append((xp, yp))
            list_queen(queen_list[:] + [(x_act, y)], new_place_list)
    return main_list


result = list_queen()
for el in result:
    print([' ABCDEFGH'[x] + str(y) for (x, y) in el])
print('Кол-во решений:', len(result))
