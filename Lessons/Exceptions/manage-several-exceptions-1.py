operation = 0

try:
    numerator = int(input("- Ingrese el numerador: "))
    denominator = int(input("- Ingrese el denominador: "))
    operation = numerator / denominator

except ValueError:  # En caso de ingresar caracteres.
    print("¡ERROR, INGRESE NÚMEROS ENTEROS!")

except ZeroDivisionError:  # En caso de dividir por cero.
    print("¡ERROR, NO SE PUEDE DIVIDIR POR CERO!")

except Exception as error:  # Capturar excepción.
    print(
        f"- Ha ocurrido el error: {type(error).__name__}"
    )  # Muestra el nombre del tipo de excepción.

print(f"• La división es: {operation}")
