# Задача 18: Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 1 2 6 4 9
# Ввод: 8
# -> 9

import random
n = int(input('Input a count of numbers: '))
x = int(input('Input your x for searching : '))
arr = []

for i in range(n):
    a = int(input('Input the number: '))
    arr[i].append(a) #start, stop, wight
print(arr)