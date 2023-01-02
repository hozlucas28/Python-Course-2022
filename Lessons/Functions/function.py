# --------------------------------- Funciones -------------------------------- #


def add(a, b):
    return a + b


def subtraction(a=None, b=None):
    if (a == None or b == None):
        print('¡Error!, Debes enviar dos valores a la función')
        return
    else:
        return a - b


# def greet(firstName='', lastName=''):
# global secondName
# secondName = 'Nahuel'
# return f'Hola {firstName} {lastName}'

# ----------------------------- Código Principal ----------------------------- #

add = add(1, 7)
subtraction = subtraction(b=20, a=8)

print(f'• La suma es {add}')
print(f'• La resta es {subtraction}')

# print(greet('Lucas', 'Hoz'))
# print(f'Hola {secondName}')