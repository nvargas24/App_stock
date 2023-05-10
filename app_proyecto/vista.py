"""
vista.py:
    Módulo encargado de generar la interfaz gráfica de la app. 
"""
__author__ = "Diego Calderón, Nahuel Vargas"
__maintainer__ = "Diego Calderón, Nahuel Vargas"
__email__ = "diegoacalderon994@gmail.com, nahuvargas24@gmail.com"
__copyright__ = "Copyright 2023"
__version__ = "0.0.2"

import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

from Qt.window_main import *
from Qt.window_agregar import *
from Qt.window_eliminar import *
from Qt.window_modificar import *
from Qt.window_consulta import *

from modelo import Crud
import random

#-------- Clases para widgets --------#
class Opciones():
    """
    Clase que establece que ventanas mostrar
    """
    def show_win_agregar(self,):
        """
        Método para setear y mostrar ventana de Agregar Articulo
        """
        self.close_all_window()
        self.window_agregar.setWindowTitle("Agregar")
        self.window_agregar.show()
        # Mueve la ventana a la derecha de la ventana principal
        self.window_agregar.move(self.geometry().right() + 10, self.geometry().top()) 
        self.opened_windows.append(self.window_agregar)

        # Limpia celdas
        self.window_agregar.ui.in_nombre.clear()
        self.window_agregar.ui.in_cant.clear()
        self.window_agregar.ui.in_precio.clear()
        self.window_agregar.ui.in_descrip.clear()
        self.window_agregar.ui.notificacion.clear()

    def show_win_eliminar(self,):
        """
        Método para setear y mostrar ventana de Eliminar Articulo
        """
        self.close_all_window()
        self.window_eliminar.setWindowTitle("Eliminar")
        self.window_eliminar.show()
        # Mueve la ventana a la derecha de la ventana principal
        self.window_eliminar.move(self.geometry().right() + 10, self.geometry().top()) 
        self.opened_windows.append(self.window_eliminar)

        # Limpia celdas
        self.window_eliminar.ui.in_nombre.clear()
        self.window_eliminar.ui.notificacion.clear()

    def show_win_modificar(self,):
        """
        Método para setear y mostrar ventana de Modficar Articulo
        """
        self.close_all_window()
        self.window_modificar.setWindowTitle("Modificar")
        self.window_modificar.show()
        # Mueve la ventana a la derecha de la ventana principal
        self.window_modificar.move(self.geometry().right() + 10, self.geometry().top()) 
        self.opened_windows.append(self.window_modificar)

        # Limpia celdas
        self.window_modificar.ui.in_nombre.clear()
        self.window_modificar.ui.in_cant.clear()
        self.window_modificar.ui.in_precio.clear()
        self.window_modificar.ui.in_descrip.clear()
        self.window_modificar.ui.notificacion.clear()

    def show_win_consultar(self,):
        """
        Método para setear y mostrar ventana de Consultar Articulo
        """
        self.close_all_window()
        self.window_consulta.setWindowTitle("Consulta")
        self.window_consulta.show()
        # Mueve la ventana a la derecha de la ventana principal
        self.window_consulta.move(self.geometry().right() + 10, self.geometry().top()) 
        self.opened_windows.append(self.window_consulta)

        # Limpia celdas
        self.window_consulta.ui.in_nombre.clear()
        self.window_consulta.ui.in_descrip.clear()
        self.window_consulta.ui.notificacion.clear()
        
        self.window_consulta.full_cat() #Obtiene catalogo completo de la DB y la muestra al abrir la ventana
    
    def close_all_window(self, ):
        """
        Método para cerrar todas las ventanas secundarias abiertas
        """
        for window in self.opened_windows:
            window.close()
        self.opened_windows = []  # vaciar la lista de ventanas abiertas

