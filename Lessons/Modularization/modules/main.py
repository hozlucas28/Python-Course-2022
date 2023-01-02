# Importaciones
import fibonacci  # Importa todo el módulo.

# from fibonacci import fibo, fiboArray  # Importa funciones especificas del módulo.
# from fibonacci import *  # Importa todas las funciones del módulo.
# import fibonacci as feb  # Importa todo el módulo, utilizando un alias para acceder a el.
# from fibonacci import fibo as fi, fiboArray as fiArr # Importa funciones especificas del módulo, utilizando un alias para acceder a ellas.

fibonacci.fibo(100)
print(fibonacci.fiboArray(100))

# fibo(100)
# print(fiboArray(100))
# feb.fibo(100)
# print(feb.fiboArray(100))
# fi(100)
# print(fiArr(100))

print(dir(fibonacci)) # Devuelve información de la importación.
