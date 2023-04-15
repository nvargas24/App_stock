# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_stock.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(591, 354)
        MainWindow.setStyleSheet(u"QApplication::setStyle(\"fusion\");\n"
"")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.menu_opciones = QGroupBox(self.centralwidget)
        self.menu_opciones.setObjectName(u"menu_opciones")
        self.menu_opciones.setGeometry(QRect(20, 90, 161, 241))
        self.btn_agregar = QPushButton(self.menu_opciones)
        self.btn_agregar.setObjectName(u"btn_agregar")
        self.btn_agregar.setGeometry(QRect(20, 30, 121, 41))
        self.btn_eliminar = QPushButton(self.menu_opciones)
        self.btn_eliminar.setObjectName(u"btn_eliminar")
        self.btn_eliminar.setGeometry(QRect(20, 80, 121, 41))
        self.btn_modificar = QPushButton(self.menu_opciones)
        self.btn_modificar.setObjectName(u"btn_modificar")
        self.btn_modificar.setGeometry(QRect(20, 130, 121, 41))
        self.btn_consultar = QPushButton(self.menu_opciones)
        self.btn_consultar.setObjectName(u"btn_consultar")
        self.btn_consultar.setGeometry(QRect(20, 180, 121, 41))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 551, 72))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titulo = QLabel(self.layoutWidget)
        self.titulo.setObjectName(u"titulo")
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.titulo)

        self.subtitulo = QLabel(self.layoutWidget)
        self.subtitulo.setObjectName(u"subtitulo")
        font1 = QFont()
        font1.setPointSize(12)
        self.subtitulo.setFont(font1)
        self.subtitulo.setAcceptDrops(False)
        self.subtitulo.setLayoutDirection(Qt.LeftToRight)
        self.subtitulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.subtitulo)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setGeometry(QRect(220, 100, 341, 231))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(1)
        self.verticalLayoutWidget = QWidget(self.frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(19, 19, 311, 191))
        self.grafica_torta = QVBoxLayout(self.verticalLayoutWidget)
        self.grafica_torta.setObjectName(u"grafica_torta")
        self.grafica_torta.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_opciones.setTitle(QCoreApplication.translate("MainWindow", u"Opciones", None))
        self.btn_agregar.setText(QCoreApplication.translate("MainWindow", u"Agregar articulo", None))
        self.btn_eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar articulo", None))
        self.btn_modificar.setText(QCoreApplication.translate("MainWindow", u"Modificar articulo", None))
        self.btn_consultar.setText(QCoreApplication.translate("MainWindow", u"Consultar Stock", None))
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"Electronica del oeste", None))
        self.subtitulo.setText(QCoreApplication.translate("MainWindow", u"Bienvenido, seleccione la opcion a realizar", None))
    # retranslateUi

