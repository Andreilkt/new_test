
def sum_list(n):
    # Инициализируем переменную суммы
    sum = 0
    # Проходим от 1 до n включительно и добавляем каждое число к сумме
    for i in range(1, n+1):
        sum += i
    # Возвращаем сумму
    return sum

# Пример и
n = 10
sum_numbers = sum_list(n)
print("Сумма чисел от 1 до", n, "равна", sum_numbers)