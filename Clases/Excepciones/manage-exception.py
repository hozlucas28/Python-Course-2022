add = 0
counter = 0

while counter < 3:
    # Manejador de excepciones
    try:  # Instrucciones donde se genera la excepción.
        number = int(input("- Ingrese un número: "))
        add += number
        counter += 1
    except:  # Se produjo excepción.
        print("¡INGRESE SOLO NÚMEROS ENTEROS!")
    else:  # No se produjo excepción.
        print("----- El tipo de dato ingresado es correcto -----")
    finally:  # Se produjo ó no excepción.
        print("----- Fin de la ejecución -----")

print(f"• La suma total es: {add}")
