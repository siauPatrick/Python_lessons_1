
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

from math import sqrt

print('Задача №1')
class Triangle:
    def __init__(self, vertexes):
        self.vertexes = vertexes

    def side(self):
        sides = []
        for i in range(3):
            if i < 2:
                sides.append(round((sqrt((self.vertexes[i+1][0] - self.vertexes[i][0]) ** 2 +
                                  (self.vertexes[i+1][1] - self.vertexes[i][1]) ** 2)), 1))
            else:
                sides.append(round((sqrt((self.vertexes[i - 2][0] - self.vertexes[i][0]) ** 2 +
                                  (self.vertexes[i - 2][1] - self.vertexes[i][1]) ** 2)), 1))
        return sides

    def perimetr(self):
        sides = self.side()
        return sum(sides)

    def area(self):
        per = self.perimetr() / 2
        sides = self.side()
        return round(sqrt(per * (per - sides[0]) * (per - sides[1]) * (per - sides[2])), 1)



triangle = Triangle([[0, 0], [0, 4], [4, 0]])
print('Площадь фигуры: ', triangle.area())
print('Периметр фигуры: ', triangle.perimetr())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

print('\n\n Задача №2')

class Trapeze:
    def __init__(self, vertexes):
        self.vertexes = vertexes

    def side(self):
        sides = []
        for i in range(4):
            if i < 3:
                sides.append(round((sqrt((self.vertexes[i+1][0] - self.vertexes[i][0]) ** 2 +
                                  (self.vertexes[i+1][1] - self.vertexes[i][1]) ** 2)), 1))
            else:
                sides.append(round((sqrt((self.vertexes[i - 3][0] - self.vertexes[i][0]) ** 2 +
                                  (self.vertexes[i - 3][1] - self.vertexes[i][1]) ** 2)), 1))

        return sides

    def check_sides(self):
        sides = self.side()
        if sides[0] == sides[2] or sides[1] == sides[3]:
            print('Трапеция равнобокая')
        else:
            print('Отсутствуют попарно равные стороны')

    def perimetr(self):
        sides = self.side()
        return sum(sides)

    def area(self):
        per = self.perimetr() / 2
        sides = self.side()
        return round(sqrt(per * (per - sides[0]) * (per - sides[1]) * (per - sides[2])), 1)



trapeze_1 = Trapeze([[0, 0], [1, 4], [4, 4], [5, 0]])
print('Длины сторон: ', trapeze_1.side())
print('Площадь фигуры: ', trapeze_1.area())
trapeze_1.check_sides()  # Проверка на равнобокую трапецию
print('Периметр фигуры: ', trapeze_1.perimetr())