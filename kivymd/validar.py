"""
validar.py:
    Módulo que se encarga de la validación de los datos ingresados.
"""
__author__ = "Diego Calderón, Nahuel Vargas"
__maintainer__ = "Diego Calderón, Nahuel Vargas"
__email__ = "diegoacalderon994@gmail.com, nahuvargas24@gmail.com"
__copyright__ = "Copyright 2023"
__version__ = "0.0.1"

import re


# Clase que contiene los métodos asociados para la comprobación de los campos de entrada.
class Validacion:
    # Método para validar los datos con regex.
    def val_entry(self, data_entry, name_entry):
        # Patrones para validar los campos por regex
        # según el tipo de campo de entrada (name_entry) a validar.
        patron1 = "^[a-zA-Z0-9\./ ]+$"
        patron2 = "^[0-9]+$"
        patron3 = "^[0-9\.]+$"

        # Retorno resultado de la validación.
        if name_entry == "nom":
            return re.match(patron1, data_entry)
        elif name_entry == "cant":
            return re.match(patron2, data_entry)
        elif name_entry == "prec":
            return re.match(patron3, data_entry)
        elif name_entry == "descrip":
            return re.match(patron1, data_entry)

    # Método para chequear si el campo de entrada se encuentra vacío.
    def empty_entry(self, data_entry, name_entry):
        # Retorna '0' si el campo está vacío.
        # Retorna '1' si en el campo se ingresó un dato.

        if (
            name_entry == "nom"
            and data_entry
            and data_entry != "Escriba el nombre del artículo"
        ):
            return 1
        elif (
            name_entry == "cant"
            and data_entry
            and data_entry != "Escriba un valor numérico"
        ):
            return 1
        elif (
            name_entry == "prec"
            and data_entry
            and data_entry != "Escriba un valor numérico"
        ):
            return 1
        elif (
            name_entry == "descrip"
            and data_entry
            and data_entry != "Agregue una breve descrip. del art."
        ):
            return 1
        else:
            return 0
