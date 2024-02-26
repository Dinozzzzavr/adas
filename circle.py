# Создайте класс Circle, описывающий круг. В классе должны быть следующие свойства:
    # _radius –  радиус

from figure import Figure
import math
class Circle(Figure):
    def __init__(self,radius):
        self._radius = radius
    def get_area(self):
        return math.pi * (self._radius**2)