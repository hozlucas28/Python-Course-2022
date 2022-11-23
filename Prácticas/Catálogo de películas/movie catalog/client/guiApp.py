# Importación
import tkinter as tk


# Crea la barra de menú
def menuBar(root):
    # Inicialización
    menuBar = tk.Menu(root)
    root.config(menu=menuBar, width=300, height=300)

    # Inicializar y anclar - 'Inicio'
    homeMenu = tk.Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="Inicio", menu=homeMenu)

    # Crear sub-opciones - 'Inicio'
    homeMenu.add_command(label="Crear un registro en base de datos")
    homeMenu.add_command(label="Eliminar registro de la base de datos")
    homeMenu.add_command(label="Salir", command=root.destroy)

    # Inicializar y anclar - 'Consultas', 'Configuración', 'Ayuda'
    menuBar.add_cascade(label="Consultas")
    menuBar.add_cascade(label="Configuración")
    menuBar.add_cascade(label="Ayuda")


# Crea el frame de la ventana
class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.pack()
        self.config(width=480, height=320)  # Configura el frame.

        self.movieField()  # Crea campos para agregar una nueva película.
        self.disableFields()  # Deshabilita los campos.

    def movieField(self):
        # Nombre
        self.labelName = tk.Label(self, text="Nombre: ")
        self.labelName.config(font=("Arial", 12, "bold"))
        self.labelName.grid(row=0, column=0, padx=10, pady=10)

        self.strName = tk.StringVar()
        self.entryName = tk.Entry(self, textvariable=self.strName)
        self.entryName.config(width=50, font=("Arial", 12))
        self.entryName.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

        # Duración
        self.labelDuration = tk.Label(self, text="Duración: ")
        self.labelDuration.config(font=("Arial", 12, "bold"))
        self.labelDuration.grid(row=1, column=0, padx=10, pady=10)

        self.strDuration = tk.StringVar()
        self.entryDuration = tk.Entry(self, textvariable=self.strDuration)
        self.entryDuration.config(width=50, font=("Arial", 12))
        self.entryDuration.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

        # Género
        self.labelGender = tk.Label(self, text="Género: ")
        self.labelGender.config(font=("Arial", 12, "bold"))
        self.labelGender.grid(row=2, column=0, padx=10, pady=10)

        self.strGender = tk.StringVar()
        self.entryGender = tk.Entry(self, textvariable=self.strGender)
        self.entryGender.config(width=50, font=("Arial", 12))
        self.entryGender.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

        # Botón - Nuevo
        self.newButton = tk.Button(self, text="Nuevo", command=self.enableFields)
        self.newButton.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="#DAD5D6",
            bg="#158645",
            cursor="hand2",
            activebackground="#35BD6F",
        )
        self.newButton.grid(row=3, column=0, padx=10, pady=10)

        # Botón - Guardar
        self.saveButton = tk.Button(self, text="Guardar", command=self.saveFields)
        self.saveButton.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="#DAD5D6",
            bg="#1658A2",
            cursor="hand2",
            activebackground="#3586DF",
        )
        self.saveButton.grid(row=3, column=1, padx=10, pady=10)

        # Botón - Cancelar
        self.cancelButton = tk.Button(self, text="Cancelar", command=self.disableFields)
        self.cancelButton.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="#DAD5D6",
            bg="#BD152E",
            cursor="hand2",
            activebackground="#E15370",
        )
        self.cancelButton.grid(row=3, column=2, padx=10, pady=10)

    def enableFields(self):
        self.strName.set("")
        self.strDuration.set("")
        self.strGender.set("")

        self.entryName.config(state="normal")
        self.entryDuration.config(state="normal")
        self.entryGender.config(state="normal")

        self.saveButton.config(state="normal")
        self.cancelButton.config(state="normal")

    def disableFields(self):
        self.strName.set("")
        self.strDuration.set("")
        self.strGender.set("")

        self.entryName.config(state="disabled")
        self.entryDuration.config(state="disabled")
        self.entryGender.config(state="disabled")

        self.saveButton.config(state="disabled")
        self.cancelButton.config(state="disabled")

    def saveFields(self):
        self.disableFields()
