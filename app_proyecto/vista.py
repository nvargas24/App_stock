"""
vista.py:
    Módulo encargado de generar la interfaz gráfica de la app. 
"""
__author__ = "Diego Calderón, Nahuel Vargas"
__maintainer__ = "Diego Calderón, Nahuel Vargas"
__email__ = "diegoacalderon994@gmail.com, nahuvargas24@gmail.com"
__copyright__ = "Copyright 2023"
__version__ = "0.0.1"

from tkinter import StringVar
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import ttk
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo
from modelo import Evento
from modelo import Crud


class Menu:
    """
    Clase que configura la ventana, treeview, botones y mensajes emergentes.

    :param window: Objeto ventana que recibe como argumento de ``controlador.py``
    """

    def __init__(self, window):
        """
        Constructor que configura la ventana y treeview.

        :param window: Objeto ventana que recibe como argumento de ``controlador.py``
        """
        self.window = window
        self.obj_sub_m = SubWindow()  # Creo un objeto de clase Subwindow.

        # --------------------Config de ventana-------------------------
        self.window.title("Control de stock - Electrónica del oeste")

        # --------------------Variables---------------------------------
        self.var_nombre = StringVar()
        self.var_cantidad = StringVar()  # Luego lo convierto a int.
        self.var_precio = StringVar()  # Luego lo convierto a float.
        self.var_descrip = StringVar()
        self.obj_f = Crud()  # Creo un objeto de clase Crud.

        # --------------------Etiquetas---------------------------------
        self.titulo = Label(
            self.window,
            text="Electrónica del oeste",
            background="#51CFF5",
            width=50,
            height=2,
            font=("calibri", 22, "bold"),
        )

        self.subtitulo = Label(
            self.window,
            text="Bienvenido, seleccione la acción a realizar",
            font=("calibri", 12),
        )

        # ---------------------Treeview-----------------------------------
        self.tree = ttk.Treeview(self.window)
        self.tree["columns"] = ("col1", "col2", "col3", "col4")
        self.tree.column("#0", width=50, minwidth=50)
        self.tree.column("col1", width=144, minwidth=144, anchor="center")
        self.tree.column("col2", width=80, minwidth=80, anchor="center")
        self.tree.column("col3", width=80, minwidth=80, anchor="center")
        self.tree.column("col4", width=250, minwidth=250, anchor="center")
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Producto")
        self.tree.heading("col2", text="Cantidad")
        self.tree.heading("col3", text="Precio")
        self.tree.heading("col4", text="Descripción")

        self.obj_f.mostrar_cat(self.tree)

        self.window.grid_rowconfigure(4, minsize=10)
        self.window.grid_rowconfigure(6, minsize=10)
        self.window.grid_rowconfigure(8, minsize=22)
        self.window.grid_rowconfigure(10, minsize=22)

        self.titulo.grid(row=0, column=0, columnspan=4, rowspan=2)
        self.subtitulo.grid(row=2, column=0, columnspan=4, pady=5)

        self.tree.grid(column=0, row=11, columnspan=6, padx=50, pady=40)

        self.obj_sub_m.ingreso_datos(
            self.window,
            self.var_nombre,
            self.var_cantidad,
            self.var_precio,
            self.var_descrip,
        )

        self.menu_opciones()

    def menu_opciones(self):
        """
        Método que configura los botones de opciones.

        """

        # ---------------------Botones--------------------------------------
        agregar = Button(
            self.window,
            text="Agregar artículo",
            background="#51CFF5",
            activebackground="#3FB9F5",
            width=15,
            height=2,
            command=lambda: self.call_agreg(),
        )

        eliminar = Button(
            self.window,
            text="Eliminar artículo",
            background="#51CFF5",
            activebackground="#3FB9F5",
            width=15,
            height=2,
            command=lambda: self.call_elim(),
        )

        modificar = Button(
            self.window,
            text="Modificar artículo",
            background="#51CFF5",
            activebackground="#3FB9F5",
            width=15,
            height=2,
            command=lambda: self.call_modif(),
        )

        consultar = Button(
            self.window,
            text="Consultar stock",
            background="#51CFF5",
            activebackground="#3FB9F5",
            width=15,
            height=2,
            command=lambda: self.call_consulta(),
        )

        catalogo = Button(
            self.window,
            text="Ver Catálogo completo",
            background="#51CFF5",
            activebackground="#3FB9F5",
            width=20,
            height=2,
            command=lambda: self.obj_f.mostrar_cat(self.tree),
        )

        # -------------------Posiciono los controles ---------------------------

        agregar.grid(row=3, column=1, pady=5, padx=50, sticky="w")
        eliminar.grid(row=5, column=1, pady=5, padx=50, sticky="w")
        modificar.grid(row=7, column=1, pady=5, padx=50, sticky="w")
        consultar.grid(row=9, column=1, pady=5, padx=50, sticky="w")
        catalogo.grid(row=7, column=2, columnspan=3, pady=5, padx=130, sticky="w")

    def call_agreg(self):
        """
        Método que imprime un mensaje emergente de acuerdo al string que retorna
        la función de agregar un dato ``agreg()``, que forma parte de ``modelo.py``.

        Si se generó una excepción mostrará el mensaje de error correspondiente.
        """
        try:
            mje = self.obj_f.agreg(
                self.var_nombre,
                self.var_cantidad,
                self.var_precio,
                self.var_descrip,
                self.tree,
            )

        except ValueError as mje:  # Si se genera una excepción, la capturo y muestro mje de error.
            print(mje)
            showerror("Error en la operación", "Campos cargados incorrectamente")

        else:
            if mje == "existe":
                showerror("Error en la carga de datos", "Artículo ya existente")
            elif mje == "cargado":
                showinfo("Operación exitosa", "Artículo cargado correctamente")
            elif mje == "campos vacios":
                showerror(
                    "Error en la operacíon", "No se han completado todos los campos"
                )

        self.obj_f.mostrar_cat(self.tree)

    def call_elim(self):
        """
        Método que imprime un mensaje emergente de acuerdo al string que retorna
        la función de eliminar un dato ``elim()``, que forma parte de ``modelo.py``.

        """
        mje = self.obj_f.elim(self.var_nombre)
        if mje == "eliminado":
            showinfo("Operación exitosa", "Artículo eliminado correctamente")
        elif mje == "no encontrado":
            showerror("Error en la operación", "Artículo no encontrado")
        elif mje == "campo vacio":
            showerror("Error en la operación", "No se ha ingresado ningun nombre")

        self.obj_f.mostrar_cat(self.tree)

    def call_modif(self):
        """
        Método que imprime un mensaje emergente de acuerdo al string que retorna
        la función de modificar un dato ``modif()``, que forma parte de ``modelo.py``.

        Si se generó una excepción mostrará el mensaje de error correspondiente.
        """
        try:
            mje = self.obj_f.modif(
                self.var_nombre,
                self.var_cantidad,
                self.var_precio,
                self.var_descrip,
            )

        except ValueError as mje:  # Si se genera una excepción, la capturo y muestro mje de error.
            print(mje)
            showerror("Error en la operación", "Campos cargados incorrectamente")

        else:
            if mje == "campo vacio":
                showerror("Error en la operación", "No se ha ingresado ningun nombre")
            elif mje == "no existe":
                showerror("Error en la operación", "Artículo no encontrado")
            elif mje == "sin modificar":
                showerror("Error en la operación", "No se completó ningún campo")
            elif mje == "modificado":
                showinfo("Operación exitosa", "Artículo modificado correctamente")

        self.obj_f.mostrar_cat(self.tree)

    def call_consulta(self):
        """
        Método que imprime un mensaje emergente de acuerdo al string que retorna
        la función de consultar stock ``consulta()``, que forma parte de ``modelo.py``.

        """
        mje = self.obj_f.consulta(self.var_nombre, self.tree)
        if mje == "campo vacio":
            showerror("Error en la operación", "No se ha ingresado ningun nombre")
        elif mje == "no encontrado":
            showerror("Error en la operación", "Artículo no encontrado")


