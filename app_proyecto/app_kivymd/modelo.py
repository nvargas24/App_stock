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

    def leer_db(self, nombre=None, descrip=None):
        """
        Método para seleccionar una o varias filas de la tabla usando como referencia
        el campo **Nombre** y/o el campo **Descripción**.

        :param nombre: Nombre del componente.
        :param descrip: Descripcion del componente.

        :returns: Fila/s encontrada/s de acuerdo a la referencia.
        """

        if nombre == None and descrip == None:
            rows = Componentes.select()
        elif nombre != None and descrip == None:
            rows = Componentes.select().where(Componentes.nombre == nombre)
        elif nombre == None and descrip != None:
            rows = Componentes.select().where(Componentes.descripcion == descrip)
        elif nombre != None and descrip != None:
            rows = Componentes.select().where(
                (Componentes.nombre == nombre) & (Componentes.descripcion == descrip)
            )

        return rows

    def actualizar_db(self, nombre, cant, prec, descrip):
        """
        Método para actualizar uno o varios campos de una fila de la tabla.

        :param nombre: Nombre del componente.
        :param cant: Nuevo valor del campo cantidad (si existe un dato válido).
        :param prec: Nuevo valor del campo precio (si existe un dato válido).
        :param descrip: Nuevo valor del campo descripción (si existe un dato válido).
        """

        if flag_c == 1:  # Si existe un dato cantidad válido.
            reg_actualizar = Componentes.update(cantidad=cant).where(
                Componentes.nombre == nombre
            )
            try:
                reg_actualizar.execute()  # Actualizo el registro.
            except:
                print("No se pudo actualizar el registro")

        if flag_p == 1:  # Si existe un dato precio válido.
            reg_actualizar = Componentes.update(precio=prec).where(
                Componentes.nombre == nombre
            )
            try:
                reg_actualizar.execute()  # Actualizo el registro.
            except:
                print("No se pudo actualizar el registro")

        if flag_d == 1:  # Si existe un dato descripción válido.
            reg_actualizar = Componentes.update(descripcion=descrip).where(
                Componentes.nombre == nombre
            )
            try:
                reg_actualizar.execute()  # Actualizo el registro.
            except:
                print("No se pudo actualizar el registro")


