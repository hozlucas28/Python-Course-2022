# ------------------------------------------------------------------------- #
# APUNTES:
# 		   Una clase heredada tendrá los mismos atributos y métodos
#          de su clase 'padre'.
#          Tambien se puede heredar sin utilizar <super()> apuntando a la
#          clase y luego a su método, enviando los argumentos que este 
#          solicita.
#
#
# IMPORTANTE:
#  			  - <super().METODO> = 'Importa' el contenido del método de
#                                  la clase padre.
# ------------------------------------------------------------------------- #


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showData(self):
        print(f"• Nombre: {self.name}\n• Edad: {self.age}")

    def __str__(self):
        return f"{self.name} - {self.age}"


# Clase heredada de 'Person'.
class Client(Person):
    pass


# Clase heredada de 'Person'.
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def showData(self):
        super().showData()
        print(f"• Salario: {self.salary}")

    def __str__(self):
        fatherReturn = super().__str__()
        return fatherReturn + f" - {self.salary}"
