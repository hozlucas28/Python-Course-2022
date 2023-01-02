# ------------------------------------------------------------------------- #
# APUNTES:
# 		   El atributo 'name' del objeto persona no es modificable, una vez
#          definido, porque se trata de un atributo privado/encapsulado.
#          Salvo que se realize dicha modificación mediante los métodos
#          declarados en la misma clase del objeto.
#
#
# IMPORTANTE:
#  			  - XXX.
# ------------------------------------------------------------------------- #

# Importación
from person import Person

firstPerson = Person("Lucas", 20)

firstPerson.__name = "Nahuel"
firstPerson.__age = 18
print(firstPerson)

firstPerson.setName("Nahuel")
firstPerson.setAge(18)
print(firstPerson)
