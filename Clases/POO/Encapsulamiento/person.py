# ------------------------------------------------------------------------- #
# APUNTES:
# 		   XXX.
#
#
# IMPORTANTE:
#  			  - <__XXX> = Indica un atributo privado/encapsulado.
# ------------------------------------------------------------------------- #


class Person:
    __name = None
    __age = None

    def __init__(self, __name, __age):
        self.__name = __name
        self.__age = __age

    def privateMethod(self):
        print("¡Soy un método privado!")

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def setName(self, newName):
        self.__name = newName

    def setAge(self, newAge):
        self.__age = newAge

    def __str__(self):
        return f"{self.__name} - {self.__age}"
