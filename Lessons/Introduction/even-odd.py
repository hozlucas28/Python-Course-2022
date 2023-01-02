# Entrada
number = int(input('Ingrese un número par o impar: '))

# Salidas
if number != 0:
    if number > 0:
        if number % 2 == 0:
            print(f'El número {number} es par positivo.')
        else:
            print(f'El número {number} es impar positivo.')
    else:
        if number % 2 == 0:
            print(f'El número {number} es par negativo.')
        else:
            print(f'El número {number} es impar negativo.')
else:
    print(f'El número {number} es neutro.')
