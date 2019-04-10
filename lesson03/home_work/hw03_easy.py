# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    power = 10**ndigits
    rest = (number * power % 1) / power
    trunc_num = number - rest
    if rest * power < 0.5:
        return number - rest
    else:
        return trunc_num + 1/power


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print(my_round(2.0000047, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    v_ticket=list(str(ticket_number))
    v_len=len(v_ticket)
    v_left_side=0
    v_right_side=0
    if v_len==6:
        for i in range(6):
            if i <= 3:
                v_left_side += int(v_ticket[i])
            else:
                v_right_side += int(v_ticket[i])
        if v_left_side == v_right_side:
            return 'Yes'
        else:
            return 'No'
    else:
        return 'No'


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
