import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core

from Qt.agregar import *
from Qt.eliminar import *
from Qt.modificar import *
from Qt.consulta import *


class WindowAgregar(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_Agregar()
        self.ui.setupUi(self,)
        self.ui.btns_option.accepted.connect(self.new_load)
        self.ui.btns_option.rejected .connect(self.exit)
    
    def exit(self, ):
        self.close()
        print("Regresa a menu principal")

    def new_load(self,):
        nombre=str(self.ui.in_nombre.text())
        cant=int(self.ui.in_cant.text())
        precio=int(self.ui.in_precio.text())
        descrip=str(self.ui.in_descrip.text())

        self.ui.in_nombre.clear()
        self.ui.in_cant.clear()
        self.ui.in_precio.clear()
        self.ui.in_descrip.clear()    

        print(nombre)
        print(cant)
        print(precio)
        print(descrip)
        self.exit()
        print("Se guarda nuevo articulo")
    
class WindowEliminar(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_Eliminar()
        self.ui.setupUi(self,)
        self.ui.btns_option.accepted.connect(self.delete)
        self.ui.btns_option.rejected .connect(self.exit)
    
    def exit(self, ):
        self.close()
        print("Regresa a menu principal")

    def delete(self,):
        nombre=str(self.ui.in_nombre.text())
        self.ui.in_nombre.clear()

        print(nombre)
        self.exit()
        print("Se elimino articulo")

class WindowModificar(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_Modificar()
        self.ui.setupUi(self,)
        self.ui.btns_option.accepted.connect(self.modificated)
        self.ui.btns_option.rejected .connect(self.exit)
    
    def exit(self, ):
        self.close()
        print("Regresa a menu principal")

    def modificated(self,):
        nombre=str(self.ui.in_nombre.text())
        cant=int(self.ui.in_cant.text())
        precio=int(self.ui.in_precio.text())
        descrip=str(self.ui.in_descrip.text())

        self.ui.in_nombre.clear()
        self.ui.in_cant.clear()
        self.ui.in_precio.clear()
        self.ui.in_descrip.clear()    

        print(nombre)
        print(cant)
        print(precio)
        print(descrip)
        self.exit()
        print("Se guardo modificaciones")

class WindowConsulta(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_Consulta()
        self.ui.setupUi(self,)
        self.ui.btn_buscar.clicked.connect(self.search)
        self.ui.btn_cat_full.clicked.connect(self.full_cat)
        self.ui.btn_volver.clicked.connect(self.exit)

        self.ui.catalogo_list.setColumnWidth(0, 40)
        self.ui.catalogo_list.setColumnWidth(1, 120)
        self.ui.catalogo_list.setColumnWidth(2, 80)
        self.ui.catalogo_list.setColumnWidth(3, 80)
        self.ui.catalogo_list.setColumnWidth(4, 160)

        self.list_componentes_test()
        self.load_list_componentes()
    
    def list_componentes_test(self, ):
        self.datos = []

        self.datos.append(('2','1N4548', '32', '32', 'Diodo'))
        self.datos.append(('3','MCP3008', '2', '434', 'Circuito integrado'))
        self.datos.append(('4','7805', '45', '120', 'Regulador de tension'))

    def load_list_componentes(self, ):
        fila=0        
        for registro in self.datos:
            columna=0            
            self.ui.catalogo_list.insertRow(fila) # se debe crear filas cada vez que se cargan dato
            for elemento in registro:
                celda = QTableWidgetItem(elemento)
                self.ui.catalogo_list.setItem(fila, columna, celda)
                columna+=1
            fila+=1


    def exit(self, ):
        self.close()
        print("Regresa a menu principal")
    
    def search(self, ):
        nombre=str(self.ui.in_nombre.text())
        descrip=str(self.ui.in_descrip.text())

        self.ui.in_nombre.clear()
        self.ui.in_descrip.clear()

        print(nombre)
        print(descrip)        
        print("Busca articulo")
    
    def full_cat(self, ):
        print("Muestra catalogo completo")
