﻿# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n,m):

    list_fib = []
    j = 0
    def n_fibonacci (x):
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            return n_fibonacci (x-1) + n_fibonacci (x-2)

    for i in range(n,m+1):
        j += 1;
        list_fib.append(n_fibonacci(i))

    return list_fib

# print (fibonacci(10,20))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    # пузырёк
    v_origin_list = list(origin_list)
    v_sort_list = []
    list_len = len(v_origin_list)
    v_min = float(0)
    v_min_pos = 0

    for i in range(list_len):
        v_min = v_origin_list[0]
        v_min_pos = 0
        for j in range(list_len - i):
            if v_origin_list[j] < v_min:
                v_min = v_origin_list[j]
                v_min_pos = j
        v_sort_list.append(v_origin_list.pop(v_min_pos))
    return v_sort_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter (cond, in_list):
    out_list = []
    n = 0

    for i in in_list:
        if cond(i):
            out_list.append(i)

    return (out_list)

v_list = [0,1,2,-4,-6,5]

print(v_list)
print(my_filter(lambda x: x>0, v_list))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
a1 = [1, 0]
a2 = [5, 0]
a3 = [7, 1]
a4 = [3, 1]
dots = [a1, a2, a3, a4]

# функция вычисления расстояния между точками
def dist (dot1, dot2):
    return ((dot1[0]-dot2[0])**2 + (dot1[1]-dot2[1])**2)**(1/2)

# получение списка расстояний между всеми четырьмя точками
dist_list = []
for i in range(4):
    i_next = i+1 if i<3 else 0
    dist_list.append(dist(dots[i], dots[i_next]))

# функция проверки на параллелограммность
def check_par (check_list):
    check_list.sort()
    if check_list[0]==check_list[1] and check_list[2]==check_list[3]:
        return "Parallelogramm"
    else:
        return "Not Parallelogramm"

print(dots)
print(dist_list)
print(check_par(dist_list))
