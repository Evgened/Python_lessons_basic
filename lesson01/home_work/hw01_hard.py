__author__ = 'Евгений Шум'

# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True

# Вопрос: Чему была равна переменная a,
# если точно известно, что её значение не изменялось?

# Подсказка: это значение точно есть ;)

# Гуглил.. Надеюсь, не дичь.

class AltMath:
    def __init__(self, x):
        self.x = x
    def __gt__ (self, other):
        return self.x <= other
    def __eq__(self, other):
        return self.x == other
    def __mul__(self, other):
        return self.x * other
    def __pow__(self, other):
        return self.x ** other

a = AltMath(0)

print ('a == a**2: ', a == a**2)
print ('a == a*2', a == a*2)
print ('a > 999999', a > 999999)