# Importaciones
import tkinter as tk
from client.guiApp import Frame, menuBar


# Función Principal
def main():
    root = tk.Tk()  # Inicializa la ventana.
    root.title("Catálogo de películas")  # Modifica el título.
    root.iconbitmap("./img/logo.ico")  # Modifica el icono.
    root.resizable(0, 0)  # Desactiva la posibilidad de modificar su tamaño.

    app = Frame(root=root)  # Inicializá la app.
    menuBar(root)  # Inicializá la barra de menú.
    app.mainloop()  # Evita el cierre de la app.


# Punto de Entrada
if __name__ == "__main__":
    main()
