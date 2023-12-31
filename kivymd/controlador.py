"""
controlador.py:
    Módulo encargado de iniciar la app. 
"""
__author__ = "Diego Calderón, Nahuel Vargas"
__maintainer__ = "Diego Calderón, Nahuel Vargas"
__email__ = "diegoacalderon994@gmail.com, nahuvargas24@gmail.com"
__copyright__ = "Copyright 2023"
__version__ = "0.0.1"

from kivymd.app import MDApp
from vista import MisPantallas


# Clase controladora encargada de crear el objeto asociado a la ventana (MisPantallas) y lanzar la App.
class AppController(MDApp):
    def build(self):
        self.icon = "img/puente.png"
        self.title = "Control de stock"
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        self.obj_vista = MisPantallas(
            self
        )  # Creo el objeto asociado a la ventana y le paso el objeto de la App.
        return self.obj_vista


if __name__ == "__main__":
    AppController().run()  # Lanzo la App.
