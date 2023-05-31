def random_sort(arr):
    n = len(arr)
    # Проходим по всем элементам списка
    for i in range(n):
        # Последние i элементов уже отсортированы, поэтому мы можем их пропустить
        for j in range(0, n-i-1):
            # Если текущий элемент больше следующего, меняем их местами
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Генерируем список из 10 случайных чисел
import random
random_numbers = random.sample(range(0, 100), 10)

# Выводим неотсортированный список
print("Исходный список:", random_numbers)

# Сортируем список и выводим его
random_sort(random_numbers)
print("Отсортированный список:", random_numbers)
