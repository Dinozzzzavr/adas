# Создайте класс Triangle, описывающий треугольник. В классе должны быть следующие свойства:
    # _side1 – первая сторона треугольника
    # _side2 – вторая сторона треугольника
    # _side3 – третья сторона треугольника
# В каждом из классов создайте следующие методы:
    # get_area() – возвращает площадь фигуры
    # get_perimeter() – возвращает периметр фигуры

# подключаем класс Figure из модуля figure
import math
from figure import Figure
class Triangle(Figure):
    def __init__(self,side1,side2 ,side3):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3
    def get_perimeter(self):
       return self._side1 + self._side2 + self._side3

    #p = (self._side1 + self._side2 + self._side3) / 2
        #return math.sqrt(p*(p-self._side1)*(p-self._side2)*(p-self._side3))