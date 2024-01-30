# Вычислить сумму знакопеременного ряда |(х * 2)^(3n)|/(3n)!, где х-матрица ранга к
# (к и матрица задаются случайным образом), n - номер слагаемого.
# Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после запятой.
# У алгоритма д.б. линейная сложность

import random
import numpy as np
from decimal import Decimal, getcontext


# Функция вычисляющая сумму ряда
def sum_series():
    # Переменные для вычислений
    n = 1
    summa = 0
    matrix = (x * 2) ** 3
    fact = 6
    sign = 1

    while True:
        # Вычисляем текущий члена ряда и складываем с предыдущими членами
        row = Decimal(np.linalg.det(matrix)/fact)
        summa += sign * row

        # Проверка необходимой точности вычислений
        if abs(row) < 1 / (10 ** t):
            break

        # Считаем переменные для следующего члена ряда
        n += 1
        fact *= (3 * n) * (3 * n)
        matrix *= x * 2
        sign = -sign

    return summa


try:
    # Считываем значение точности вычислений
    t = int(input("Введите число t\nt - количество знаков после запятой:\n"))
    while t > 300 or t < 1:
        t = int(input("Введите число знаков после запятой\n"))
except ValueError:
    print("Вы ввели символ, а не число, перезапустите программу и попробуйте снова\n")

# Создаем матрицу со значениями от -1 до 1 и случайно созданным рангом k
k = random.randint(2, 10)
x = np.round(np.random.uniform(-1, 1, (k, k)), 3)

# Вывод матрицы
print(f"Сгенерированная матрица:\n{x}")

# Значение точности для Decimal
getcontext().prec = t + 100

# Выводим сумму ряда
print(f"Сумма знакопеременного ряда с точностью {t} знаков после запятой: {sum_series():.{t}f}")
