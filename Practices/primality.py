# ¿Es primo?
def isPrime(number=0):
    counter = 0

    for i in range(1, number + 1):
        if (number % i == 0):
            counter += 1
    return (counter == 2)


# Función Principal
def main():
    number = int(input('Ingrese un número: '))
    if (isPrime(number)):
        print(f'El número {number} es primo.')
    else:
        print(f'El número {number} no es primo.')


# Punto de Entrada
if (__name__ == '__main__'):
    main()