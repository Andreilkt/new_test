""" Генерация списка случайных чисер и сортировка этого списка"""

def random_sort(for_list):
    n = len(for_list)
    # Проходим по всем элементам списка
    for i in range(n):
        for j in range(0, n-i-1):
            # Если текущий элемент больше следующего, меняем их местами
            if for_list[j] > for_list[j+1]:
                for_list[j], for_list[j+1] = for_list[j+1], for_list[j]

# Генерируем список из 10 случайных чисел
import random
random_list = random.sample(range(0, 99), 7)

# До сортировки
print("Cписок до сортировки:", random_list)

# После сортировки
random_sort(random_list)
print("Список после сортировки:", random_list)
