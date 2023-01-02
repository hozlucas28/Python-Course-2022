# ------------------------------------------------------------------------- #
# APUNTES:
# 		   XXX.
#
#
# IMPORTANTE:
#  			  - *<var> = Indica el envio de una cantidad 'n' de argumentos.
#             - **<var> = Indica el envio de un argumento por nombre.
# ------------------------------------------------------------------------- #

# ---------------------------------- Función --------------------------------- #


def add(*args):
    operation = 0
    for i in args:
        operation += i
    return operation


# ----------------------------- Código Principal ----------------------------- #

add = add(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(add)