# Importaciones
import random


# Generar contraseña
def generatePassword(passwordLenght):
    symbols = ['#', '!', '&', '%', '$']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    lowercases = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    uppercases = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    password = []
    characters = numbers + symbols + lowercases + uppercases

    for i in range(0, passwordLenght):
        rdCharacter = random.choice(characters)
        password.append(rdCharacter)

    password = ''.join(password)
    return password


# Función Principal
def main():
    passwordLenght = int(
        input('Ingrese la cantidad de caracteres de la contraseña: '))
    password = generatePassword(passwordLenght)
    print(f'La contraseña generada es: {password}')


# Punto de Entrada
if (__name__ == '__main__'):
    main()
