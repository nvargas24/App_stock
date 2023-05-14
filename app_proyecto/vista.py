"""
vista.py:
    Módulo encargado de generar la interfaz gráfica de la app. 
"""
__author__ = "Diego Calderón, Nahuel Vargas"
__maintainer__ = "Diego Calderón, Nahuel Vargas"
__email__ = "diegoacalderon994@gmail.com, nahuvargas24@gmail.com"
__copyright__ = "Copyright 2023"
__version__ = "0.0.2"

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

from Qt.window_main import *
from Qt.window_agregar import *
from Qt.window_eliminar import *
from Qt.window_modificar import *
from Qt.window_consulta import *

from modelo import Crud
import random


# -------- Clases para widgets -------- #
class Opciones:
    """
    Clase que establece qué ventanas mostrar
    """

    def show_win_agregar(self):
        """
        Método para setear y mostrar ventana de **Agregar Artículo**.
        """
        self.close_all_window()
        self.window_agregar.setWindowTitle("Agregar")
        self.window_agregar.show()
        # Muevo la ventana a la derecha de la ventana principal.
        self.window_agregar.move(self.geometry().right() + 10, self.geometry().top())
        self.opened_windows.append(self.window_agregar)

        # Limpio celdas.
        self.window_agregar.ui.in_nombre.clear()
        self.window_agregar.ui.in_cant.clear()
        self.window_agregar.ui.in_precio.clear()
        self.window_agregar.ui.in_descrip.clear()
        self.window_agregar.ui.notificacion.clear()

    def show_win_eliminar(self):
        """
        Método para setear y mostrar ventana de **Eliminar Artículo**.
        """
        self.close_all_window()
        self.window_eliminar.setWindowTitle("Eliminar")
        self.window_eliminar.show()
        # Muevo la ventana a la derecha de la ventana principal.
        self.window_eliminar.move(self.geometry().right() + 10, self.geometry().top())
        self.opened_windows.append(self.window_eliminar)

        # Limpio celdas.
        self.window_eliminar.ui.in_nombre.clear()
        self.window_eliminar.ui.notificacion.clear()

    def show_win_modificar(self):
        """
        Método para setear y mostrar ventana de **Modificar Artículo**.
        """
        self.close_all_window()
        self.window_modificar.setWindowTitle("Modificar")
        self.window_modificar.show()
        # Muevo la ventana a la derecha de la ventana principal.
        self.window_modificar.move(self.geometry().right() + 10, self.geometry().top())
        self.opened_windows.append(self.window_modificar)

        # Limpio celdas.
        self.window_modificar.ui.in_nombre.clear()
        self.window_modificar.ui.in_cant.clear()
        self.window_modificar.ui.in_precio.clear()
        self.window_modificar.ui.in_descrip.clear()
        self.window_modificar.ui.notificacion.clear()

    def show_win_consultar(self):
        """
        Método para setear y mostrar ventana de **Consultar Artículo**.
        """
        self.close_all_window()
        self.window_consulta.setWindowTitle("Consulta")
        self.window_consulta.show()
        # Muevo la ventana a la derecha de la ventana principal.
        self.window_consulta.move(self.geometry().right() + 10, self.geometry().top())
        self.opened_windows.append(self.window_consulta)

        # Limpio celdas.
        self.window_consulta.ui.in_nombre.clear()
        self.window_consulta.ui.in_descrip.clear()
        self.window_consulta.ui.notificacion.clear()

        self.window_consulta.full_cat()  # Obtengo catálogo completo de la bd y lo muestra al abrir la ventana.

    def close_all_window(self):
        """
        Método para cerrar todas las ventanas secundarias abiertas.
        """
        for window in self.opened_windows:
            window.close()
        self.opened_windows = []  # Vacio la lista de ventanas abiertas.


