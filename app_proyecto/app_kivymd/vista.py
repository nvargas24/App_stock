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
from kivymd.uix.button import MDIconButton
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg as FigureCanvas
import matplotlib.pyplot as plt
import random

# Flag utilizado para indicar si el widget actual
# en la pantalla de Consulta es la tabla (1) o el gráfico (0).
flag_tabla = 1


# Clase destinada a cargar el contenido del archivo "home.kv"
class Home(MDBoxLayout):
    Builder.load_file("home.kv")


# Clase destinada a cargar el contenido del archivo "agregar.kv"
class Agregar(MDBoxLayout):
    Builder.load_file("agregar.kv")


# Clase destinada a cargar el contenido del archivo "eliminar.kv"
class Eliminar(MDBoxLayout):
    Builder.load_file("eliminar.kv")


# Clase destinada a cargar el contenido del archivo "modificar.kv"
class Modificar(MDBoxLayout):
    Builder.load_file("modificar.kv")


# Clase destinada a cargar el contenido del archivo "consultar.kv"
class Consultar(MDBoxLayout):
    Builder.load_file("consultar.kv")


# Clase personalizada utilizada para añadir íconos en el menú desplegable
# encargado de cambiar el tema de la App.
class IconListItem(OneLineIconListItem):
    icon = StringProperty()


# Clase que contiene métodos para actualizar y dar estilo al gráfico de torta.
class Canvas_grafica(FigureCanvas):
    # Constructor que hereda el correspondiente a la clase FigureCanvas(),
    # y que además crea un gráfico matplotlib en blanco.
    def __init__(self, app):
        # Asigno un espacio para ubicar el gráfico de matplotlib usando Canvas.
        self.fig, self.ax = plt.subplots(
            1, dpi=100, figsize=(50, 50), sharey=True, facecolor="none"
        )
        super().__init__(self.fig)
        self.obj_app = app  # Objeto asociado a la App.

    # Método para actualizar nombres y cantidades en gráfico de torta.
    def upgrade_graph(self, nombre, cantidad):
        # Borro gráfico antiguo.
        self.ax.clear()

        # Parámetros para nuevo gráfico.
        self.nombres = nombre
        self.tamanio = cantidad
        self.colores = []
        self.explotar = []

        # Asigno color aleatorio claros segun la cantidad de artículos disponibles.
        for i in range(len(self.nombres)):
            r = random.randint(150, 255)
            g = random.randint(150, 255)
            b = random.randint(150, 255)
            self.colores.append("#%02x%02x%02x" % (r, g, b))
            self.explotar.append(0.05)

        # Pasaje de porcentaje a valor real en bd.
        valor_real = lambda pct: "{:.0f}".format(
            (pct * sum(list(map(int, self.tamanio)))) / 100
        )

        # Chequeo el tema actual definido en la App para, en función de ello,
        # cambiar el color de la fuente del gráfico.
        if self.obj_app.theme_cls.theme_style == "Dark":
            text_color = {"fontsize": 18, "color": "white"}
        else:
            text_color = {"fontsize": 18, "color": "black"}

        # Asigno nuevos parámetros a gráfico.
        self.ax.pie(
            self.tamanio,
            explode=self.explotar,
            labels=self.nombres,
            colors=self.colores,
            autopct=valor_real,
            pctdistance=0.8,
            shadow=True,
            startangle=90,
            radius=0.7,
            labeldistance=1.1,
            textprops=text_color,
        )
        self.draw()  # Dibujo el gráfico.


