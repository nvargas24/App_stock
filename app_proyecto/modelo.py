"""
modelo.py:
    Módulo encargado de la lógica de la app, lo cual implica el manejo de base de datos, CRUD, y eventos. 
"""
__author__ = "Diego Calderón, Nahuel Vargas"
__maintainer__ = "Diego Calderón, Nahuel Vargas"
__email__ = "diegoacalderon994@gmail.com, nahuvargas24@gmail.com"
__copyright__ = "Copyright 2023"
__version__ = "0.0.1"

from peewee import *
from validar import Validacion

# --------------------Variables---------------------------------
# Flag utilizado para informar si hubo un error en la validación de los datos de un campo a actualizar.
flag_e = 0
# Flag utilizado para informar que existe un dato válido para actualizar en el campo cantidad.
flag_c = 0
# Flag utilizado para informar que existe un dato válido para actualizar en el campo precio.
flag_p = 0
# Flag utilizado para informar que existe un dato válido para actualizar en el campo descripción.
flag_d = 0


class Evento:
    """
    Clase que integra los métodos asociados a los eventos de los campos de entrada.
    """

    def click(self, event, campo, var, entry):
        """
        Método que borra el texto escrito por defecto de acuerdo al campo donde se hizo click.

        :param event: Evento ``<<Button-1>>`` que recibe como argumento.
        :param campo: Tipo de campo de entrada donde se realizó click.
        :param var: Variable asociada al campo de entrada.
        :param entry: Campo de entrada donde se realizó click.
        """
        if campo == "nom":
            if var.get() == "Escriba el nombre del artículo":
                entry.delete(0, "end")
                entry.config(foreground="black")
        elif campo == "cant":
            if var.get() == "Escriba un valor numérico":
                entry.delete(0, "end")
                entry.config(foreground="black")
        elif campo == "precio":
            if var.get() == "Escriba un valor numérico":
                entry.delete(0, "end")
                entry.config(foreground="black")
        elif campo == "descrip":
            if var.get() == "Agregue una breve descrip. del art.":
                entry.delete(0, "end")
                entry.config(foreground="black")

    def focus_out(self, event, campo, var, entry):
        """
        Método que reescribe el texto por defecto de acuerdo al campo que se encuentre vacío
        y si no se está posicionado sobre el mismo.

        :param event: Evento ``<<FocusOut>>`` que recibe como argumento.
        :param campo: Tipo de campo de entrada donde ocurrió el evento.
        :param var: Variable asociada al campo de entrada.
        :param entry: Campo de entrada donde se produjo el evento.
        """
        if campo == "nom":
            if var.get() == "":
                entry.insert(0, "Escriba el nombre del artículo")
                entry.config(foreground="grey")
        elif campo == "cant":
            if var.get() == "":
                entry.insert(0, "Escriba un valor numérico")
                entry.config(foreground="grey")
        elif campo == "precio":
            if var.get() == "":
                entry.insert(0, "Escriba un valor numérico")
                entry.config(foreground="grey")
        elif campo == "descrip":
            if var.get() == "":
                entry.insert(0, "Agregue una breve descrip. del art.")
                entry.config(foreground="grey")


# ---------------------Clases que contienen métodos para base de datos--------------------------------

try:
    db = SqliteDatabase(
        "base_stock.db"
    )  # Creo el objeto que indica el tipo y nombre de bd a la cual me voy a conectar (si no existe la crea).
except:
    print("No se pudo crear la base de datos")


class BaseModel(Model):
    """
    Clase que establece a que base de datos me conecto y su tipo.
    """

    class Meta:

        database = db  # Indico a que base me conecto y su tipo.


class Componentes(BaseModel):
    """
    Clase asociada a la tabla de la base de datos, y donde defino sus atributos (campos).
    """

    nombre = CharField()
    cantidad = CharField()
    precio = CharField()
    descripcion = CharField()


