# ------------------------------------------------------------------------- #
# APUNTES:
# 		   Al tener un constructor no es necesario definir los atributos.
#
#
# IMPORTANTE:
#  			  - <self> = Indica que el método pertenece a su clase contenedora.
#             - <__init__> = Indica la declaración de un constructor.
#             - <__str__> = Indica la declaración de un método que devuelve
#                           el estado del objeto.
# ------------------------------------------------------------------------- #


class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Métodos
    def showData(self): # Mostrar atributos.
        print(f"• Nombre: {self.name} • Edad: {self.age}")

    def __str__(self):
        return f'{self.name} - {self.age}'
