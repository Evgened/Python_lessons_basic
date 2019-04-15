﻿# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

list1 = [1,2,4,0]
list2 = [i**2 for i in list1]
print(list2)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits1=['яблоко','груша','абрикос', 'ананас']
fruits2=['персик','банан','вишня', 'груша', 'яблоко', 'чернослив', 'ананас']
fruits3=[]
#
# for i in fruits1:
#     if i in fruits2:
#         fruits3.append(i)

[fruits3.append(i) for i in fruits1 if i in fruits2]
print(fruits3)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random

randlist = [random.randint(-999,999) for i in range(20)]
resultlist = [r for r in randlist if (r%3==0 and r > 0 and r%4!=4)]
# resultlist = [r for r in [random.randint(-999,999) for i in range(20)] if (r%3==0 and r > 0 and r%4!=4)]
print(randlist)
print(resultlist)
