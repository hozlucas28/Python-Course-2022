# Importaciones
from random import randint


# Iniciar juego
def startGame(difficulty):
    global numberToGuess
    lives = getLives(difficulty)
    numberToGuess = randint(1, 101)
    # print(f'{numberToGuess}')
    print("\n----- Número aleatorio entre 1 y 100 generado ¡A jugar! -----\n")

    while lives > 0:
        print(f"• Vidas: {lives}.")
        number = int(input("• Ingrese un número: "))
        if number != numberToGuess:
            lives -= 1
            if lives > 0:
                print("¡Mal!")
                showClue(number)
            else:
                print("\n----- ¡JUEGO TERMINADO! Te has quedado sin vidas -----\n")
        else:
            print("\n----- ¡FELICITACIONES! Adivinaste el número -----\n")
            break


# Mostrar pista
def showClue(number):
    if number < numberToGuess:
        print("\n----- ¡Pista! El numero que ingresaste es menor -----\n")
    else:
        print("\n----- ¡Pista! El numero que ingresaste es mayor -----\n")


# Obtener numero de vidas
def getLives(difficulty):
    if difficulty == 1:
        lives = 10
    elif difficulty == 2:
        lives = 7
    else:
        lives = 5
    return lives


# Obtener dificultad
def getDifficulty():
    menu = """
    Dificultades...
    0 - Salir
    1 - Fácil = 10 vidas/intentos
    2 - Intermedio = 7 vidas/intentos
    3 - Difícil = 5 vidas/intentos

    • Seleccionar dificultad: """
    difficultySelected = int(input(menu))
    while difficultySelected < 0 or difficultySelected > 3:
        difficultySelected = int(
            input(
                "¡Error! La dificultad seleccionada no es valida, vuelva a intentar: "
            )
        )
    return difficultySelected


# Función Principal
def main():
    difficulty = getDifficulty()
    if difficulty == 1 or difficulty == 2 or difficulty == 3:
        startGame(difficulty)


# Punto de Entrada
if __name__ == "__main__":
    main()
