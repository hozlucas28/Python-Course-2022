import sqlite3


class DBConnection:
    def __init__(self):
        self.dataBase = "database/movies.db"
        self.connection = sqlite3.connect(self.dataBase)
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.commit()
        self.connection.close()
