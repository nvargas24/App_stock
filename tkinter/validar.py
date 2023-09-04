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


class Validacion:
    """
    Clase que contiene los métodos asociados para la comprobación de los campos de entrada.
    """

    def val_entry(self, data_entry, name_entry):
        """
        Método para validar los datos con regex.

        :param data_entry: Dato a validar.
        :param name_entry: Tipo de campo de entrada a validar.

        :returns: Resultado de la validación.
        """
        # Patrones para validar los campos por regex.
        patron1 = "^[a-zA-Z0-9\./ ]+$"
        patron2 = "^[0-9]+$"
        patron3 = "^[0-9\.]+$"

        if name_entry == "nom":
            return re.match(patron1, data_entry)
        elif name_entry == "cant":
            return re.match(patron2, data_entry)
        elif name_entry == "prec":
            return re.match(patron3, data_entry)
        elif name_entry == "descrip":
            return re.match(patron1, data_entry)

    def empty_entry(self, data_entry, name_entry):
        """
        Método para chequear si el campo de entrada se encuentra vacío.

        :param data_entry: Contenido del campo de entrada.
        :param name_entry: Tipo de campo de entrada a revisar.

        :returns: ``0`` Si el campo está vacío.
        :returns: ``1`` Si en el campo se ingresó un dato.
        """
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
