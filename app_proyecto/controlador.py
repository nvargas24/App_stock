"""
controlador.py:
    Módulo encargado de iniciar la app. 
"""
__author__ = "Diego Calderón, Nahuel Vargas"
__maintainer__ = "Diego Calderón, Nahuel Vargas"
__email__ = "diegoacalderon994@gmail.com, nahuvargas24@gmail.com"
__copyright__ = "Copyright 2023"
__version__ = "0.0.2"

import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from servidor import Serv
import threading
from vista import MainWindow
from observador import ObservadorConcreto


class Controlador:
    """
    Clase que crea un objeto de clase ``MainWindow()`` para la configuración de la interfaz gráfica.
    También define un observador y enciende el servidor.
    """

    def __init__(self):
        """
        Constructor que crea un objeto de clase ``MainWindow()`` (que importa de ``vista.py``)
        y define un observador que seguirá las acciones del objeto de clase ``Crud()`` creado en ``vista.MainWindow``,
        También se encarga de activar el servidor que atenderá las conexiones entrantes.
        """
        self.obj_win_main = MainWindow()
        # Los metodos utilizados son los heredados de la clase QMainWindow().
        self.obj_win_main.setWindowTitle("App Stock")
        self.obj_win_main.show()
        self.obj_win_main.move(400, 200)

        self.observador_win_agregar = ObservadorConcreto(self.obj_win_main.obj_f)

        # ----------------- Servidor ----------------- #
        # Creo hilo que lanza el servidor.
        threading.Thread(
            target=self.iniciar_servidor, args=(self.obj_win_main.obj_f,), daemon=True
        ).start()

        # --------------------------------------------- #
        try:
            # Mantiene abierta la app.
            sys.exit(app.exec_())
        except SystemExit:
            print("Cierro menu de app_stock")

    def iniciar_servidor(self, obj_f):
        """
        Método que crea objeto de clase ``Serv()`` para lanzar al servidor.

        :param obj_f: Objeto de clase ``Crud()`` creado en ``MainWindow()``.
        """
        self.servidor = Serv(obj_f)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    obj_controlador = Controlador()
