import random


# Реализуем алгорит "быстрой сортировки"
def sort_to_max(origin_list: list) -> list:
    if len(origin_list) <= 1:
        return origin_list
    choice = random.choice(origin_list)
    left, right, eq = [], [], []
    for elem in origin_list:
        if elem < choice:
            left.append(elem)
        elif elem > choice:
            right.append(elem)
        else:
            eq.append(elem)
    return sort_to_max(left) + eq + sort_to_max(right)


list_to_sort = [random.randint(-100, 100) for i in range(30)]
list_default = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]

print(list_to_sort)
print(sort_to_max(list_to_sort))
print(list_default)
print(sort_to_max(list_default))
