"""
vista.py:
    Módulo encargado de generar la interfaz gráfica de la app. 
"""
__author__ = "Diego Calderón, Nahuel Vargas"
__maintainer__ = "Diego Calderón, Nahuel Vargas"
__email__ = "diegoacalderon994@gmail.com, nahuvargas24@gmail.com"
__copyright__ = "Copyright 2023"
__version__ = "0.0.1"

from modelo import Crud
from kivy.metrics import dp
from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty


class Home(MDBoxLayout):
    Builder.load_file("home.kv")


class Agregar(MDBoxLayout):
    Builder.load_file("agregar.kv")


class Eliminar(MDBoxLayout):
    Builder.load_file("eliminar.kv")


class Modificar(MDBoxLayout):
    Builder.load_file("modificar.kv")


class IconListItem(OneLineIconListItem):
    icon = StringProperty()


class MisPantallas(MDScreenManager):
    def __init__(self, app, **kwargs):
        super(MisPantallas, self).__init__(**kwargs)
        self.obj_app = app
        self.obj_home = Home()
        self.obj_agregar = Agregar()
        self.obj_eliminar = Eliminar()
        self.obj_modificar = Modificar()
        self.ids.home.add_widget(self.obj_home)
        self.ids.add.add_widget(self.obj_agregar)
        self.ids.elim.add_widget(self.obj_eliminar)
        self.ids.mod.add_widget(self.obj_modificar)
        self.obj_c = Crud()
        self.crear_menu()

    def cambiar_tema(self, value):
        if value == "claro":
            self.menu.dismiss()
            self.obj_app.theme_cls.primary_palette = "LightBlue"
            self.obj_app.theme_cls.theme_style = "Light"
            self.obj_home.ids.buttonadd.md_bg_color = "#C7C7C7"
            self.obj_home.ids.buttondel.md_bg_color = "#C7C7C7"
            self.obj_home.ids.buttonedit.md_bg_color = "#C7C7C7"
            self.obj_home.ids.buttonsearch.md_bg_color = "#C7C7C7"
            self.crear_menu()
        else:
            self.menu.dismiss()
            self.obj_app.theme_cls.primary_palette = "Orange"
            self.obj_app.theme_cls.theme_style = "Dark"
            self.obj_home.ids.buttonadd.md_bg_color = "#404040"
            self.obj_home.ids.buttondel.md_bg_color = "#404040"
            self.obj_home.ids.buttonedit.md_bg_color = "#404040"
            self.obj_home.ids.buttonsearch.md_bg_color = "#404040"
            self.crear_menu()

    def crear_menu(self):
        self.menu_items = [
            {
                "icon": "weather-sunny",
                "text": "Tema Claro",
                "theme_text_color": "Custom",
                "text_color": self.obj_app.theme_cls.opposite_bg_darkest,
                "viewclass": "IconListItem",
                "on_release": lambda x="claro": self.cambiar_tema(x),
            },
            {
                "icon": "moon-waning-crescent",
                "text": "Tema Oscuro",
                "theme_text_color": "Custom",
                "text_color": self.obj_app.theme_cls.opposite_bg_darkest,
                "viewclass": "IconListItem",
                "on_release": lambda x="oscuro": self.cambiar_tema(x),
            },
        ]
        self.menu = MDDropdownMenu(
            caller=self.obj_home.ids.button,
            items=self.menu_items,
            max_height=dp(100),
            width_mult=dp(3),
        )

    def call(self):
        nombre = self.obj_agregar.ids.input_nombre_add
        cantidad = self.obj_agregar.ids.input_cantidad_add
        precio = self.obj_agregar.ids.input_precio_add
        descripcion = self.obj_agregar.ids.input_descrip_add
        mje = self.obj_c.agreg(nombre, cantidad, precio, descripcion)
        print(mje)
