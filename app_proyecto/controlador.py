import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core

from vista import *
from modelo import *
from observador import ObservadorConcreto

class Controlador:
    def __init__(self, ):
        self.obj_db = BaseDatos()
        self.obj_f = Crud(self.obj_db)  # Creo un objeto de clase Crud.

        self.crear_ventanas()
        self.observador_crud=ObservadorConcreto(self.obj_f, self.obj_db)
        self.window_consulta.full_cat() #Obtiene catalogo completo de la DB y la muestra al abrir la ventana

        try:
            print("Abro menu de app_stock")            
            sys.exit(app.exec_())    # Mantiene abierta la app
        except SystemExit:
            print("Cierro menu de app_stock")

    def crear_ventanas(self, ):
        self.window_main = MainWindow(self)
        self.window_agregar = WindowAgregar(self.obj_f)
        self.window_eliminar = WindowEliminar(self.obj_f)
        self.window_modificar = WindowModificar(self.obj_f)
        self.window_consulta = WindowConsulta(self.obj_f, self.window_main) 

        # Los metodos utilizados son los heredados de la clase QMainWindow
        self.window_main.setWindowTitle("App Stock")
        self.window_main.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setStyle("fusion")

    obj_controlador = Controlador()