# Clase asociada a la ventana de la App y que permite el acceso a las otras pantallas(MDScreen) de la misma.
class MisPantallas(MDScreenManager):
    def __init__(self, app, **kwargs):
        super(MisPantallas, self).__init__(**kwargs)
        self.obj_app = app  # Objeto asociado a la App.
        # Objeto asociado a la clase Home (root) del archivo "home.kv".
        self.obj_home = Home()
        # Objeto asociado a la clase Agregar (root) del archivo "agregar.kv".
        self.obj_agregar = Agregar()
        # Objeto asociado a la clase Eliminar (root) del archivo "eliminar.kv".
        self.obj_eliminar = Eliminar()
        # Objeto asociado a la clase Modificar (root) del archivo "modificar.kv".
        self.obj_modificar = Modificar()
        # Objeto asociado a la clase Consultar (root) del archivo "consultar.kv".
        self.obj_consultar = Consultar()

        # Agrego el contenido del archivo "home.kv" al MDScreen cuyo id es "home".
        self.ids.home.add_widget(self.obj_home)
        # Agrego el contenido del archivo "agregar.kv" al MDScreen cuyo id es "add".
        self.ids.add.add_widget(self.obj_agregar)
        # Agrego el contenido del archivo "eliminar.kv" al MDScreen cuyo id es "elim".
        self.ids.elim.add_widget(self.obj_eliminar)
        # Agrego el contenido del archivo "modificar.kv" al MDScreen cuyo id es "mod".
        self.ids.mod.add_widget(self.obj_modificar)
        # Agrego el contenido del archivo "consultar.kv" al MDScreen cuyo id es "consulta".
        self.ids.consulta.add_widget(self.obj_consultar)

        self.filter_selected = "Nombre"
        self.grafica = Canvas_grafica(self.obj_app)

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
            self.crear_menu_filtro()
            self.crear_tabla()
            if flag_tabla:
                self.show_table(self)
            else:
                self.show_graph(self)
            self.obj_c.mostrar_cat(self)
        else:
            self.menu.dismiss()
            self.obj_app.theme_cls.primary_palette = "Orange"
            self.obj_app.theme_cls.theme_style = "Dark"
            self.obj_home.ids.buttonadd.md_bg_color = "#404040"
            self.obj_home.ids.buttondel.md_bg_color = "#404040"
            self.obj_home.ids.buttonedit.md_bg_color = "#404040"
            self.obj_home.ids.buttonsearch.md_bg_color = "#404040"
            self.crear_menu()
            self.crear_menu_filtro()
            self.crear_tabla()
            if flag_tabla:
                self.show_table(self)
            else:
                self.show_graph(self)
            self.obj_c.mostrar_cat(self)

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
        self.crear_tabla()
        """
        self.data_tables = MDDataTable(
            rows_num=10000,
            size_hint=(1, 1),
            column_data=[
                ("[size=18][color=#CC742C]ID[/color][/size]", dp(10)),
                ("[size=18][color=#CC742C]Producto[/color][/size]", dp(30)),
                ("[size=18][color=#CC742C]Cantidad[/color][/size]", dp(20)),
                ("[size=18][color=#CC742C]Precio[/color][/size]", dp(30)),
                ("[size=18][color=#CC742C]Descripcion[/color][/size]", dp(50)),
            ],
        )
        """
        self.bar_search = MDTextField(
            id="bar_search",
            size_hint=(2, 1),
            hint_text="Buscar por nombre",
            # mode="fill",
            max_text_length=20,
            font_size="18sp",
            hint_text_color_normal=(0, 0, 0, 1),
            hint_text_color_focus=(0, 0, 0, 1),
            text_color_normal=(0, 0, 0, 1),
            text_color_focus=(0, 0, 0, 1),
            line_color_normal=(0, 0, 0, 1),
            line_color_focus=(0, 0, 0, 1),
            max_length_text_color=(0, 0, 0, 1),
        )
        self.filter = MDIconButton(
            id="filter",
            size_hint=(1, 1),
            # pos_hint= {"center_y": .5},
            # pos= (self.bar_search.width - self.width + dp(8), 0),
            # theme_text_color="Primary",
            icon="filter-variant",
            font_size="48sp",
            on_release=self.select_filter,
        )
        self.titulo = MDLabel(
            id="titulo",
            size_hint=(1, 1),
            halign="center",
            font_style="H5",
            theme_text_color="Custom",
            text_color=(0, 0, 0, 1),
            text="Catálogo",
        )  # Si asigno 'id' con .kv no lo reconoce dentro del layout, usando children

        self.crear_menu_filtro()
        """
        self.filter_menu = MDDropdownMenu(
            caller=self.filter,
            items=[
                {
                    "text": "Nombre",
                    "theme_text_color": "Custom",
                    "text_color": self.obj_app.theme_cls.opposite_bg_darkest,
                    "viewclass": "OneLineListItem",
                    "left_widget": MDCheckbox(),
                    "on_release": lambda x="Nombre": self.filter_item_selected(x)
                },
                {
                    "text": "Descripcion",
                    "theme_text_color": "Custom",
                    "text_color": self.obj_app.theme_cls.opposite_bg_darkest,
                    "viewclass": "OneLineListItem",
                    "left_widget": MDCheckbox(),
                    "on_release": lambda x="Descripcion": self.filter_item_selected(x)
                },
            ],
            max_height=dp(100),
            width_mult=dp(3),
        )
        """

        self.btn_graph = MDIconButton(
            id="button_graph",
            size_hint=(1, 1),
            icon="chart-pie",
            font_size="48sp",
            on_release=self.show_graph,
        )
        self.btn_table = MDIconButton(
            id="button_table",
            size_hint=(1, 1),
            icon="table-eye",
            font_size="48sp",
            on_release=self.show_table,
        )

        # Evento para detectar texto en MDTextField
        self.bar_search.bind(text=self.on_text_changed)

        # Agrego widgets a layout
        self.obj_consultar.ids.table.add_widget(self.data_tables)
        self.obj_consultar.ids.field_search.add_widget(self.titulo)
        self.obj_consultar.ids.button_data.add_widget(self.btn_graph)

        self.obj_c.mostrar_cat(self)

    def crear_tabla(self):
        if self.obj_app.theme_cls.primary_palette == "Orange":
            self.data_tables = MDDataTable(
                rows_num=10000,
                size_hint=(1, 1),
                column_data=[
                    ("[size=18][color=#CC742C]ID[/color][/size]", dp(10)),
                    ("[size=18][color=#CC742C]Producto[/color][/size]", dp(30)),
                    ("[size=18][color=#CC742C]Cantidad[/color][/size]", dp(20)),
                    ("[size=18][color=#CC742C]Precio[/color][/size]", dp(30)),
                    ("[size=18][color=#CC742C]Descripcion[/color][/size]", dp(50)),
                ],
            )
        else:
            self.data_tables = MDDataTable(
                rows_num=10000,
                size_hint=(1, 1),
                column_data=[
                    ("[size=18][color=#03A9F4]ID[/color][/size]", dp(10)),
                    ("[size=18][color=#03A9F4]Producto[/color][/size]", dp(30)),
                    ("[size=18][color=#03A9F4]Cantidad[/color][/size]", dp(20)),
                    ("[size=18][color=#03A9F4]Precio[/color][/size]", dp(30)),
                    ("[size=18][color=#03A9F4]Descripcion[/color][/size]", dp(50)),
                ],
            )

    def crear_menu_filtro(self):
        self.filter_menu = MDDropdownMenu(
            caller=self.filter,
            items=[
                {
                    "text": "Nombre",
                    "theme_text_color": "Custom",
                    "text_color": self.obj_app.theme_cls.opposite_bg_darkest,
                    "viewclass": "OneLineListItem",
                    "left_widget": MDCheckbox(),
                    "on_release": lambda x="Nombre": self.filter_item_selected(x),
                },
                {
                    "text": "Descripcion",
                    "theme_text_color": "Custom",
                    "text_color": self.obj_app.theme_cls.opposite_bg_darkest,
                    "viewclass": "OneLineListItem",
                    "left_widget": MDCheckbox(),
                    "on_release": lambda x="Descripcion": self.filter_item_selected(x),
                },
            ],
            max_height=dp(100),
            width_mult=dp(3),
        )

    def select_filter(self, instance):
        self.filter_menu.open()

    def filter_item_selected(self, filter_selected):
        self.filter_menu.dismiss()
        print(f"Elemento seleccionado: {filter_selected}")
        self.filter_selected = filter_selected

        if self.filter_selected == "Nombre":
            self.bar_search.hint_text = "Buscar por nombre"
        elif self.filter_selected == "Descripcion":
            self.bar_search.hint_text = "Buscar por descripcion"

    def show_buscar(self):
        # Toggle widget en layout
        id_widget = self.obj_consultar.ids.field_search.children[0].id

        print(self.obj_consultar.ids.field_search.children)
        if id_widget == "titulo":
            self.obj_consultar.ids.field_search.clear_widgets()
            self.obj_consultar.ids.field_search.add_widget(self.bar_search)
            self.obj_consultar.ids.field_search.add_widget(self.filter)
        elif id_widget == "bar_search" or id_widget == "filter":
            self.obj_consultar.ids.field_search.clear_widgets()
            self.obj_consultar.ids.field_search.add_widget(self.titulo)

    def on_text_changed(self, instance, item_search):
        print("Texto cambiado:", item_search)
        if self.filter_selected == "Nombre":
            msj = self.obj_c.consulta(item_search, "", self)
        elif self.filter_selected == "Descripcion":
            msj = self.obj_c.consulta("", item_search, self)

        print(msj)
        if msj:
            self.data_tables.row_data = []  # Borro filas

    def show_graph(self, instance):
        global flag_tabla

        flag_tabla = 0
        self.obj_consultar.ids.button_data.clear_widgets()
        self.obj_consultar.ids.table.clear_widgets()

        self.obj_consultar.ids.button_data.add_widget(self.btn_table)
        self.obj_consultar.ids.table.add_widget(self.grafica)

        self.obj_consultar.ids.field_search.clear_widgets()
        self.obj_consultar.ids.field_search.add_widget(self.titulo)

    def show_table(self, instance):
        global flag_tabla

        flag_tabla = 1
        self.obj_consultar.ids.button_data.clear_widgets()
        self.obj_consultar.ids.table.clear_widgets()

        self.obj_consultar.ids.button_data.add_widget(self.btn_graph)
        self.obj_consultar.ids.table.add_widget(self.data_tables)

    def delete(self):
        self.data_tables.row_data = []  # Borro filas

    # Accedo a base de datos -> lectura en modelo.py-> carga en vista.py
    def full_cat(
        self,
    ):
        self.delete()
        self.obj_c.mostrar_cat(
            self
        )  # para que desde modelo.py pueda acceder a add_frame

    # Agrega frame a tabla
    def add_frame(self, *args):
        self.data_tables.add_row((args[0], args[1], args[2], args[3], args[4]))