class BaseDatos:
    """
    Clase que contiene métodos para conectarme a la base de datos, y para manejar los registros de la misma.
    """

    def __init__(self):
        """
        Constructor para crear, conectarme, y agregar una tabla a la base de datos.
        """
        self.con = db
        self.con.connect()  # Me conecto a la bd.
        self.con.create_tables([Componentes])  # Creo la tabla Componentes.

    def agregar_db(self, nombre, cantidad, precio, descripcion):
        """
        Método para agregar una fila de datos (registro) a la tabla.

        :param nombre: Nombre del componente.
        :param cantidad: Cantidad del componente.
        :param precio: Precio del componente.
        :param descripcion: Descripción del componente.
        """
        comp = Componentes()  # Creo un objeto (registro) de la clase Componentes.

        # Le asigno los valores ingresados a cada atributo(campo) del objeto.
        comp.nombre = nombre
        comp.cantidad = cantidad
        comp.precio = precio
        comp.descripcion = descripcion

        try:
            comp.save()  # Guardo el registro en la tabla.
        except:
            print("No se pudo guardar el registro")

    def eliminar_db(self, nombre):
        """
        Método para eliminar una fila de datos (registro) de la tabla
        usando como referencia el campo **Nombre**.

        :param nombre: Nombre del componente.
        """
        reg_borrar = Componentes.get(Componentes.nombre == nombre)

        try:
            reg_borrar.delete_instance()  # Borro el registro de la tabla.
        except:
            print("No se pudo eliminar el registro")

    def leer_db(self, nombre):
        """
        Método para seleccionar una o varias filas de la tabla usando como referencia el campo **Nombre**.

        :param nombre: Nombre del componente.

        :returns: Fila/s encontrada/s de acuerdo a la referencia.
        """
        if nombre == None:
            rows = Componentes.select()
        else:
            rows = Componentes.select().where(Componentes.nombre == nombre)

        return rows

    def actualizar_db(self, nombre, param, data2mod):
        """
        Método para actualizar uno o varios campos de una fila de la tabla.

        :param nombre: Nombre del componente.
        :param param: Nuevo valor del campo.
        :param data2mod: Campo a modificar.
        """
        if data2mod == "cant":
            reg_actualizar = Componentes.update(cantidad=param).where(
                Componentes.nombre == nombre
            )

        elif data2mod == "prec":
            reg_actualizar = Componentes.update(precio=param).where(
                Componentes.nombre == nombre
            )

        elif data2mod == "descrip":
            reg_actualizar = Componentes.update(descripcion=param).where(
                Componentes.nombre == nombre
            )

        try:
            reg_actualizar.execute()  # Actualizo el registro.
        except:
            print("No se pudo actualizar el registro")


