from kivy.metrics import dp
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty


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
        self.app = app
        self.crear_menu()

    def cambiar_tema(self, value):
        if value == "claro":
            self.menu.dismiss()
            self.app.theme_cls.primary_palette = "LightBlue"
            self.app.theme_cls.theme_style = "Light"
            self.ids.buttonadd.md_bg_color = "#C7C7C7"
            self.ids.buttondel.md_bg_color = "#C7C7C7"
            self.ids.buttonedit.md_bg_color = "#C7C7C7"
            self.ids.buttonsearch.md_bg_color = "#C7C7C7"
            self.crear_menu()
        else:
            self.menu.dismiss()
            self.app.theme_cls.primary_palette = "Orange"
            self.app.theme_cls.theme_style = "Dark"
            self.ids.buttonadd.md_bg_color = "#404040"
            self.ids.buttondel.md_bg_color = "#404040"
            self.ids.buttonedit.md_bg_color = "#404040"
            self.ids.buttonsearch.md_bg_color = "#404040"
            self.crear_menu()

    def crear_menu(self):
        self.menu_items = [
            {
                "icon": "weather-sunny",
                "text": "Tema Claro",
                "theme_text_color": "Custom",
                "text_color": self.app.theme_cls.opposite_bg_darkest,
                "viewclass": "IconListItem",
                "on_release": lambda x="claro": self.cambiar_tema(x),
            },
            {
                "icon": "moon-waning-crescent",
                "text": "Tema Oscuro",
                "theme_text_color": "Custom",
                "text_color": self.app.theme_cls.opposite_bg_darkest,
                "viewclass": "IconListItem",
                "on_release": lambda x="oscuro": self.cambiar_tema(x),
            },
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.button,
            items=self.menu_items,
            max_height=dp(100),
            width_mult=dp(3),
        )


class Main(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        return MisPantallas(self)

    def imprimir(self):
        print("Hola")


Main().run()