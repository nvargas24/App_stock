# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_main.ui'
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
        MainWindow.resize(643, 550)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(True)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"/*QApplication::setStyle(\"fusion\");*/\n"
"background-color: #EAEAEA;\n"
"")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.menu_opciones = QGroupBox(self.centralwidget)
        self.menu_opciones.setObjectName(u"menu_opciones")
        self.menu_opciones.setGeometry(QRect(60, 180, 191, 331))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.menu_opciones.sizePolicy().hasHeightForWidth())
        self.menu_opciones.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.menu_opciones.setFont(font)
        self.menu_opciones.setFlat(False)
        self.menu_opciones.setCheckable(False)
        self.menu_opciones.setChecked(False)
        self.verticalLayout_2 = QVBoxLayout(self.menu_opciones)
        self.verticalLayout_2.setSpacing(14)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(16, 16, 16, 18)
        self.btn_agregar = QPushButton(self.menu_opciones)
        self.btn_agregar.setObjectName(u"btn_agregar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_agregar.sizePolicy().hasHeightForWidth())
        self.btn_agregar.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.btn_agregar.setFont(font1)
        self.btn_agregar.setMouseTracking(False)
        self.btn_agregar.setTabletTracking(False)
        self.btn_agregar.setAcceptDrops(False)
        self.btn_agregar.setAutoFillBackground(False)
        self.btn_agregar.setStyleSheet(u"QPushButton {\n"
"    background-color: #F2F2F2; /* Color de fondo */\n"
"    border: 2px solid #D9D9D9; /* Borde gris claro */\n"
"    border-radius: 15px; /* Bordes curvos */\n"
"    padding: 5px 10px; /* Espacio interno para texto */\n"
"    font-weight: bold; /* Texto en negrita */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    color: #444444; /* Color de texto */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #88AEF1; /* Color celeste */\n"
"    border-color: #0078D7; /* Borde celeste */\n"
"    color: #FFFFFF; /* Color de texto blanco */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #88AEF1; /* Color celeste */\n"
"    border-color: #0078D7; /* Borde celeste */\n"
"    color: #FFFFFF; /* Color de texto blanco */\n"
"	outline: none; /* Elimina el contorno alrededor del QLineEdit al seleccionarlo */\n"
"}")
        self.btn_agregar.setAutoDefault(True)

        self.verticalLayout_2.addWidget(self.btn_agregar)

        self.btn_eliminar = QPushButton(self.menu_opciones)
        self.btn_eliminar.setObjectName(u"btn_eliminar")
        sizePolicy1.setHeightForWidth(self.btn_eliminar.sizePolicy().hasHeightForWidth())
        self.btn_eliminar.setSizePolicy(sizePolicy1)
        self.btn_eliminar.setFont(font1)
        self.btn_eliminar.setStyleSheet(u"QPushButton {\n"
"    background-color: #F2F2F2; /* Color de fondo */\n"
"    border: 2px solid #D9D9D9; /* Borde gris claro */\n"
"    border-radius: 15px; /* Bordes curvos */\n"
"    padding: 5px 10px; /* Espacio interno para texto */\n"
"    font-weight: bold; /* Texto en negrita */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    color: #444444; /* Color de texto */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #88AEF1; /* Color celeste */\n"
"    border-color: #0078D7; /* Borde celeste */\n"
"    color: #FFFFFF; /* Color de texto blanco */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #88AEF1; /* Color celeste */\n"
"    border-color: #0078D7; /* Borde celeste */\n"
"    color: #FFFFFF; /* Color de texto blanco */\n"
"	outline: none; /* Elimina el contorno alrededor del QLineEdit al seleccionarlo */\n"
"}\n"
"")
        self.btn_eliminar.setAutoDefault(True)

        self.verticalLayout_2.addWidget(self.btn_eliminar)

        self.btn_modificar = QPushButton(self.menu_opciones)
        self.btn_modificar.setObjectName(u"btn_modificar")
        sizePolicy1.setHeightForWidth(self.btn_modificar.sizePolicy().hasHeightForWidth())
        self.btn_modificar.setSizePolicy(sizePolicy1)
        self.btn_modificar.setFont(font1)
        self.btn_modificar.setStyleSheet(u"QPushButton {\n"
"    background-color: #F2F2F2; /* Color de fondo */\n"
"    border: 2px solid #D9D9D9; /* Borde gris claro */\n"
"    border-radius: 15px; /* Bordes curvos */\n"
"    padding: 5px 10px; /* Espacio interno para texto */\n"
"    font-weight: bold; /* Texto en negrita */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    color: #444444; /* Color de texto */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #88AEF1; /* Color celeste */\n"
"    border-color: #0078D7; /* Borde celeste */\n"
"    color: #FFFFFF; /* Color de texto blanco */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #88AEF1; /* Color celeste */\n"
"    border-color: #0078D7; /* Borde celeste */\n"
"    color: #FFFFFF; /* Color de texto blanco */\n"
"	outline: none; /* Elimina el contorno alrededor del QLineEdit al seleccionarlo */\n"
"}")
        self.btn_modificar.setAutoDefault(True)

        self.verticalLayout_2.addWidget(self.btn_modificar)

        self.btn_consultar = QPushButton(self.menu_opciones)
        self.btn_consultar.setObjectName(u"btn_consultar")
        sizePolicy1.setHeightForWidth(self.btn_consultar.sizePolicy().hasHeightForWidth())
        self.btn_consultar.setSizePolicy(sizePolicy1)
        self.btn_consultar.setFont(font1)
        self.btn_consultar.setStyleSheet(u"QPushButton {\n"
"    background-color: #F2F2F2; /* Color de fondo */\n"
"    border: 2px solid #D9D9D9; /* Borde gris claro */\n"
"    border-radius: 15px; /* Bordes curvos */\n"
"    padding: 5px 10px; /* Espacio interno para texto */\n"
"    font-weight: bold; /* Texto en negrita */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    color: #444444; /* Color de texto */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #88AEF1; /* Color celeste */\n"
"    border-color: #0078D7; /* Borde celeste */\n"
"    color: #FFFFFF; /* Color de texto blanco */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #88AEF1; /* Color celeste */\n"
"    border-color: #0078D7; /* Borde celeste */\n"
"    color: #FFFFFF; /* Color de texto blanco */\n"
"	outline: none; /* Elimina el contorno alrededor del QLineEdit al seleccionarlo */\n"
"}")
        self.btn_consultar.setAutoDefault(True)

        self.verticalLayout_2.addWidget(self.btn_consultar)

        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(1, 5)
        self.verticalLayout_2.setStretch(2, 5)
        self.verticalLayout_2.setStretch(3, 5)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 591, 103))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titulo = QLabel(self.layoutWidget)
        self.titulo.setObjectName(u"titulo")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(36)
        font2.setBold(True)
        font2.setWeight(75)
        self.titulo.setFont(font2)
        self.titulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.titulo)

        self.subtitulo = QLabel(self.layoutWidget)
        self.subtitulo.setObjectName(u"subtitulo")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setWeight(75)
        self.subtitulo.setFont(font3)
        self.subtitulo.setAcceptDrops(False)
        self.subtitulo.setLayoutDirection(Qt.LeftToRight)
        self.subtitulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.subtitulo)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setGeometry(QRect(270, 190, 311, 321))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(1)
        self.verticalLayoutWidget = QWidget(self.frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 291, 301))
        self.grafica_torta = QVBoxLayout(self.verticalLayoutWidget)
        self.grafica_torta.setObjectName(u"grafica_torta")
        self.grafica_torta.setContentsMargins(0, 0, 0, 0)
        self.notificacion = QLabel(self.centralwidget)
        self.notificacion.setObjectName(u"notificacion")
        self.notificacion.setGeometry(QRect(420, 520, 161, 20))
        self.notificacion.setFont(font1)
        self.notificacion.setLayoutDirection(Qt.LeftToRight)
        self.notificacion.setStyleSheet(u"color: #aa0000")
        self.notificacion.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.notificacion.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(60, 150, 511, 20))
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setLineWidth(0)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)
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
        self.notificacion.setText("")
    # retranslateUi