# ---------------------Clase que contienen métodos para manejo de datos ingresados--------------------------------
class Crud(BaseDatos):
    """
    Clase que contiene métodos para el manejo de los datos ingresados.
    """

    def __init__(self):
        """
        Constructor que hereda el correspondiente a la clase ``BaseDatos()``,
        y que además crea un objeto ``Validacion()`` para comprobar los campos de entrada.
        También hereda de la clase ``Sujeto()`` para el manejo de observadores.
        """
        super().__init__()
        self.obj_val = Validacion()

    def agreg(self, nombre, cantidad, precio, descripcion):
        """
        Método para agregar un nuevo componente.

        :param nombre: Nombre del componente.
        :param cantidad: Cantidad del componente.
        :param precio: Precio del componente.
        :param descripcion: Descripción del componente.

        :returns: ``"Campos vacios"`` si no se completaron todos los campos.
        :returns: ``"Ya existe el articulo"`` si el componente que se quiere ingresar ya se encontraba cargado.
        :returns: ``"Nuevo articulo cargado"`` si el componente fue ingresado exitosamente.

        Si en algunos de los campos se ingresó un dato inválido (no cumple regex)
        se generará una excepción.
        """
        nom = nombre.text
        cant = cantidad.text
        prec = precio.text
        descrip = descripcion.text

        # Chequeo que el campo nombre, cantidad, precio y descripción no se encuentren vacíos.
        if not (
            self.obj_val.empty_entry(nom, "nom")
            and self.obj_val.empty_entry(cant, "cant")
            and self.obj_val.empty_entry(prec, "prec")
            and self.obj_val.empty_entry(descrip, "descrip")
        ):
            return ["Error en la operación", "No se han completado todos los campos"]

        # Si se ingresó un dato inválido genero una excepción.
        if not (
            self.obj_val.val_entry(nom, "nom")
            and self.obj_val.val_entry(cant, "cant")
            and self.obj_val.val_entry(prec, "prec")
            and self.obj_val.val_entry(descrip, "descrip")
        ):
            raise ValueError("Campos incorrectos")

        # Cargo en la base de datos y notifico al observador
        if not self.leer_db(nom):
            self.agregar_db(nom, cant, prec, descrip)
            return ["Operación exitosa", "Artículo cargado correctamente"]

        return ["Error en la operación", "Artículo ya existente"]

    def elim(self, nombre):
        """
        Método para eliminar un componente ingresado (lo busco por el nombre).

        :param nombre: Nombre del componente.

        :returns: ``"Campo vacio"`` si no se ingresó ningún nombre.
        :returns: ``"Articulo no encontrado"`` si el componente a eliminar no se encuentra ingresado.
        :returns: ``"Articulo eliminado"`` si el componente fue eliminado exitosamente.
        """
        nom = nombre.text

        # Chequeo que el campo nombre no esté vacío.
        if not self.obj_val.empty_entry(nom, "nom"):
            return ["Error en la operación", "No se ha ingresado ningun nombre"]

        # Chequeo si el artículo a eliminar existe.
        if not self.leer_db(nom):
            return ["Error en la operación", "Artículo no encontrado"]

        # Elimino de la base de datos y notifico al observador.
        self.eliminar_db(nom)
        return ["Operación exitosa", "Artículo eliminado correctamente"]

    def modif(self, nombre, cantidad, precio, descripcion):
        """
        Método para modificar un componente ingresado (lo busco por el nombre).

        :param nombre: Nombre del componente.
        :param cantidad: Cantidad del componente.
        :param precio: Precio del componente.
        :param descripcion: Descripción del componente.

        :returns: ``"Campo vacio"`` si no se ingresó ningún nombre.
        :returns: ``"Articulo no existe"`` si el componente a modificar no se encuentra ingresado.
        :returns: ``"Articulo sin modificar"`` si no se ingresó ningún parámetro a modificar del componente.
        :returns: ``"Articulo modificado"`` si el componente fue modificado exitosamente.

        Si en algunos de los campos se ingresó un dato inválido (no cumple regex)
        se generará una excepción.
        """
        global flag_e
        global flag_c
        global flag_p
        global flag_d

        nom = nombre.text
        cant = cantidad.text
        prec = precio.text
        descrip = descripcion.text

        # Chequeo que el campo nombre no esté vacío.
        if not self.obj_val.empty_entry(nom, "nom"):
            return ["Error en la operación", "No se ha ingresado ningun nombre"]

        # Chequeo si el artículo a modificar existe.
        if not self.leer_db(nom):
            return ["Error en la operación", "Artículo no encontrado"]

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
        if not flag_e:
            # Si no se ingresó ningún dato a modificar.
            if not (flag_c or flag_p or flag_d):
                return ["Error en la operación", "No se ha modificado el artículo"]

            # Si se ingresó un dato modifico el componente y notifico al observador.
            self.actualizar_db(nom, cant, prec, descrip)

            flag_c = 0
            flag_p = 0
            flag_d = 0

            return ["Operación exitosa", "Artículo modificado correctamente"]

        # Si hubo error en la validación de datos (flag == 1)
        # no se actualizará ningun campo y se informará del error al usuario.
        flag_e = 0  # Como ya se detecto un error se lo vuelve a setear para la siguiente operación.

        raise ValueError(
            "Campos incorrectos"
        )  # Si se ingresó un dato inválido genero una excepción.

    def consulta(self, nombre, descrip, window_consulta):
        """
        Método para consultar los datos de un componente en particular (lo busco por el nombre y/o descripción).

        :param nombre: Nombre del componente.
        :param descrip: Descripción del componente.
        :param window_consulta: Objeto de clase ``WindowConsulta()``.

        :returns: ``"Campo vacios"`` si no se ingresó ningún nombre y/o descripción.
        :returns: ``"Articulo no encontrado por nombre"`` si el componente consultado por nombre no se encuentra ingresado.
        :returns: ``"Articulo no encontrado por descripcion"`` si el componente consultado por descripción no se encuentra ingresado.
        :returns: ``"Articulo no encontrado"`` si el componente consultado por nombre y descripción no se encuentra ingresado.
        """
        nom = nombre
        descrip = descrip

        # Búsqueda por nombre.
        if self.obj_val.empty_entry(nom, "nom") and not self.obj_val.empty_entry(
            descrip, "descrip"
        ):
            print("busqueda por nombre")
            data_from_db = self.leer_db(nom, None)
            if not data_from_db:
                return "Artículo no encontrado por nombre"

        # Búsqueda por descripción.
        elif not self.obj_val.empty_entry(nom, "nom") and self.obj_val.empty_entry(
            descrip, "descrip"
        ):
            print("busqueda por descripcion")
            data_from_db = self.leer_db(None, descrip)
            if not data_from_db:
                return "Artículo no encontrado por descripción"

        # Búsqueda por nombre y descripción.
        elif self.obj_val.empty_entry(nom, "nom") and self.obj_val.empty_entry(
            descrip, "descrip"
        ):
            print("busqueda por nombre y descripcion")
            data_from_db = self.leer_db(nom, descrip)
            if not data_from_db:
                return "Artículo no encontrado"

        else:
            return "Campos vacíos"

        # Borro las filas de la tabla que contiene la ventana de Consulta.
        window_consulta.delete()

        # Cargo la tabla con la/s fila/s encontradas de acuerdo a la búsqueda.
        for row in data_from_db:
            window_consulta.add_frame(
                str(row.id),
                row.nombre,
                row.cantidad,
                row.precio,
                row.descripcion,
            )

    # NO ES NECESARIO PASAR EL PARAMETRO SDE WINDOWS_MAIN AL DECORADOR
    # YA QUE SE MUESTRA EN LA VENTANA DE CATALOGO
    def mostrar_cat(self, window_consulta):
        """
        Método que muestra el catálogo completo de componentes cargados hasta el momento.

        :param window_consulta: Objeto de clase ``WindowConsulta()``.

        :returns: **x_nom**, lista que almacena los nombres de cada componente registrado.
        :returns: **y_cant**, lista que almacena las cantidades de cada componente registrado.
        """

        x_nom = []  # Lista que almacena los nombres de cada componente cargado.
        y_cant = []  # Lista que almacena las cantidades de cada componente cargado.

        data_from_db = self.leer_db()

        # Cargo la tabla de la ventana Consulta con todos los registros almacenados en la bd.
        for row in data_from_db:
            window_consulta.add_frame(
                str(row.id),
                row.nombre,
                row.cantidad,
                row.precio,
                row.descripcion,
            )

            x_nom.append(row.nombre)
            y_cant.append(row.cantidad)

        return x_nom, y_cant
