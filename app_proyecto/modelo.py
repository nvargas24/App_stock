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
from observador import Sujeto
import datetime
import pandas as pd
import matplotlib.pyplot as plt


# --------------------Variables---------------------------------
# Flag utilizado para informar si hubo un error en la validación de los datos de un campo a actualizar.
flag_e = 0
# Flag utilizado para informar que existe un dato válido para actualizar en el campo cantidad.
flag_c = 0
# Flag utilizado para informar que existe un dato válido para actualizar en el campo precio.
flag_p = 0
# Flag utilizado para informar que existe un dato válido para actualizar en el campo descripción.
flag_d = 0

# ---------------------Decoradores-------------------------------
def decorador_add(metodo):
    def envoltura(*args):
        archivo = open("registro_log.txt", "a", encoding="utf-8")
        archivo.write(
            "Se ingresó un nuevo registro "
            + "Fecha: "
            + str(datetime.datetime.today().strftime("%d/%m/%y"))
            + " Hora: "
            + str(datetime.datetime.today().strftime("%H:%M:%S"))
            + "\n"
        )
        metodo(*args)

    return envoltura


def decorador_del(metodo):
    def envoltura(*args):
        archivo = open("registro_log.txt", "a", encoding="utf-8")
        archivo.write(
            "Se eliminó un registro "
            + "Fecha: "
            + str(datetime.datetime.today().strftime("%d/%m/%y"))
            + " Hora: "
            + str(datetime.datetime.today().strftime("%H:%M:%S"))
            + "\n"
        )
        metodo(*args)

    return envoltura


def decorador_mod(metodo):
    def envoltura(*args):
        archivo = open("registro_log.txt", "a", encoding="utf-8")
        archivo.write(
            "Se modificó un registro "
            + "Fecha: "
            + str(datetime.datetime.today().strftime("%d/%m/%y"))
            + " Hora: "
            + str(datetime.datetime.today().strftime("%H:%M:%S"))
            + "\n"
        )
        metodo(*args)

    return envoltura


def decorador_mostrar(metodo):
    def envoltura(*args):
        # Si args[2] == True (graf=True) se muestra en consola una tabla de cada componente cargado con su respectiva cantidad
        # y se realiza un gráfico de torta a partir de dichos datos
        if len(args) == 3 and args[2] == True:
            x, y = metodo(*args)

            # Se calcula y se muestra en consola una tabla de componentes cargados con sus respectivas cantidades
            print("---" * 23)
            print("Lista de stock")
            dataset = {"Componente": x, "Cantidad": y}
            df = pd.DataFrame(dataset)
            print(df)
            print("---" * 23)

            # Se realiza un gráfico de torta del total de componentes cargados con sus respectivas cantidades
            df.groupby(["Componente"]).sum().plot(
                kind="pie",
                y="Cantidad",
                autopct=lambda p: "{:.0f}".format(p * sum(df["Cantidad"]) / 100),
                title="Stock total de componentes",
                legend=False,
            )
            plt.ylabel("")
            plt.show()

        else:
            metodo(*args)

    return envoltura


# ---------------------Clase que contienen métodos para eventos--------------------------------
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

    @decorador_add
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

    @decorador_del
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

    @decorador_mod
    def actualizar_db(self, nombre, cant, prec, descrip):
        """
        Método para actualizar uno o varios campos de una fila de la tabla.

        :param nombre: Nombre del componente.
        :param cant: Nuevo valor del campo cantidad(si existe un dato válido).
        :param cant: Nuevo valor del campo precio(si existe un dato válido).
        :param cant: Nuevo valor del campo descripción(si existe un dato válido).
        """

        if flag_c == 1:  # Si existe un dato "cantidad" válido
            reg_actualizar = Componentes.update(cantidad=cant).where(
                Componentes.nombre == nombre
            )
            
            try:
                reg_actualizar.execute()  # Actualizo el registro.
            except:
                print("No se pudo actualizar el registro")

        if flag_p == 1:  # Si existe un dato "precio" válido
            reg_actualizar = Componentes.update(precio=prec).where(
                Componentes.nombre == nombre
            )
            
            try:
                reg_actualizar.execute()  # Actualizo el registro.
            except:
                print("No se pudo actualizar el registro")

        if flag_d == 1:  # Si existe un dato "descripción" válido
            reg_actualizar = Componentes.update(descripcion=descrip).where(
                Componentes.nombre == nombre
            )
           
            try:
                reg_actualizar.execute()  # Actualizo el registro.
            except:
                print("No se pudo actualizar el registro")


# ---------------------Clase que contienen métodos para manejo de datos ingresados--------------------------------
class Crud(BaseDatos,Sujeto):
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

                    # Notifico al observador
                    self.notificar("agreg",nom,cant,prec,descrip)
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

                # Notifico al observador
                self.notificar("elim",nom)
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
                    if flag_c or flag_p or flag_d:  # Si se ingresó un dato a modificar
                        self.actualizar_db(nom, cant, prec, descrip)

                        # Notifico al observador
                        self.notificar("modif", nom, flag_c, cant, flag_p, prec, flag_d, descrip)

                        flag_c = 0
                        flag_p = 0
                        flag_d = 0

                        return "modificado"
                    else:
                        # No se completó ningún campo a modificar
                        return "sin modificar"

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

    @decorador_mostrar
    def mostrar_cat(self, tree, graf=False):
        """
        Método que muestra el catálogo completo de componentes cargados hasta el momento.

        :param tree: Treeview de la interfaz.
        :param graf: Indica si se requiere graficar o no el stock total de componentes cargados. Por defecto dicho parámetro será ``"False"``.

        :returns: ``x``,``y`` solo si se solicitó graficar el stock total de componentes cargados.
        """

        x = []  # Lista que almacena los nombres de cada componente cargado
        y = []  # Lista que almacena los cantidades de cada componente cargado

        data_from_db = self.leer_db(None)
        tree.delete(*tree.get_children())
        if graf == True:
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

                x.append(row.nombre)
                y.append(int(row.cantidad))

            return x, y

        else:
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