# ------------------------------- Importaciones ------------------------------ #

from math import pi


# ---------------------------------- Clases ---------------------------------- #


class Figure:
    def __init__(self, name):
        self.name = name

    def getArea(self):
        pass

    def getPerimeter(self):
        pass

    def __str__(self):
        return f"{self.name}"


class Rectangle(Figure):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height

    def getArea(self):
        area = self.base * self.height
        return area

    def getPerimeter(self):
        perimeter = (2 * self.base) + (2 * self.height)
        return perimeter

    def __str__(self):
        fatherReturn = super().__str__()
        return fatherReturn + f" - {self.base} - {self.height}"


class Circle(Figure):
    def __init__(self, name, radio):
        super().__init__(name)
        self.radio = radio

    def getArea(self):
        area = pi * (self.radio**2)
        return area

    def getPerimeter(self):
        perimeter = 2 * pi * self.radio
        return perimeter

    def __str__(self):
        fatherReturn = super().__str__()
        return fatherReturn + f" - {self.radio}"


# --------------------------------- Funciones -------------------------------- #


def testFigure(figure):
    print("• Estado del objeto:", figure)
    print("• Área:", figure.getArea())
    print("• Perímetro:", figure.getPerimeter())
