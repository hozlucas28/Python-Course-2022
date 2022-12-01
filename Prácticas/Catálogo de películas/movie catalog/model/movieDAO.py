# Importaciones
from tkinter import messagebox
from .dbConnection import DBConnection


class Movie:
    def __init__(self, name, duration, gender):
        self.id = None
        self.name = name
        self.duration = duration
        self.gender = gender

    def __str__(self):
        return f"Movie [{self.name}, {self.duration}, {self.gender}]"


def createTable():
    # Establecer conexión y definir consulta
    connection = DBConnection()
    query = """
        CREATE TABLE movies(
            id INTEGER,
            name VARCHAR(100),
            duration VARCHAR(10),
            gender VARCHAR(100),
            PRIMARY KEY(id AUTOINCREMENT)
        )
    """

    # Ejecutar consulta
    try:
        connection.cursor.execute(query)
        connection.close()

        title = "Crear Registro"
        message = "Se creo la tabla en la base de datos."
        messagebox.showinfo(title, message)
    except:
        title = "Crear Registro"
        message = "¡Error! La tabla ya existe en la base de datos."
        messagebox.showwarning(title, message)


def deleteTable():
    connection = DBConnection()
    query = "DROP TABLE movies"

    try:
        connection.cursor.execute(query)
        connection.close()

        title = "Borrar Registro"
        message = "Se borro la tabla de la base de datos."
        messagebox.showinfo(title, message)
    except:
        title = "Borrar Registro"
        message = "¡Error! La tabla no existe en la base de datos."
        messagebox.showwarning(title, message)


def saveData(Movie):
    connection = DBConnection()
    query = f"""
        INSERT INTO movies(name, duration, gender)
        VALUES('{Movie.name}', '{Movie.duration}', '{Movie.gender}')
    """

    try:
        connection.cursor.execute(query)
        connection.close()
    except:
        title = "Guardar"
        message = "¡Error! La tabla no existe en la base de datos."
        messagebox.showwarning(title, message)


def deleteData(id):
    connection = DBConnection()
    query = f"DELETE FROM movies WHERE id = {id}"

    try:
        connection.cursor.execute(query)
        connection.close()
    except:
        title = "Eliminar Registro"
        message = "¡Error! No se pudo eliminar el registro de la base de datos."
        messagebox.showwarning(title, message)


def updateData(movie, id):
    connection = DBConnection()
    query = f"""
        UPDATE movies SET
            name = '{movie.name}',
            duration = '{movie.duration}',
            gender = '{movie.gender}'
        WHERE id = {id}
    """

    try:
        connection.cursor.execute(query)
        connection.close()
    except:
        title = "Actualizar el Registro"
        message = "¡Error! No se pudo actualizar el registro de la base de datos."
        messagebox.showwarning(title, message)


def getDataList():
    connection = DBConnection()
    query = "SELECT * FROM movies"
    moviesList = []

    try:
        connection.cursor.execute(query)
        moviesList = connection.cursor.fetchall()  # Obtener registros de la consulta
        connection.close()
    except:
        title = "Conexión al Registro"
        message = "¡Error! Creé la tabla en la base de datos."
        messagebox.showwarning(title, message)
    return moviesList
