# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import os, json
workers_path = os.path.join('c:\GitRepo\Python_GeekBrain\lesson03\home_work\data', 'workers')
hours_path = os.path.join('c:\GitRepo\Python_GeekBrain\lesson03\home_work\data', 'hours_of')

list_workers = []
list_hours = []
n = 0
with open(workers_path, 'r', encoding='UTF-8') as f:
    for line in f.readlines():
        if n > 0:
            list_workers.append(line.split())
        n +=1
n = 0
with open(hours_path, 'r', encoding='UTF-8') as f:
    for line in f.readlines():
        if n > 0:
            list_hours.append(line.split())
        n +=1

total_hours = 0
worker_salary = []

def get_worker_salary (list_workers, name, surname):
    for i in list_workers:
        if i[0] == name and i[1] == surname:
            return i
topay = float(0)
for i in list_hours:

    w_salary = get_worker_salary (list_workers, i[0], i[1])

    if int(i[2]) < int(w_salary[4]):
        print ('Отработал меньше нормы: ', i[1], '. Отработано: ', i[2], ', норма: ', w_salary[4])
        topay =  round(int(w_salary[2]) * int(i[2]) / int(w_salary[4]),2)
        print('Выплатить: ', topay)
    else:
        print ('Отработал не меньше нормы: ', i[1], '. Отработано: ', i[2], ', норма: ', w_salary[4])
        topay = round(int(w_salary[2]) + 2 * int(w_salary[2]) * ( int(i[2]) - int(w_salary[4])) / int (w_salary[4]),2)
        print ('Выплатить: ', topay)
    # worker_salary.append( list((list_workers[i][0], list_workers[i][1], list_hours[i][2])) )

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