# --- Clase para iteractuar con grafico ---#
class Canvas_grafica(FigureCanvas):
    """
    Clase que contiene métodos para actualizar y dar estilo a grafico de torta
    """
    def __init__(self, ):
        """
        Constructor que hereda el correspondiente a la clase ``FigureCanvas()``,
        y que además crea un grafico matplotlib en blanco
        """
        # Asigno un espacio para ubicar el grafico de matplotlib usando Canvas
        self.fig, self.ax = plt.subplots(1, dpi=70, figsize=(12,12), sharey=True, facecolor='none')
        super().__init__(self.fig)

    def upgrade_graph(self, nombre, cantidad):
        """
        Método para actulizar nombres y valor cantidad en grafico de torta.

        :param nombre: Nombre del componente.
        :param cantidad: Cantidad del componente.
        """
        # Parametros para nuevo grafico
        self.nombres=nombre
        self.tamanio=cantidad
        self.colores=[]
        self.explotar=[]

        # Asigno color aleatorio claros segun la cantidad de articulos disponibles
        for i in range(len(self.nombres)):
            r = random.randint(150, 255)
            g = random.randint(150, 255)
            b = random.randint(150, 255)
            self.colores.append('#%02x%02x%02x' % (r, g, b))
            self.explotar.append(0.05)

        # Borro grafico viejo
        self.ax.clear()
        # Pasaje de porcentaje a valor real en bd
        valor_real = lambda pct: "{:.0f}".format((pct * sum(list(map(int, self.tamanio)))) / 100) 
        # Asigno nuevos parametros a grafico
        self.ax.pie(self.tamanio, explode=self.explotar, labels=self.nombres, colors=self.colores,
                    autopct=valor_real, pctdistance=0.8, shadow=True, startangle=90, radius=1.2, labeldistance=1.1, textprops={'fontsize': 18})

        self.ax.axis('equal')
        # Actualizo grafico
        self.draw() 

#-------- Clases para ventanas -------#
class MainWindow(QMainWindow, Opciones):
    """
    Clase que contiene métodos para la interaccion en la ventana principal.
    """
    def __init__(self, parent=None):
        """
        Constructor que hereda el correspondiente a la clase ''QMainWindow()'' para acceder widgets,
        y ''Opciones'' para acceder a las ventanas secundarias. Que además crea un objeto ''Crud()'' 
        para el manejo de datos.
        """
        super().__init__()
        # Creo objeto de la clase en QT para crear widgets
        self.ui = Ui_MainWindow() 
        # Se acccede al metodo setupUi que crea widgets
        self.ui.setupUi(self,)
        self.obj_f = Crud()  
        
        # Creo objetos window para acceder a las ventanas secundarias y estas a la principal
        self.window_agregar = WindowAgregar(self.obj_f)
        self.window_eliminar = WindowEliminar(self.obj_f)
        self.window_modificar = WindowModificar(self.obj_f)
        self.window_consulta = WindowConsulta(self.obj_f, self) 

        # Lista de ventanas abiertas
        self.opened_windows=[]

        # Creo objeto grafica para crear y actualizar grafico matplotlib
        self.grafica = Canvas_grafica()
        self.ui.grafica_torta.addWidget(self.grafica)

        # Obtengo y muestro catalogo completo en grafico de torta al iniciar
        self.window_consulta.full_cat()
        
        # Callback de widgets Button para abrir ventanas secundarias
        self.ui.btn_agregar.clicked.connect(self.show_win_agregar)
        self.ui.btn_eliminar.clicked.connect(self.show_win_eliminar)
        self.ui.btn_modificar.clicked.connect(self.show_win_modificar)
        self.ui.btn_consultar.clicked.connect(self.show_win_consultar)

class WindowAgregar(QDialog):
    """
    Clase que contiene métodos para la interaccion en la ventana Agregar.
    """
    def __init__(self, obj_f):
        """
        Constructor que hereda el correspondiente a la clase ''QDialog()'' para acceder widgets.
        :param obj_f: Objeto Crud.
        """
        super().__init__()
        # Creo objeto de la clase en QT para crear widgets
        self.ui = Ui_Agregar()
        # Se acccede al metodo setupUi que crea widgets
        self.ui.setupUi(self,)
        # Sedo accedo a objeto Crud desde cualquier metodo de esta clase
        self.obj_f = obj_f

        # Callback de widgets Button
        self.ui.btn_aceptar.clicked.connect(self.new_load)
        self.ui.btn_cancelar.clicked.connect(self.close)

    def new_load(self, ):
        """
        Método para agregar un nuevo articulo.
        """
        try:
            mje = self.obj_f.agreg(
                        self.ui.in_nombre, 
                        self.ui.in_cant, 
                        self.ui.in_precio, 
                        self.ui.in_descrip)
            # Informa en la ventana estado del nuevo articulo
            self.ui.notificacion.setText(mje)
        except (
            ValueError
        ) as mje:
            # Informa en la ventana la excepcion
            self.ui.notificacion.setText(str(mje))

