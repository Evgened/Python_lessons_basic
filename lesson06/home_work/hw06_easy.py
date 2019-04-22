# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

class Triangle:
    dots: list([list, list, list])

    def set_dots(self, dots_list: list):
        if len(dots_list) != 3:
            print ('Треугольник задаётся тремя координатами')
            return
        for i in dots_list:
            if len(i) != 2:
                print ('Координат точки должно быть две')
                return
        self.dots = dots_list

    @property
    def get_square (self):
        return (abs((self.dots[1][0] - self.dots[0][0])*(self.dots[2][1] - self.dots[0][1]) - (self.dots[2][0] - self.dots[0][0])*(self.dots[1][1] - self.dots[0][1])) / 2)

    def get_len (dot1, dot2):
        return (math.sqrt((dot2[0] - dot1[0])**2 + (dot2[1] - dot1[1])**2))

    @property
    def get_perim (self):
        return(Triangle.get_len (self.dots[0], self.dots[1]) + Triangle.get_len (self.dots[0], self.dots[2]) + Triangle.get_len (self.dots[1], self.dots[2]))

tr = Triangle()

tr.dots = list([[-10, 0], [0, 10], [0, 0]])
tr.set_dots(tr.dots)

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
