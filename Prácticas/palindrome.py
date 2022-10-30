# ¿Es palíndroma?
def isPalindrome(word):
    word = word.lower()
    wordReversed = word[::-1]
    return word == wordReversed


# Función Principal
def main():
    word = input('Ingrese una palabra: ')

    if (isPalindrome(word)):
        print(f'La palabra {word} es palíndroma.')
    else:
        print(f'La palabra {word} no es palíndroma.')


# Punto de Entrada
if (__name__ == '__main__'):
    main()
