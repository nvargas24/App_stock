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

import random

#-------- Clases para widgets --------#
#--- Clase para abrir ventanas secundarias ---#
class Opciones():
    def show_win_agregar(self,):
        self.parent.window_agregar.setWindowTitle("Agregar")
        self.parent.window_agregar.show()

        #--- Limpia celdas  ---#
        self.parent.window_agregar.ui.in_nombre.clear()
        self.parent.window_agregar.ui.in_cant.clear()
        self.parent.window_agregar.ui.in_precio.clear()
        self.parent.window_agregar.ui.in_descrip.clear()
        self.parent.window_agregar.ui.notificacion.clear()

    def show_win_eliminar(self,):
        self.parent.window_eliminar.setWindowTitle("Eliminar")
        self.parent.window_eliminar.show()

        #--- Limpia celdas  ---#
        self.parent.window_eliminar.ui.in_nombre.clear()
        self.parent.window_eliminar.ui.notificacion.clear()

    def show_win_modificar(self,):
        self.parent.window_modificar.setWindowTitle("Modificar")
        self.parent.window_modificar.show()

        #--- Limpia celdas  ---#
        self.parent.window_modificar.ui.in_nombre.clear()
        self.parent.window_modificar.ui.in_cant.clear()
        self.parent.window_modificar.ui.in_precio.clear()
        self.parent.window_modificar.ui.in_descrip.clear()
        self.parent.window_modificar.ui.notificacion.clear()

    def show_win_consultar(self,):
        self.parent.window_consulta.setWindowTitle("Consulta")
        self.parent.window_consulta.show()

        #--- Limpia celdas  ---#
        self.parent.window_consulta.ui.in_nombre.clear()
        self.parent.window_consulta.ui.in_descrip.clear()
        self.parent.window_consulta.ui.notificacion.clear()
        
        self.parent.window_consulta.full_cat() #Obtiene catalogo completo de la DB y la muestra al abrir la ventana

# --- Clase para iteractuar con grafico ---#
class Canvas_grafica(FigureCanvas):
    def __init__(self, ):
        # Asigno un espacio para ubicar el grafico de matplotlib usando Canvas
        self.fig, self.ax = plt.subplots(1, dpi=70, figsize=(12,12), sharey=True, facecolor='none')
        super().__init__(self.fig)
        
    def upgrade_graph(self, componentes, cantidad):
        self.nombres=componentes
        self.tamanio=cantidad
        self.colores=[]
        self.explotar=[]
        
        # Asigno color aleatorio segun la cantidad de articulos disponibles
        for i in range(len(self.nombres)):
            r = random.randint(150, 255)
            g = random.randint(150, 255)
            b = random.randint(150, 255)
            self.colores.append('#%02x%02x%02x' % (r, g, b))
            self.explotar.append(0.08)

        self.ax.clear()
        valor_real = lambda pct: "{:.0f}".format((pct * sum(list(map(int, self.tamanio)))) / 100) #pasaje de porcentaje a valor real en bd

        self.ax.pie(self.tamanio, explode=self.explotar, labels=self.nombres, colors=self.colores,
                    autopct=valor_real, pctdistance=0.8, shadow=True, startangle=90, radius=1.2, labeldistance=1.1, textprops={'fontsize': 18})

        self.ax.axis('equal')
        self.draw() # para actualizar grafico de ventana

#-------- Clases para ventanas -------#
class MainWindow(QMainWindow, Opciones):
    def __init__(self, parent):
        super().__init__() # Acccedo a constructor de la clase QMainWindow
        self.ui = Ui_MainWindow() # Creo objeto de la clase en QT para crear widgets
        self.ui.setupUi(self,) # Se acccede al metodo setupUi que crea widgets
        self.parent = parent # Para poder acceder a mostrar las ventanas en la clase Opciones

        #------------- Grafico de torta -------------------#
        self.grafica = Canvas_grafica()
        self.ui.grafica_torta.addWidget(self.grafica)

        #--------------- Acciones para botones ------------#
        self.ui.btn_agregar.clicked.connect(self.show_win_agregar)
        self.ui.btn_eliminar.clicked.connect(self.show_win_eliminar)
        self.ui.btn_modificar.clicked.connect(self.show_win_modificar)
        self.ui.btn_consultar.clicked.connect(self.show_win_consultar)
        
