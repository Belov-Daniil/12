# 4. Вычислить сумму знакопеременного ряда |(х * 2)^(3n)|/(3n)!, где х-матрица ранга к (к и матрица
# задаются случайным образом), n - номер слагаемого. Сумма считается вычисленной, если
# точность вычислений будет не меньше t знаков после запятой. У алгоритма д.б. линейная
# сложность. Знак первого слагаемого  -

import random
import numpy as np


# для упрощения поиска определителя матрицы использую библиотеку numpy
# создание матрицы ранга k
def make_matrix():
    # создание случайного к
    k = random.randint(2, 8)
    n = []
    for i in range(k):
        n.append([])
        for j in range(k):
            n[i].append(random.choice([-1, 1]))
    matrix = np.array(n)
    if abs(np.linalg.det(n)) == 0:
        return make_matrix()
    else:

        return matrix


# Функция факториала
def fuc(prev, n):
    for i in range(n):
        prev *= n
    return prev

# Функция вычисления суммы знакопеременного ряда
def Line(t):
    if t < 0:
        print('Введите положительное число')
        return
    # создание матрицы
    matrix = make_matrix()
    result = 0.0
    n = 1
    flag = True

    # цикл while работает пока в переменной result не будет t знаков после запятой
    while flag:
        try:
            # подсчет следующего значения знакопеременного ряда
            matrix = (matrix * 2) ** (3 * n)
            result += ((-1) ** n) * (abs(np.linalg.det(matrix)) / fuc(n, 3 * n))
            n += 1
            # проверка колличества знаков после запятой в переменной result
            if len(str(result).split('.')) >= 2:
                if len(str(result).split('.')[1]) > t:
                    flag = False
                elif str(result).find('e') != -1:
                    try:
                        flag = (len(str(result).split('.')[1]) + int(str(result).split('-')[1])) < t
                    except:
                        flag = (len(str(result).split('.')[1]) + int(str(result).split('+')[1])) < t
        except OverflowError:
            print('Числа в матрице привысили 2 147 483 647')
            print('Для повторного запуска напишите новое число :')
            return
    print('Суммa знакопеременного ряда |х^(3n)|/(3n)! :')
    print(result)
    print('Для повторного запуска напишите новое число, для выхода напишите "выход" :')
    return


# запуск программы
print('Введите кол-во знаков после запятой: ')
while True:
    try:
        inp = input()
        Line(int(inp))
    except ValueError:
        if inp == 'выход':
            exit()
        else:
            print('Введите чилсло')
