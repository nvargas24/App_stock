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


class AppController(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        self.obj_vista = MisPantallas(self)
        return self.obj_vista


if __name__ == "__main__":
    AppController().run()