# --- Clase para interactuar con gráfico de torta --- #
class Canvas_grafica(FigureCanvas):
    """
    Clase que contiene métodos para actualizar y dar estilo al gráfico de torta.
    """

    def __init__(self):
        """
        Constructor que hereda el correspondiente a la clase ``FigureCanvas()``,
        y que además crea un gráfico matplotlib en blanco.
        """
        # Asigno un espacio para ubicar el gráfico de matplotlib usando Canvas.
        self.fig, self.ax = plt.subplots(
            1, dpi=70, figsize=(12, 12), sharey=True, facecolor="none"
        )
        super().__init__(self.fig)

    def upgrade_graph(self, nombre, cantidad):
        """
        Método para actualizar nombres y cantidades en gráfico de torta.

        :param nombre: Nombre del componente.
        :param cantidad: Cantidad del componente.
        """
        # Parámetros para nuevo gráfico.
        self.nombres = nombre
        self.tamanio = cantidad
        self.colores = []
        self.explotar = []

        # Asigno color aleatorio claros segun la cantidad de artículos disponibles.
        for i in range(len(self.nombres)):
            r = random.randint(150, 255)
            g = random.randint(150, 255)
            b = random.randint(150, 255)
            self.colores.append("#%02x%02x%02x" % (r, g, b))
            self.explotar.append(0.05)

        # Borro gráfico antiguo.
        self.ax.clear()
        # Pasaje de porcentaje a valor real en bd.
        valor_real = lambda pct: "{:.0f}".format(
            (pct * sum(list(map(int, self.tamanio)))) / 100
        )
        # Asigno nuevos parámetros a gráfico.
        self.ax.pie(
            self.tamanio,
            explode=self.explotar,
            labels=self.nombres,
            colors=self.colores,
            autopct=valor_real,
            pctdistance=0.8,
            shadow=True,
            startangle=90,
            radius=1.2,
            labeldistance=1.1,
            textprops={"fontsize": 14},
        )

        self.ax.axis("equal")
        # Actualizo gráfico.
        self.draw()


# -------- Clases para ventanas -------#
class MainWindow(QMainWindow, Opciones):
    """
    Clase que contiene métodos para la interacción en la ventana principal.
    """

    def __init__(self, parent=None):
        """
        Constructor que hereda el correspondiente a la clase ``QMainWindow()`` para acceder a widgets.
        Tambíen hereda de la clase ``Opciones()`` para acceder a las ventanas secundarias.
        """
        super().__init__()
        # Creo objeto de la clase en QT para crear widgets.
        self.ui = Ui_MainWindow()
        # Se acccede al metodo setupUi que crea widgets.
        self.ui.setupUi(self)
        # Defino un objeto de clase Crud() para el manejo de datos.
        self.obj_f = Crud()

        # Creo objetos window para acceder a las ventanas secundarias y estas a la principal.
        self.window_agregar = WindowAgregar(self.obj_f)
        self.window_eliminar = WindowEliminar(self.obj_f)
        self.window_modificar = WindowModificar(self.obj_f)
        self.window_consulta = WindowConsulta(self.obj_f, self)

        # Lista de ventanas abiertas.
        self.opened_windows = []

        # Creo objeto de clase Canvas_grafica() para crear y actualizar gráfico de matplotlib.
        self.grafica = Canvas_grafica()
        self.ui.grafica_torta.addWidget(self.grafica)

        # Obtengo y muestro catálogo completo en gráfico de torta al iniciar.
        self.window_consulta.full_cat()

        # Callback de widgets Button para abrir ventanas secundarias.
        self.ui.btn_agregar.clicked.connect(self.show_win_agregar)
        self.ui.btn_eliminar.clicked.connect(self.show_win_eliminar)
        self.ui.btn_modificar.clicked.connect(self.show_win_modificar)
        self.ui.btn_consultar.clicked.connect(self.show_win_consultar)


class WindowAgregar(QDialog):
    """
    Clase que contiene métodos para la interacción en la ventana **Agregar Artículo**.
    """

    def __init__(self, obj_f):
        """
        Constructor que hereda el correspondiente a la clase ``QDialog()`` para acceder a widgets.

        :param obj_f: Objeto de clase ``Crud()``.
        """
        super().__init__()
        # Creo objeto de la clase en QT para crear widgets.
        self.ui = Ui_Agregar()
        # Se acccede al método setupUi que crea widgets.
        self.ui.setupUi(self)
        # Cedo acceso a objeto Crud desde cualquier método de esta clase.
        self.obj_f = obj_f

        # Callback de widgets Button
        self.ui.btn_aceptar.clicked.connect(self.new_load)
        self.ui.btn_cancelar.clicked.connect(self.close)

    def new_load(self):
        """
        Método para agregar un nuevo artículo.
        """
        try:
            mje = self.obj_f.agreg(
                self.ui.in_nombre,
                self.ui.in_cant,
                self.ui.in_precio,
                self.ui.in_descrip,
            )
            # Informo en la ventana el resultado de la operacíon realizada.
            self.ui.notificacion.setText(mje)
        except ValueError as mje:
            # Informo en la ventana la excepción.
            self.ui.notificacion.setText(str(mje))


