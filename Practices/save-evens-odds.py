# Importación
from random import randint

# Declaraciones
evens = []
odds = []

tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Operaciones y Salidas
for i in tuple:
    randNumber = randint(0, 100)
    operation = i * randNumber
    print(f'{i} x {randNumber} = {operation}')
    if (operation % 2 == 0):
        evens.append(operation)
    else:
        odds.append(operation)
print(f'• Lista de pares: {evens}', )
print(f'• Lista de impares: {odds}')