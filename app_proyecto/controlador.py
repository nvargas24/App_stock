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


class Controlador:
    """
    Clase que crea un objeto de clase ``Menu()`` para la configuración de la interfaz gráfica.

    :param window: Objeto ventana que se crea al iniciar la app.
    """

    def __init__(self, window):
        """
        Constructor que crea un objeto de clase ``Menu()`` (que importa de ``vista.py``)
        y le pasa como argumento el objeto ventana (``window``).

        :param window: Objeto ventana que se crea al iniciar la app.
        """
        self.window_controlador = window
        self.obj_vista = Menu(self.window_controlador)


if __name__ == "__main__":
    window_tk = Tk()
    obj_controlador = Controlador(window_tk)
    window_tk.mainloop()
