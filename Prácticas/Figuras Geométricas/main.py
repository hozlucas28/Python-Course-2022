# Importación
from figures import Figure, Rectangle, Circle, testFigure


# Función Principal
def main():
    menu = """
    Opciones disponibles...
    - 1 : Rectángulo.
    - 2 : Circulo.
    - 3 : Salir
    • Seleccionar opción: """

    while True:
        optionSelected = int(input(menu))
        if optionSelected == 1 or optionSelected == 2:
            if optionSelected == 1:
                print("|---------- Rectángulo ----------|")
                base = float(input("• Ingrese la base: "))
                height = float(input("• Ingrese la altura: "))
                rectangle = Rectangle("Rectángulo", base, height)
                testFigure(rectangle)
            else:
                print("|---------- Circulo ----------|")
                radio = float(input("• Ingrese el radio: "))
                circle = Circle("Circulo", radio)
                testFigure(circle)
        elif optionSelected == 3:
            print("¡Aplicación Cerrada!")
            break
        else:
            print("¡Error! La opción ingresada no es válida")


# Punto de Entrada
if __name__ == "__main__":
    main()
