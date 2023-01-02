# Crear excepción
class operatorException(Exception):
    def __init__(self, message):
        super().__init__(message)


# Función - Dividir
def dividing(a, b):
    if b == 0:
        raise operatorException(
            "¡ERROR, NO SE PUEDE DIVIDIR POR CERO!"
        )  # En caso de dividir por cero.
    else:
        return a / b


dividing(4, 0)
