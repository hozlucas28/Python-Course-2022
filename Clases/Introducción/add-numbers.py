# Variables
add = 0
number = 0
counter = 0

# Entrada
number = int(input('Ingrese un entero positivo, distinto a cero: '))

while number <= 0:
    number = int(
        input('¡Error! Ingrese un entero positivo (distinto a cero): '))

# Proceso
while counter < number:
    add += counter
    counter += 1

# Salida
print(f'La suma es: {add}')