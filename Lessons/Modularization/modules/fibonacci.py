# Muestra en consola la secuencia de números
def fibo(number):
    a, b = 0, 1
    while a < number:
        print(a, end=" ")  # Mostrar en consola sin salto de línea.
        a, b = b, a + b

    print() # Realizar salto de línea.


# Devuelve la secuencia de números como un 'Array'
def fiboArray(number):
    result = []
    a, b = 0, 1
    while a < number:
        result.append(a)
        a, b = b, a + b

    return result
