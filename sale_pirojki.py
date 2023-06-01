"""Скрипт рассчитывает стоимость пирожков, в зависимости от их количества """

def sale_pirojki(n):
    price = 0
    sum = 0

    if n < 5:
        price = 100
    elif n >= 5 and n < 10:
        price = 95
    elif n >= 10:
        price = 90

    else:
        print("Такое количество продать не можем")

    sum = price * n
    return sum

quantity = int(input("Сколько желаете пирожков:"))
total_cost = sale_pirojki(quantity)
print(total_cost)


