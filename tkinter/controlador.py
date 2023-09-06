"""
controlador.py:
    Módulo encargado de iniciar la app. 
"""
__author__ = "Diego Calderón, Nahuel Vargas"
__maintainer__ = "Diego Calderón, Nahuel Vargas"
__email__ = "diegoacalderon994@gmail.com, nahuvargas24@gmail.com"
__copyright__ = "Copyright 2023"
__version__ = "0.0.1"

from tkinter import Tk
from vista import Menu
from observador import ObservadorConcreto
from servidor import Serv
import threading

theproc = ""


class Controlador:
    """
    Clase que crea un objeto de clase ``Menu()`` para la configuración de la interfaz gráfica.

    :param window: Objeto ventana que se crea al iniciar la app.
    """

    def __init__(self, window):
        """
        Constructor que crea un objeto de clase ``Menu()`` (que importa de ``vista.py``)
        y le pasa como argumento el objeto ventana (``window``).
        También crea un observador que seguirá las acciones del objeto de clase Crud creado en vista.Menu

        :param window: Objeto ventana que se crea al iniciar la app.
        """
        self.window_controlador = window
        self.obj_vista = Menu(self.window_controlador)

        # Creo el observador y le paso el objeto de clase Crud creado en vista.Menu
        self.el_observador = ObservadorConcreto(self.obj_vista.obj_f)

        # -------------------Servidor-----------------------------------
        # Lanzo servidor
        if theproc != "":
            theproc.kill()
            threading.Thread(
                target=self.iniciar_servidor, args=(self.obj_vista.obj_f,), daemon=True
            ).start()
        else:
            threading.Thread(
                target=self.iniciar_servidor, args=(self.obj_vista.obj_f,), daemon=True
            ).start()

    def iniciar_servidor(self, obj_f):
        self.servidor = Serv(
            obj_f
        )  # Creo objeto de clase Serv cuyo constructor lanza el servidor


if __name__ == "__main__":
    window_tk = Tk()
    obj_controlador = Controlador(window_tk)
    window_tk.mainloop()
