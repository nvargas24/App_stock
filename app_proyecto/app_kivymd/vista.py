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
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField


class Home(MDBoxLayout):
    Builder.load_file("home.kv")


class Agregar(MDBoxLayout):
    Builder.load_file("agregar.kv")


class Eliminar(MDBoxLayout):
    Builder.load_file("eliminar.kv")


class Modificar(MDBoxLayout):
    Builder.load_file("modificar.kv")


class Consultar(MDBoxLayout):
    Builder.load_file("consultar.kv")


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
        self.obj_consultar = Consultar()
        self.ids.home.add_widget(self.obj_home)
        self.ids.add.add_widget(self.obj_agregar)
        self.ids.elim.add_widget(self.obj_eliminar)
        self.ids.mod.add_widget(self.obj_modificar)
        self.ids.consulta.add_widget(self.obj_consultar)
        self.obj_c = Crud()
        self.crear_menu()
        self.widgets_consulta()

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

    def call_agreg(self):
        nombre = self.obj_agregar.ids.input_nombre_add
        cantidad = self.obj_agregar.ids.input_cantidad_add
        precio = self.obj_agregar.ids.input_precio_add
        descripcion = self.obj_agregar.ids.input_descrip_add
        try:
            mje = self.obj_c.agreg(nombre, cantidad, precio, descripcion)
        except ValueError as mje:
            print(mje)
            self.show_msg_popup(
                ["Error en la operación", "Campos cargados incorrectamente"]
            )
        else:
            self.show_msg_popup(mje)

    def call_elim(self):
        nombre = self.obj_eliminar.ids.input_nombre_elim

        mje = self.obj_c.elim(nombre)
        self.show_msg_popup(mje)

    def call_modif(self):
        nombre = self.obj_modificar.ids.input_nombre_mod
        cantidad = self.obj_modificar.ids.input_cantidad_mod
        precio = self.obj_modificar.ids.input_precio_mod
        descripcion = self.obj_modificar.ids.input_descrip_mod
        try:
            mje = self.obj_c.modif(nombre, cantidad, precio, descripcion)
        except ValueError as mje:
            print(mje)
            self.show_msg_popup(
                ["Error en la operación", "Campos cargados incorrectamente"]
            )
        else:
            self.show_msg_popup(mje)

    def show_msg_popup(self, mje):
        self.dialog = MDDialog(
            title=mje[0],
            type="custom",
            content_cls=MDLabel(
                text=mje[1],
                theme_text_color="Custom",
                text_color=self.obj_app.theme_cls.opposite_bg_darkest,
            ),
            buttons=[
                MDFlatButton(
                    text="Aceptar",
                    theme_text_color="Custom",
                    text_color=self.obj_app.theme_cls.primary_color,
                    on_release=self.close_msg_popup,
                ),
            ],
        )

        self.dialog.open()

    def close_msg_popup(self, obj):
        self.dialog.dismiss()

    def limpiar_campos(self, lista_campos):
        for campo in lista_campos:
            campo.text = ""
            campo.error = False

    """
    def set_error_message(self, instance_text):
        if instance_text.focus == False:
            instance_text.required = True
        else:
            instance_text.required = True
            instance_text.error = False
    """


    # Metodos para screen consulta
    def widgets_consulta(self):
        self.data_tables = MDDataTable(
            rows_num=10000,
            # use_pagination=True,
            size_hint=(1, 1),
            column_data=[
                ("[size=18][color=#CC742C]ID[/color][/size]", dp(10)),
                ("[size=18][color=#CC742C]Producto[/color][/size]", dp(30)),
                ("[size=18][color=#CC742C]Cantidad[/color][/size]", dp(20)),
                ("[size=18][color=#CC742C]Precio[/color][/size]", dp(30)),
                ("[size=18][color=#CC742C]Descripcion[/color][/size]", dp(50)),
            ],
        )
        self.bar_search = MDTextField(
            id="bar_search",
            size_hint_x=1,
            size_hint_y=1,
            # pos_hint = {"center_x": .5, "center_y": .5},
            hint_text="Buscar",
            mode="fill",
            max_text_length=20,
            # icon_left= "magnify",
            font_size="18sp",
        )

        self.titulo = MDLabel(
            id="titulo",
            size_hint_x=1,
            size_hint_y=1,
            halign="center",
            font_style="H5",
            theme_text_color="Custom",
            text="Catalogo",
        )  # Si asigno 'id' con .kv no lo reconoce dentro del layout, usando children

        # Evento para detectar texto en MDTextField
        self.bar_search.bind(text=self.on_text_changed)
        self.bar_search.bind(focus=self.on_focus)
        # Agrego widgets a layout
        self.obj_consultar.ids.table.add_widget(self.data_tables)
        self.obj_consultar.ids.field_search.add_widget(self.titulo)

        self.obj_c.mostrar_cat(self)

    def on_focus(self, instance, value):
        #print("valor:  ", value)
        #print(self.bar_search.hint_text)
        if value:
            self.bar_search.hint_text = ""
        else:
            self.bar_search.hint_text = "Buscar"

    def show_buscar(self):
        # Toggle widget en layout
        # print(self.obj_consultar.ids.field_search.children)
        if self.obj_consultar.ids.field_search.children[0].id == "titulo":
            self.obj_consultar.ids.field_search.clear_widgets()
            self.obj_consultar.ids.field_search.add_widget(self.bar_search)
        elif self.obj_consultar.ids.field_search.children[0].id == "bar_search":
            self.obj_consultar.ids.field_search.clear_widgets()
            self.obj_consultar.ids.field_search.add_widget(self.titulo)

    def on_text_changed(self, instance, value):
        print("Texto cambiado:", value)
        self.obj_c.consulta(value, value, self)
    
    def delete(self, ):
        self.data_tables.row_data=[] # Borro filas

    # Accedo a base de datos -> lectura en modelo.py-> carga en vista.py
    def full_cat(self, ):
        self.delete()
        self.obj_c.mostrar_cat(self) # para que desde modelo.py pueda acceder a add_frame
    # Agrega frame a tabla 
    def add_frame(self, *args):
        self.data_tables.add_row((args[0], args[1], args[2], args[3], args[4]))