class Crud(BaseDatos):
    """
    Clase que contiene métodos para el manejo de los datos ingresados.
    """

    def __init__(self):
        """
        Constructor que hereda el correspondiente a la clase ``BaseDatos()``,
        y que además crea un objeto ``Validacion()`` para comprobar los campos de entrada.
        """
        super(Crud, self).__init__()
        self.obj_val = Validacion()

    def agreg(self, nombre, cantidad, precio, descripcion, tree):
        """
        Método para agregar un nuevo componente.

        :param nombre: Nombre del componente.
        :param cantidad: Cantidad del componente.
        :param precio: Precio del componente.
        :param descripcion: Descripción del componente.
        :param tree: Treeview de la interfaz.

        :returns: ``"campos vacíos"`` si no se completaron todos los campos.
        :returns: ``"existe"`` si el componente que se quiere ingresar ya se encontraba cargado.
        :returns: ``"cargado"`` si el componente fue ingresado exitosamente.

        Si en algunos de los campos se ingresó un dato inválido (no cumple regex)
        se generará una excepción.
        """
        nom = nombre.get()
        cant = cantidad.get()
        prec = precio.get()
        descrip = descripcion.get()

        # Chequeo que los campos esten completos.
        if (
            self.obj_val.empty_entry(nom, "nom")
            and self.obj_val.empty_entry(cant, "cant")
            and self.obj_val.empty_entry(prec, "prec")
            and self.obj_val.empty_entry(descrip, "descrip")
        ):
            # Valido los campos con regex.
            if (
                self.obj_val.val_entry(nom, "nom")
                and self.obj_val.val_entry(cant, "cant")
                and self.obj_val.val_entry(prec, "prec")
                and self.obj_val.val_entry(descrip, "descrip")
            ):
                if self.leer_db(nom):
                    return "existe"
                else:
                    self.agregar_db(nom, cant, prec, descrip)
                    tree.insert(
                        "",
                        "end",
                        values=(nom, int(cant), float(prec), descrip),
                    )
                    return "cargado"
            else:
                raise ValueError(
                    "campos incorrectos"
                )  # Si se ingresó un dato inválido genero una excepción.
        else:
            return "campos vacios"

    def elim(self, nombre):
        """
        Método para eliminar un componente ingresado (lo busco por el nombre).

        :param nombre: Nombre del componente.

        :returns: ``"campo vacio"`` si no se ingresó ningún nombre.
        :returns: ``"no encontrado"`` si el componente a eliminar no se encuentra ingresado.
        :returns: ``"eliminado"`` si el componente fue eliminado exitosamente.
        """
        nom = nombre.get()

        # Chequeo que el campo nombre no esté vacío.
        if self.obj_val.empty_entry(nom, "nom"):

            # Chequeo si el artículo a eliminar existe.
            if self.leer_db(nom):
                self.eliminar_db(nom)
                return "eliminado"
            else:
                return "no encontrado"
        else:
            return "campo vacio"

    def modif(self, nombre, cantidad, precio, descripcion):
        """
        Método para modificar un componente ingresado (lo busco por el nombre).

        :param nombre: Nombre del componente.

        :returns: ``"campo vacio"`` si no se ingresó ningún nombre.
        :returns: ``"no existe"`` si el componente a modificar no se encuentra ingresado.
        :returns: ``"modificado"`` si el componente fue modificado exitosamente.

        Si en algunos de los campos se ingresó un dato inválido (no cumple regex)
        se generará una excepción.
        """
        global flag_e
        global flag_c
        global flag_p
        global flag_d

        nom = nombre.get()
        cant = cantidad.get()
        prec = precio.get()
        descrip = descripcion.get()

        # Chequeo que el campo nombre no esté vacío.
        if self.obj_val.empty_entry(nom, "nom"):

            # Chequeo si el artículo a modificar existe.
            if self.leer_db(nom):

                # Si el campo cantidad no está vacío y cumple con el patrón de regex
                # se pondrá en '1' el flag_c (dato válido para actualizar).
                if self.obj_val.empty_entry(cant, "cant"):
                    if self.obj_val.val_entry(cant, "cant"):
                        flag_c = 1
                    else:
                        flag_e = 1

                # Si el campo precio no está vacío y cumple con el patrón de regex
                # se pondrá en '1' el flag_p (dato válido para actualizar).
                if self.obj_val.empty_entry(prec, "prec"):
                    if self.obj_val.val_entry(prec, "prec"):
                        flag_p = 1
                    else:
                        flag_e = 1

                # Si el campo descripción no está vacío y cumple con el patrón de regex
                # se pondrá en '1' el flag_p (dato válido para actualizar).
                if self.obj_val.empty_entry(descrip, "descrip"):
                    if self.obj_val.val_entry(descrip, "descrip"):
                        flag_d = 1
                    else:
                        flag_e = 1

                # Si no hubo error en la validación de datos (flag_e == 0) se actualizarán
                # los datos que hayan sido ingresados en los campos correspondientes.
                if flag_e == 0:
                    if flag_c:
                        self.actualizar_db(nom, cant, "cant")
                        flag_c = 0
                    if flag_p:
                        self.actualizar_db(nom, prec, "prec")
                        flag_p = 0
                    if flag_d:
                        self.actualizar_db(nom, descrip, "descrip")
                        flag_d = 0

                    return "modificado"

                # Si hubo error en la validación de datos (flag == 1)
                # no se actualizará ningun campo y se informará del error al usuario.
                if flag_e:
                    flag_e = 0
                    raise ValueError(
                        "campos incorrectos"
                    )  # Si se ingresó un dato inválido genero una excepción.
            else:
                return "no existe"
        else:
            return "campo vacio"

    def consulta(self, nombre, tree):
        """
        Método para consultar los datos de un componente en particular (lo busco por el nombre).

        :param nombre: Nombre del componente.

        :returns: ``"campo vacio"`` si no se ingresó ningún nombre.
        :returns: ``"no encontrado"`` si el componente a consultar no se encuentra ingresado.
        """
        nom = nombre.get()

        # Chequeo que el campo nombre no esté vacío.
        if self.obj_val.empty_entry(nom, "nom"):

            # Chequeo si el artículo a consultar existe.
            if self.leer_db(nom):
                data_from_db = self.leer_db(nom)

                # Borro todas las filas del treeview para mostrar solo el artículo consultado.
                tree.delete(*tree.get_children())
                for row in data_from_db:
                    tree.insert(
                        "",
                        "end",
                        text=str(row.id),
                        values=(
                            row.nombre,
                            int(row.cantidad),
                            float(row.precio),
                            row.descripcion,
                        ),
                    )
            else:
                return "no encontrado"
        else:
            return "campo vacio"

    def mostrar_cat(self, tree):
        """
        Método que muestra el catálogo completo de componentes cargados hasta el momento.

        :param tree: Treeview de la interfaz.
        """
        data_from_db = self.leer_db(None)
        tree.delete(*tree.get_children())
        for row in data_from_db:
            tree.insert(
                "",
                "end",
                text=str(row.id),
                values=(
                    row.nombre,
                    int(row.cantidad),
                    float(row.precio),
                    row.descripcion,
                ),
            )
