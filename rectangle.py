# Создайте класс Rectangle, описывающий прямоугольник. В классе должны быть следующие свойства:
    # _length – длина прямоугольника
    # _width – ширина прямоугольника
# В каждом из классов создайте следующие методы:
    # get_area() – возвращает площадь фигуры
    # get_perimeter() – возвращает периметр фигуры


# подключаем класс Figure из модуля figure
from figure import Figure

class Rectangle(Figure):
    def __init__(self,length ,width ):
        self._length = length
        self._width = width
    def get_area(self):
        return self._length * self._width

    def get_perimeter(self):
        return (self._length + self._width)*2