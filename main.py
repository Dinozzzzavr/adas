# экземпляры класса Rectangle и Triangle
from triangle import Triangle
from circle import Circle
from rectangle import Rectangle
try:
    rect1 = Rectangle(4, 5)
    rect2 = Rectangle(8, 10)
    irc = Circle(8)
    #print(f"Площадь равна:{rect1.get_area()}")
    #print(f"Периметр равен:{rect1.get_perimeter()}")
    #print(f"Площадь равна:{rect2.get_perimeter()}")
    #print(f"Периметр равен:{rect2.get_perimeter()}")
    trian1 = Triangle(3, 4, 5)
    trian2 = Triangle(5, 5, 5)
    figures=[rect1,rect2,trian1,trian2,irc]
    for item in figures:
        print(f"Площадь равна:{item.get_perimeter()}")
        print(f"Периметр равен:{item.get_area()}")
except NotImplementedError as exc:
    print(exc.__str__())
