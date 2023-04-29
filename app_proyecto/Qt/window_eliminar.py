# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_eliminar.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Eliminar(object):
    def setupUi(self, Eliminar):
        if not Eliminar.objectName():
            Eliminar.setObjectName(u"Eliminar")
        Eliminar.resize(339, 201)
        self.layoutWidget = QWidget(Eliminar)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 60, 291, 41))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_nombre = QLabel(self.layoutWidget)
        self.label_nombre.setObjectName(u"label_nombre")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(14)
        self.label_nombre.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_nombre)

        self.in_nombre = QLineEdit(self.layoutWidget)
        self.in_nombre.setObjectName(u"in_nombre")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.in_nombre.sizePolicy().hasHeightForWidth())
        self.in_nombre.setSizePolicy(sizePolicy)
        font1 = QFont()
        self.in_nombre.setFont(font1)
        self.in_nombre.setTabletTracking(False)
        self.in_nombre.setFocusPolicy(Qt.StrongFocus)
        self.in_nombre.setAutoFillBackground(False)
        self.in_nombre.setStyleSheet(u"QLineEdit {\n"
"    background-color: #F7F7F7; /* Color de fondo */\n"
"    border: 2px solid #D9D9D9; /* Borde gris claro */\n"
"    border-radius: 17px; /* Bordes curvos */\n"
"    padding: 5px 10px; /* Espacio interno para texto */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    color: #444444; /* Color de texto */\n"
"}\n"
"QLineEdit:focus {\n"
"    border-color: #0078d7; /* Cambia el color del borde cuando se selecciona el QLineEdit */\n"
"    outline: none; /* Elimina el contorno alrededor del QLineEdit al seleccionarlo */\n"
"}")
        self.in_nombre.setInputMethodHints(Qt.ImhNone)
        self.in_nombre.setMaxLength(32767)
        self.in_nombre.setFrame(True)
        self.in_nombre.setDragEnabled(False)
        self.in_nombre.setReadOnly(False)
        self.in_nombre.setClearButtonEnabled(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.in_nombre)

        self.titulo = QLabel(Eliminar)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(60, 10, 221, 45))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.titulo.setFont(font2)
        self.titulo.setAlignment(Qt.AlignCenter)
        self.notificacion = QLabel(Eliminar)
        self.notificacion.setObjectName(u"notificacion")
        self.notificacion.setGeometry(QRect(100, 170, 161, 20))
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        self.notificacion.setFont(font3)
        self.notificacion.setLayoutDirection(Qt.LeftToRight)
        self.notificacion.setStyleSheet(u"color: #aa0000")
        self.notificacion.setAlignment(Qt.AlignCenter)
        self.notificacion.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable)
        self.horizontalLayoutWidget = QWidget(Eliminar)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 120, 291, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, 0, 15, 0)
        self.btn_aceptar = QPushButton(self.horizontalLayoutWidget)
        self.btn_aceptar.setObjectName(u"btn_aceptar")
        self.btn_aceptar.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_aceptar.sizePolicy().hasHeightForWidth())
        self.btn_aceptar.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setBold(True)
        font4.setWeight(75)
        self.btn_aceptar.setFont(font4)
        self.btn_aceptar.setStyleSheet(u"QPushButton {\n"
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
"}")
        self.btn_aceptar.setInputMethodHints(Qt.ImhSensitiveData|Qt.ImhUppercaseOnly)
        self.btn_aceptar.setCheckable(True)
        self.btn_aceptar.setChecked(True)
        self.btn_aceptar.setAutoRepeat(True)
        self.btn_aceptar.setAutoRepeatDelay(150)
        self.btn_aceptar.setAutoDefault(False)
        self.btn_aceptar.setFlat(False)

        self.horizontalLayout.addWidget(self.btn_aceptar)

        self.btn_cancelar = QPushButton(self.horizontalLayoutWidget)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.btn_cancelar.sizePolicy().hasHeightForWidth())
        self.btn_cancelar.setSizePolicy(sizePolicy1)
        self.btn_cancelar.setFont(font4)
        self.btn_cancelar.setStyleSheet(u"QPushButton {\n"
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
"}")
        self.btn_cancelar.setInputMethodHints(Qt.ImhSensitiveData|Qt.ImhUppercaseOnly)
        self.btn_cancelar.setCheckable(True)
        self.btn_cancelar.setChecked(True)
        self.btn_cancelar.setAutoRepeat(True)
        self.btn_cancelar.setAutoRepeatDelay(150)
        self.btn_cancelar.setAutoDefault(False)
        self.btn_cancelar.setFlat(False)

        self.horizontalLayout.addWidget(self.btn_cancelar)


        self.retranslateUi(Eliminar)

        self.btn_aceptar.setDefault(False)
        self.btn_cancelar.setDefault(False)


        QMetaObject.connectSlotsByName(Eliminar)
    # setupUi

    def retranslateUi(self, Eliminar):
        Eliminar.setWindowTitle(QCoreApplication.translate("Eliminar", u"Dialog", None))
        self.label_nombre.setText(QCoreApplication.translate("Eliminar", u"Producto:", None))
        self.in_nombre.setInputMask("")
        self.in_nombre.setText("")
        self.in_nombre.setPlaceholderText(QCoreApplication.translate("Eliminar", u"Ingrese nombre de producto", None))
        self.titulo.setText(QCoreApplication.translate("Eliminar", u"Eliminar articulo", None))
        self.notificacion.setText("")
        self.btn_aceptar.setText(QCoreApplication.translate("Eliminar", u"Aceptar", None))
        self.btn_cancelar.setText(QCoreApplication.translate("Eliminar", u"Cancelar", None))
    # retranslateUi