class WindowAgregar(QDialog):
    def __init__(self, obj_f, parent=None):
        super().__init__()
        self.ui = Ui_Agregar()
        self.ui.setupUi(self,)
        self.obj_f = obj_f # Objeto Crud

        self.ui.btn_aceptar.clicked.connect(self.new_load)
        self.ui.btn_cancelar.clicked.connect(self.close)

    def new_load(self, ):
        mje = self.obj_f.agreg(
                    self.ui.in_nombre, 
                    self.ui.in_cant, 
                    self.ui.in_precio, 
                    self.ui.in_descrip)

        self.ui.notificacion.setText(mje)

        if not mje:
            self.close() # Borra ventana

class WindowEliminar(QDialog):
    def __init__(self, obj_f, parent=None):
        super().__init__()
        self.ui = Ui_Eliminar()
        self.ui.setupUi(self,)
        self.obj_f = obj_f

        self.ui.btn_aceptar.clicked.connect(self.delete)
        self.ui.btn_cancelar.clicked.connect(self.close)
    
    def delete(self, ):
        mje = self.obj_f.elim(
            self.ui.in_nombre)

        self.ui.notificacion.setText(mje)
        
        if not mje:
            self.close # Borra ventana

class WindowModificar(QDialog):
    def __init__(self, obj_f, parent=None):
        super().__init__()
        self.ui = Ui_Modificar()
        self.ui.setupUi(self,)
        self.obj_f = obj_f

        self.ui.btn_aceptar.clicked.connect(self.modificated)
        self.ui.btn_cancelar.clicked.connect(self.close)

    def modificated(self, ):
        mje = self.obj_f.modif(
                    self.ui.in_nombre, 
                    self.ui.in_cant, 
                    self.ui.in_precio, 
                    self.ui.in_descrip)

        self.ui.notificacion.setText(mje)
        
        if not mje:
            self.close() # Borra ventana

class WindowConsulta(QWidget):
    def __init__(self, obj_f, obj_menu):
        super().__init__()
        self.ui = Ui_Consulta()
        self.ui.setupUi(self,)
        self.obj_f = obj_f
        self.obj_menu = obj_menu

        self.ui.btn_buscar.clicked.connect(self.search)
        self.ui.btn_cat_full.clicked.connect(self.full_cat)
        self.ui.btn_volver.clicked.connect(self.close)

        #--- Ajusto ancho de columnas de la tabla ---#
        """
        self.ui.catalogo_list.setColumnWidth(0, 40)
        self.ui.catalogo_list.setColumnWidth(1, 120)
        self.ui.catalogo_list.setColumnWidth(2, 80)
        self.ui.catalogo_list.setColumnWidth(3, 80)
        self.ui.catalogo_list.setColumnWidth(4, 160)  
        """
    def insert(self, id, nom, cant, prec, descrip):
        self.frame = []
        self.frame.append((id, nom, cant, prec, descrip))

        fila=0        
        for registro in self.frame:
            columna=0            
            self.ui.catalogo_list.insertRow(fila) # se debe crear filas cada vez que se cargan dato
            for elemento in registro:
                self.ui.catalogo_list.setItem(fila, columna, QTableWidgetItem(elemento))
                columna+=1
            fila+=1

    # Para borrar las celdas de la tabla y solo mostrar la busqueda
    def delete(self, ):
        self.ui.catalogo_list.clearContents()

    def search(self, ):
        print("Buscar articulo")
        mje = self.obj_f.consulta(
                    self.ui.in_nombre, 
                    self.ui.in_descrip, 
                    self)

        self.ui.notificacion.setText(mje)

    def full_cat(self, ):
        self.ui.catalogo_list.clearContents()  
        print("Muestra catalogo completo")
        self.obj_f.mostrar_cat(self, self.obj_menu)