class SubWindow:
    """
    Clase que configura las etiquetas y los campos de entrada.
    """

    def ingreso_datos(self, window, var_nombre, var_cantidad, var_precio, var_descrip):
        """
        Método que define las etiquetas, los campos de entrada y eventos asociados a los mismos.

        :param window: Objeto ventana que recibe como argumento de la clase ``Menu()``.
        :param var_nombre: Variable que será asociada al campo de entrada **Nombre**.
        :param var_cantidad: Variable que será asociada al campo de entrada **Cantidad**.
        :param var_precio: Variable que será asociada al campo de entrada **Precio**.
        :param var_descrip: Variable que será asociada al campo de entrada **Descripción**.
        """
        self.obj_e = Evento()

        self.nombre = Label(window, text="\tNombre:")
        self.cantidad = Label(window, text="\tCantidad:")
        self.precio = Label(window, text="\tPrecio:")
        self.descripcion = Label(window, text="\tDescripción:")

        # --------------------------Campos de entrada------------------------------------
        # En lambda, a la función que llama le paso como parámetro
        # "nom"/"cant"/"precio"/"descrip" para hacer referencia
        # al campo "Nombre"/"Cantidad"/"Precio"/"Descripción".

        self.nombre_entry = Entry(window, textvariable=var_nombre, width=30)
        self.nombre_entry.config(foreground="grey")
        self.nombre_entry.insert(0, "Escriba el nombre del artículo")
        self.nombre_entry.bind(
            "<Button-1>",
            lambda event: self.obj_e.click(event, "nom", var_nombre, self.nombre_entry),
        )
        self.nombre_entry.bind(
            "<FocusOut>",
            lambda event: self.obj_e.focus_out(
                event,
                "nom",
                var_nombre,
                self.nombre_entry,
            ),
        )

        self.cantidad_entry = Entry(window, textvariable=var_cantidad, width=30)
        self.cantidad_entry.config(foreground="grey")
        self.cantidad_entry.insert(0, "Escriba un valor numérico")
        self.cantidad_entry.bind(
            "<Button-1>",
            lambda event: self.obj_e.click(
                event, "cant", var_cantidad, self.cantidad_entry
            ),
        )
        self.cantidad_entry.bind(
            "<FocusOut>",
            lambda event: self.obj_e.focus_out(
                event,
                "cant",
                var_cantidad,
                self.cantidad_entry,
            ),
        )

        self.precio_entry = Entry(window, textvariable=var_precio, width=30)
        self.precio_entry.config(foreground="grey")
        self.precio_entry.insert(0, "Escriba un valor numérico")
        self.precio_entry.bind(
            "<Button-1>",
            lambda event: self.obj_e.click(
                event, "precio", var_precio, self.precio_entry
            ),
        )
        self.precio_entry.bind(
            "<FocusOut>",
            lambda event: self.obj_e.focus_out(
                event,
                "precio",
                var_precio,
                self.precio_entry,
            ),
        )

        self.descripcion_entry = Entry(window, textvariable=var_descrip, width=30)
        self.descripcion_entry.config(foreground="grey")
        self.descripcion_entry.insert(0, "Agregue una breve descrip. del art.")
        self.descripcion_entry.bind(
            "<Button-1>",
            lambda event: self.obj_e.click(
                event, "descrip", var_descrip, self.descripcion_entry
            ),
        )
        self.descripcion_entry.bind(
            "<FocusOut>",
            lambda event: self.obj_e.focus_out(
                event,
                "descrip",
                var_descrip,
                self.descripcion_entry,
            ),
        )

        self.nombre.grid(row=3, column=2, sticky="w")
        self.cantidad.grid(row=4, column=2, sticky="w")
        self.precio.grid(row=5, column=2, sticky="w")
        self.descripcion.grid(row=6, column=2, sticky="w")

        self.nombre_entry.grid(row=3, column=3, padx=5, sticky="w")
        self.cantidad_entry.grid(row=4, column=3, padx=5, sticky="w")
        self.precio_entry.grid(row=5, column=3, padx=5, sticky="w")
        self.descripcion_entry.grid(row=6, column=3, padx=5, sticky="w")
