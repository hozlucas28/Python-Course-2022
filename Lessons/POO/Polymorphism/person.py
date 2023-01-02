# ------------------------------------------------------------------------- #
# APUNTES:
# 		   El polimorfismo es la capacidad de reescribir métodos de la
#          clase padre.
#
#
# IMPORTANTE:
#  			  - El parámetro <object> es irrelevante.
# ------------------------------------------------------------------------- #


class Person(object):
    def __init__(self, name):
        self.name = name

    def move(self):
        print("¡Estoy Caminando!")


class Athlete(Person):
    def move(self):
        print("¡Estoy Corriendo!")


class Cyclist(Person):
    def move(self):
        print("¡Estoy Ciclando!")