class WindowEliminar(QDialog):
    """
    Clase que contiene métodos para la interacción en la ventana **Eliminar Artículo**.
    """

    def __init__(self, obj_f):
        """
        Constructor que hereda el correspondiente a la clase ``QDialog()`` para acceder a widgets.

        :param obj_f: Objeto de clase ``Crud()``.
        """
        super().__init__()
        # Creo objeto de la clase en QT para crear widgets.
        self.ui = Ui_Eliminar()
        # Se acccede al método setupUi que crea widgets.
        self.ui.setupUi(self)
        # Cedo acceso a objeto Crud desde cualquier método de esta clase.
        self.obj_f = obj_f

        # Callback de widgets Button.
        self.ui.btn_aceptar.clicked.connect(self.delete)
        self.ui.btn_cancelar.clicked.connect(self.close)

    def delete(self):
        """
        Método para eliminar un artículo existente.
        """
        mje = self.obj_f.elim(self.ui.in_nombre)

        # Informo en la ventana el resultado de la operacíon realizada.
        self.ui.notificacion.setText(mje)


class WindowModificar(QDialog):
    """
    Clase que contiene métodos para la interacción en la ventana **Modificar Artículo**.
    """

    def __init__(self, obj_f):
        """
        Constructor que hereda el correspondiente a la clase ``QDialog()`` para acceder a widgets.

        :param obj_f: Objeto de clase ``Crud()``.
        """
        super().__init__()
        # Creo objeto de la clase en QT para crear widgets.
        self.ui = Ui_Modificar()
        # Se acccede al método setupUi que crea widgets.
        self.ui.setupUi(self)
        # Cedo acceso a objeto Crud desde cualquier método de esta clase.
        self.obj_f = obj_f

        # Callback de widgets Button.
        self.ui.btn_aceptar.clicked.connect(self.modificated)
        self.ui.btn_cancelar.clicked.connect(self.close)

    def modificated(self):
        """
        Método para modificar un artículo existente.
        """
        try:
            mje = self.obj_f.modif(
                self.ui.in_nombre,
                self.ui.in_cant,
                self.ui.in_precio,
                self.ui.in_descrip,
            )
            # Informo en la ventana el resultado de la operacíon realizada.
            self.ui.notificacion.setText(mje)
        except ValueError as mje:
            # Informo en la ventana la excepción.
            self.ui.notificacion.setText(str(mje))


class WindowConsulta(QWidget):
    """
    Clase que contiene métodos para la interacción en la ventana **Consultar Artículo**.
    """

    def __init__(self, obj_f, obj_win_main):
        """
        Constructor que hereda el correspondiente a la clase ``QWidget()`` para acceder a widgets.

        :param obj_f: Objeto de clase ``Crud()``.
        :param obj_win_main: Objeto de clase ``MainWindow()`` para acceder a atributos/métodos de ventana principal.
        """
        super().__init__()
        # Creo objeto de la clase en QT para crear widgets.
        self.ui = Ui_Consulta()
        # Se acccede al método setupUi que crea widgets.
        self.ui.setupUi(self)
        # Cedo acceso a objeto Crud desde cualquier método de esta clase.
        self.obj_f = obj_f
        # Cedo acceso a objeto MainWindow desde cualquier método de esta clase.
        self.obj_win_main = obj_win_main

        # Callback de widgets Button.
        self.ui.btn_buscar.clicked.connect(self.search)
        self.ui.btn_cat_full.clicked.connect(self.full_cat)
        self.ui.btn_volver.clicked.connect(self.close)

    def insert(self, id, nom, cant, prec, descrip):
        """
        Método para agregar un artículo nuevo en la tabla.
        """
        self.frame = []
        self.frame.append((id, nom, cant, prec, descrip))

        fila = 0
        for registro in self.frame:
            columna = 0
            # Creo fila nueva cada vez que se lee un nuevo frame (todos los parámetros de un artículo).
            self.ui.catalogo_list.insertRow(fila)
            for elemento in registro:
                # Cargo cada parámetro en la columna correspondiente, por orden.
                self.ui.catalogo_list.setItem(fila, columna, QTableWidgetItem(elemento))
                columna += 1

    def delete(self):
        """
        Método para limpiar celdas de la tabla.
        """
        self.ui.catalogo_list.clearContents()

    def search(self):
        """
        Método para buscar y mostrar artículo/s en la tabla.
        """
        mje = self.obj_f.consulta(self.ui.in_nombre, self.ui.in_descrip, self)

        # Informo en la ventana el resultado de la operacíon realizada.
        self.ui.notificacion.setText(mje)

    def full_cat(self):
        """
        Método para mostrar todos los artículos en la tabla.
        """
        self.ui.catalogo_list.clearContents()
        # Actualizo tabla y gráfico de torta.
        self.obj_f.mostrar_cat(self, self.obj_win_main)
