# ------------------------------------------------------------------------- #
# APUNTES:
# 		   Las funciones del tipo lambda tienen la misma finalidad que
#          las funciones flechas en JavaScript.
#
#
# IMPORTANTE:
#  			  - XXX.
# ------------------------------------------------------------------------- #

# Funciones lambda
add = lambda a, b: a + b
substraction = lambda a, b: a - b

even = lambda a: a % 2 == 0
odd = lambda a: a % 2 != 0

reverseString = lambda string: string[::-1]

# Salidas
print(add(10, 15))
print(substraction(10, 15))

print(even(2))
print(odd(2))

print(reverseString('Hola'))
