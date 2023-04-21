import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core

from vista import *

class Controlador:
    def __init__(self, window):
        # Los metodos utilizados son los heredados de la clase QMainWindow
        window.setWindowTitle("App Stock")
        window.show()

        try:
            sys.exit(app.exec_())    # Mantiene abierta la app
        except SystemExit:
            print("Cierro menu de app_stock")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setStyle("fusion")
    window = MainWindow() # Creo objeto de la clase MainWindow

    obj_controlador = Controlador(window)