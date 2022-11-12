def dividing(a, b):
    if b == 0:
        raise ZeroDivisionError(
            "¡ERROR, NO SE PUEDE DIVIDIR POR CERO!"
        )  # En caso de dividir por cero.
    else:
        return a / b


dividing(4, 0)
