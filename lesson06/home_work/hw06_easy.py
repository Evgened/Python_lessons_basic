# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

class Dot:
    __dot: []

    def __init__ (self, coord):
        self.set_dot(coord)

    def set_dot(self, dot):
        if len(dot) != 2:
            print ('Координат точки должно быть две')
            return
        elif dot[0] == '' or dot[1] == '':
            print ('Координата точки не может быть пустой')
            return
        self.__dot = dot

    def get_dot_dist (self, dot2):
        return (math.sqrt((dot2[0] - self[0])**2 + (dot2[1] - self[1])**2))

    @property
    def get_dot (self):
        return self.__dot

class Triangle (Dot):
    __dots: []

    def __init__(self, tr_dots):
        self.set_dots(tr_dots)

    def set_dots(self, dots_list: list):
        if len(dots_list) != 3:
            print ('Треугольник задаётся тремя координатами')
            return
        self.__dots = dots_list

    @property
    def get_square (self):
        return (abs((self.__dots[1][0] - self.__dots[0][0])*(self.__dots[2][1] - self.__dots[0][1]) - (self.__dots[2][0] - self.__dots[0][0])*(self.__dots[1][1] - self.__dots[0][1])) / 2)

    @property
    def get_perim (self):
        return Dot.get_dot_dist(self.__dots[0], self.__dots[1]) + Dot.get_dot_dist(self.__dots[0], self.__dots[2]) + Dot.get_dot_dist(self.__dots[0], self.__dots[2])

d1 = Dot([-10, 0])
d2 = Dot([0, 10])
d3 = Dot([0, 0])

tr_dots = [d1.get_dot, d2.get_dot, d3.get_dot]
print (tr_dots)

tr = Triangle(tr_dots)
# задаём список точек треугольника
tr.set_dots(tr_dots)
print ('Площадь треугольника: ', tr.get_square)
print ('Периметр треугольника: ', tr.get_perim)


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezoid:
    dots: list([list, list, list, list])
    lenghts: list

    def get_len (dot1, dot2):
        return (math.sqrt((dot2[0] - dot1[0])**2 + (dot2[1] - dot1[1])**2))

    def set_dots(self, dots_list: list):
        tr_lenght = []
        next_dot = 0
        if len(dots_list) != 4:
            print ('Трапеция задаётся четырьмя координатами')
            return
        for i, x in enumerate(dots_list):
            if len(x) != 2:
                print ('Координат точки должно быть две')
                return
            else:
                if i == 3:
                    next_dot = 0
                else:
                    next_dot = i + 1
                tr_lenght.append(Trapezoid.get_len (self.dots[i], self.dots[next_dot]))
        tr_lenght.sort()
        if not (tr_lenght[1] == tr_lenght[2] and tr_lenght[0] < tr_lenght[3]):
            print ('Фигура не является равнобочной трапецией')
            return
        self.lenghts = tr_lenght

    @property
    def get_perim (self):
        perim = 0
        for i in self.lenghts:
            perim = perim + i
        return perim

    @property
    def get_lenghts (self):
        return lenghts

    @property
    def get_square (self):
        # объемный расчёт
        pass



trp = Trapezoid()

trp.dots = list([[0, 0], [5, 10], [15, 10], [20, 0]])

trp.set_dots(trp.dots)
print ('Периметр трапеции: ', trp.get_perim)
print ('Длины сторон: ', trp.lenghts)
print ('Площадь: <>', trp.get_square)