class WindowEliminar(QDialog):
    """
    Clase que contiene métodos para la interaccion en la ventana Eliminar.
    """
    def __init__(self, obj_f):
        """
        Constructor que hereda el correspondiente a la clase ''QDialog()'' para acceder widgets.
        :param obj_f: Objeto Crud.
        """
        super().__init__()
        # Creo objeto de la clase en QT para crear widgets
        self.ui = Ui_Eliminar()
        # Se acccede al metodo setupUi que crea widgets
        self.ui.setupUi(self,)
        # Sedo accedo a objeto Crud desde cualquier metodo de esta clase        
        self.obj_f = obj_f

        # Callback de widgets Button
        self.ui.btn_aceptar.clicked.connect(self.delete)
        self.ui.btn_cancelar.clicked.connect(self.close)
    
    def delete(self, ):
        """
        Método para eliminar un articulo existente.
        """
        mje = self.obj_f.elim(
            self.ui.in_nombre)

        # Informa en la ventana estado del nuevo articulo
        self.ui.notificacion.setText(mje)
        
class WindowModificar(QDialog):
    """
    Clase que contiene métodos para la interaccion en la ventana Modificar.
    """
    def __init__(self, obj_f):
        """
        Constructor que hereda el correspondiente a la clase ''QDialog()'' para acceder widgets.
        :param obj_f: Objeto Crud.
        """
        super().__init__()
        # Creo objeto de la clase en QT para crear widgets
        self.ui = Ui_Modificar()
        # Se acccede al metodo setupUi que crea widgets
        self.ui.setupUi(self,)
        # Sedo accedo a objeto Crud desde cualquier metodo de esta clase
        self.obj_f = obj_f

        # Callback de widgets Button
        self.ui.btn_aceptar.clicked.connect(self.modificated)
        self.ui.btn_cancelar.clicked.connect(self.close)

    def modificated(self, ):
        """
        Método para modificar un articulo existente.
        """
        try:
            mje = self.obj_f.modif(
                        self.ui.in_nombre, 
                        self.ui.in_cant, 
                        self.ui.in_precio, 
                        self.ui.in_descrip)
            # Informa en la ventana estado del nuevo articulo
            self.ui.notificacion.setText(mje)
        except (
            ValueError
        ) as mje:
            # Informa en la ventana la excepcion
            self.ui.notificacion.setText(str(mje))

class WindowConsulta(QWidget):
    """
    Clase que contiene métodos para la interaccion en la ventana Consulta.
    """
    def __init__(self, obj_f, obj_win_main):
        """
        Constructor que hereda el correspondiente a la clase ''QWidget()'' para acceder widgets.
        :param obj_f: Objeto Crud.
        :param obj_win_main: Objeto para acceder atributos/metodos de ventana principal
        """
        super().__init__()
        # Creo objeto de la clase en QT para crear widgets
        self.ui = Ui_Consulta()
        # Se acccede al metodo setupUi que crea widgets
        self.ui.setupUi(self,)
        # Sedo accedo a objeto Crud desde cualquier metodo de esta clase
        self.obj_f = obj_f
        # Sedo accedo a objeto MainWindow desde cualquier metodo de esta clase
        self.obj_win_main = obj_win_main

        # Callback de widgets Button
        self.ui.btn_buscar.clicked.connect(self.search)
        self.ui.btn_cat_full.clicked.connect(self.full_cat)
        self.ui.btn_volver.clicked.connect(self.close)

    def insert(self, id, nom, cant, prec, descrip):
        """
        Método para agregar un articulo nuevo en la tabla.
        """
        self.frame = []
        self.frame.append((id, nom, cant, prec, descrip))

        fila=0        
        for registro in self.frame:
            columna=0            
            # Creo fila nueva cada vez que se lee un nuevo frame (todos los parametros de un articulo)
            self.ui.catalogo_list.insertRow(fila) 
            for elemento in registro:
                # Cargo cada parametro en la columna correspondiente, por orden.
                self.ui.catalogo_list.setItem(fila, columna, QTableWidgetItem(elemento))
                columna+=1
            fila+=1

    def delete(self, ):
        """
        Método para limpiar celdas de la tabla.
        """
        self.ui.catalogo_list.clearContents()

    def search(self, ):
        """
        Método para buscar y mostrar articulo en la tabla.
        """
        mje = self.obj_f.consulta(
                    self.ui.in_nombre, self.ui.in_descrip, self)

        # Informa en la ventana estado del nuevo articulo
        self.ui.notificacion.setText(mje)

    def full_cat(self, ):
        """
        Método para mostrar todos los articulos en la tabla
        """
        self.ui.catalogo_list.clearContents()  
        # Actualizo tabla y grafico de torta
        self.obj_f.mostrar_cat(self, self.obj_win_main)
