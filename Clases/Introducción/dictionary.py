# ------------------------------------------------------------------------- #
# APUNTES:
# 		   Los diccionarios se declaran como si fueran objetos en JavaScript.
#
#
# IMPORTANTE:
#  			  - Las claves deben ser únicas.
# ------------------------------------------------------------------------- #

# Declaración del diccionario
dictionary = {'firstName': 'Lucas', 'lastName': 'Hoz', 'age': 20}

# Obtener el valor de la clave enviada
print(dictionary['firstName'])

# Agregar elementos al diccionario
dictionary['address'] = 'Paso del rey'
print(dictionary)

# Buscar elemento según la clave enviada
aux = dictionary.get('key', 'La clave no existe')
print(aux)

# Devolver todas las claves
print(dictionary.keys())

# Devolver todos los valores
print(dictionary.values())

# Devolver claves y valores
print(dictionary.items())

# Quitar la clave enviada
aux = dictionary.pop('age', 'La clave no existe')

# Limpiar diccionario
dictionary.clear()
print(dictionary)