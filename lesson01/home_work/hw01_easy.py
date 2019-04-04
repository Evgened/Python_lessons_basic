__author__ = 'Евгений Шум'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

import random
v = str(random.randint(1,999))
print (v)
n = len (v)
i = 0
while i < n:
    print ( v[i] )
    i +=1

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

v1 = input('Введите первую переменную: ')
v2 = input('Введите вторую переменную: ')

v3 = v2
v2 = v1
v1 = v3

print(v1)
print(v2)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

v = int (input('Укажите ваш возраст: '))

if v >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом возможно только с 18 лет')