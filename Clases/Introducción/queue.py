# ------------------------------------------------------------------------- #
# APUNTES:
# 		   Las listas se utilizan para almacenar datos en donde la devolución
#          de sus elementos comienza del primer campo al ultimo, de manera
#          consecutiva.
#
#
# IMPORTANTE:
#  			  - Las listas nos permiten almacenar datos y modificarlos.
# ------------------------------------------------------------------------- #

# Importación
from collections import deque

# Declaración de la cola
queue = deque(['Alex', 'Lucas', 'Nahuel'])

# Agregar elemento al final de la lista
queue.append('Carlos')
print(queue)

# Quitar el primer elemento de la lista
firstElement = queue.popleft()
print(f'{firstElement} <-- {queue}')