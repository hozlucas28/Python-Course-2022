# ------------------------------------------------------------------------- #
# APUNTES:
# 		   XXX.
#
#
# IMPORTANTE:
#  			  - <sys.argv> = Devuelve un 'Array' con los argumentos enviados,
#                            cuando se ejecuta el script..
# ------------------------------------------------------------------------- #


# Importaciones
import sys

if len(sys.argv) == 3:
    text = sys.argv[1]
    number = int(sys.argv[2])

    for i in range(0, number):
        print(f"{text}")
else:
    print("¡Error! No se has enviado tres argumentos.")
    print(
        "• Por ejemplo: C:/Python310/python.exe c:/Users/hozlu/Documents/Workspace/Python-Course-2022/Clases/Modularización/entry-script.py 'Hola Mundo' 5"
    )
