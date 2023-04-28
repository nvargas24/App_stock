import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core

from vista import *
from observador import ObservadorConcreto

class Controlador:
    def __init__(self, ):    
        self.obj_win_main = MainWindow() # Creo objeto de la clase MainWindow
        # Los metodos utilizados son los heredados de la clase QMainWindow
        self.obj_win_main.setWindowTitle("App Stock")
        self.obj_win_main.show()

        self.observador_win_agregar=ObservadorConcreto(self.obj_win_main.obj_f)

        try:
            sys.exit(app.exec_())    # Mantiene abierta la app
        except SystemExit:
            print("Cierro menu de app_stock")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setStyle("fusion")

    obj_controlador = Controlador()