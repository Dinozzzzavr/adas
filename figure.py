# класс, описывающий фигуру
class Figure:
    # метод для получения площади фигуры
    def get_area(self):
       raise NotImplementedError("метод get_area() нужно определить в дочернем классе")

    # метод для получения площади фигуры
    def get_perimeter(self):
        raise NotImplementedError( "медот get_perimeter() нужно определить в дочернем классе")
