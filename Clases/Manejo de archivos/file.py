# ------------------------------------------------------------------------- #
# APUNTES:
# 		   Este archivo debe ser ejecutado desde CMD, con el interpretador
#          de Python.
#          Si el método es 'r' ó 'a' y el archivo no existe lanzara un error,
#          en cambio si el método es 'w' y el archivo no existe este sera creado.
#
#
# IMPORTANTE:
#             - Método 'w' = Crea/Reescribe el archivo.
#             - Método 'r' = Lee el contenido del archivo.
#             - Método 'a' = Permite agregar datos al final del archivo.
#             - Método 'r+' = Permite leer y escribir datos del archivo.
#
#  			  - open(<NOMBRE DEL ARCHIVO>, <MÉTODO>) = Abre el archivo.
#             - <ARCHIVO>.write(<CONTENIDO>) = Escribe el contenido.
#             - <ARCHIVO>.read() = Devuelve el contenido.
#             - <ARCHIVO>.readlines() = Devuelve el contenido en formato array.
#             - <ARCHIVO>.close() = Cierra el archivo.
#
#             - <ARCHIVO>.seek(<POSICIÓN>) = Posiciona al puntero.
# ------------------------------------------------------------------------- #

# Importación
from io import open
from os import path


# Escribir archivo
def writeFile():
    file = open("write.txt", "w")
    file.write("Hola Mundo")
    file.close()


# Leer archivo
def readFile():
    if path.isfile("read.txt"):  # Verifica si el archivo existe.
        file = open("read.txt", "r")
        # content = file.read()
        content = file.readlines()
        file.close()
        print(content)
    else:
        print("¡NO EXISTE EL ARCHIVO!")


# Agregar contenido
def addContentToFile():
    if path.isfile("add.txt"):
        file = open("add.txt", "a")
        file.write("\nHola Lucas")
        file.close()
    else:
        print("¡NO EXISTE EL ARCHIVO!")


# Actualizar contenido
def updateContentOfFile():
    if path.isfile("update.txt"):
        file = open("update.txt", "r+")
        content = file.readlines()
        content[2] = "Hola Nahuel - Linea 3"

        file.seek(0)  # Posiciona el puntero al inicio del archivo.
        file.writelines(content)
        file.close()
    else:
        print("¡NO EXISTE EL ARCHIVO!")


# Eliminar contenido
def deleteContentOfFile():
    file = open("delete.txt", "w")
    file.close()


# writeFile()
# readFile()
# addContentToFile()
# updateContentOfFile()
deleteContentOfFile()
