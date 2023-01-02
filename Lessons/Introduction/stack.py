# ------------------------------------------------------------------------- #
# APUNTES:
# 		   Las pilas se utilizan para almacenar datos en donde la devolución
#          de sus elementos comienza del ultimo campo al primero, de manera
#          consecutiva.
#
#
# IMPORTANTE:
#  			  - Las pilas nos permiten almacenar datos y modificarlos.
# ------------------------------------------------------------------------- #

# Declaración de la pila
stack = [1, 2, 3]

# Agregar elementos al final de la pila
stack.append(4)
stack.append(5)
print(stack)

# Quitar el ultimo elemento de la pila
lastElement = stack.pop()
print(f'{stack} --> {lastElement}')
