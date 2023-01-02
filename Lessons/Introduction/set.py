# ------------------------------------------------------------------------- #
# APUNTES:
# 		   Los conjuntos se deben utilizar cuando trabajemos con una gran
#          cantidad de datos que no queremos que se repitan.
#
#
# IMPORTANTE:
#             - Los elementos que conforman al conjunto siempre estarán
#               desordenados.
#  			  - Si declaro un 'string' en el conjunto, el mismo será separado
#               en los caracteres que lo componen.
# ------------------------------------------------------------------------- #

# Declaración de conjuntos
mySetA = set()
mySetB = set('puente')

# Observación de la no aceptación de elementos repetidos
mySetA = {'a', 'b', 'c', 'd', 'c', 'b', 'a', 'e'}
print(mySetA)

# Devolver elementos que están en A, pero no en B
print(mySetA - mySetB)

# Devolver las letras de A y B
print(mySetA | mySetB)

# Devolver las letras que comparten A y B
print(mySetA & mySetB)

# Devolver las letras que no comparten A y B
print(mySetA ^ mySetB)

# Agregar un elemento al conjunto
mySetA = {'a', 'b', 'c'}
mySetA.add('d')
print(mySetA)

# Eliminar un elemento al conjunto
mySetA.discard('b')
print(mySetA)

# Limpiar conjunto
mySetA.clear()
print(mySetA)