# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_agregar.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Agregar(object):
    def setupUi(self, Agregar):
        if not Agregar.objectName():
            Agregar.setObjectName(u"Agregar")
        Agregar.resize(382, 320)
        self.titulo = QLabel(Agregar)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(80, 10, 221, 45))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setAlignment(Qt.AlignCenter)
        self.notificacion = QLabel(Agregar)
        self.notificacion.setObjectName(u"notificacion")
        self.notificacion.setGeometry(QRect(100, 290, 161, 20))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.notificacion.setFont(font1)
        self.notificacion.setLayoutDirection(Qt.LeftToRight)
        self.notificacion.setStyleSheet(u"color: #aa0000")
        self.notificacion.setAlignment(Qt.AlignCenter)
        self.notificacion.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable)
        self.layoutWidget_2 = QWidget(Agregar)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(30, 60, 321, 161))
        self.formLayout = QFormLayout(self.layoutWidget_2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_nombre = QLabel(self.layoutWidget_2)
        self.label_nombre.setObjectName(u"label_nombre")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(14)
        self.label_nombre.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_nombre)

        self.in_nombre = QLineEdit(self.layoutWidget_2)
        self.in_nombre.setObjectName(u"in_nombre")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.in_nombre.sizePolicy().hasHeightForWidth())
        self.in_nombre.setSizePolicy(sizePolicy)
        font3 = QFont()
        self.in_nombre.setFont(font3)
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

        self.label_cant = QLabel(self.layoutWidget_2)
        self.label_cant.setObjectName(u"label_cant")
        self.label_cant.setFont(font2)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_cant)

        self.in_cant = QLineEdit(self.layoutWidget_2)
        self.in_cant.setObjectName(u"in_cant")
        sizePolicy.setHeightForWidth(self.in_cant.sizePolicy().hasHeightForWidth())
        self.in_cant.setSizePolicy(sizePolicy)
        self.in_cant.setFont(font3)
        self.in_cant.setTabletTracking(False)
        self.in_cant.setFocusPolicy(Qt.StrongFocus)
        self.in_cant.setAutoFillBackground(False)
        self.in_cant.setStyleSheet(u"QLineEdit {\n"
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
"}\n"
"")
        self.in_cant.setInputMethodHints(Qt.ImhNone)
        self.in_cant.setMaxLength(32767)
        self.in_cant.setFrame(True)
        self.in_cant.setDragEnabled(False)
        self.in_cant.setReadOnly(False)
        self.in_cant.setClearButtonEnabled(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.in_cant)

        self.label_precio_2 = QLabel(self.layoutWidget_2)
        self.label_precio_2.setObjectName(u"label_precio_2")
        self.label_precio_2.setFont(font2)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_precio_2)

        self.in_precio = QLineEdit(self.layoutWidget_2)
        self.in_precio.setObjectName(u"in_precio")
        sizePolicy.setHeightForWidth(self.in_precio.sizePolicy().hasHeightForWidth())
        self.in_precio.setSizePolicy(sizePolicy)
        self.in_precio.setFont(font3)
        self.in_precio.setTabletTracking(False)
        self.in_precio.setFocusPolicy(Qt.StrongFocus)
        self.in_precio.setAutoFillBackground(False)
        self.in_precio.setStyleSheet(u"QLineEdit {\n"
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
        self.in_precio.setInputMethodHints(Qt.ImhNone)
        self.in_precio.setMaxLength(32767)
        self.in_precio.setFrame(True)
        self.in_precio.setDragEnabled(False)
        self.in_precio.setReadOnly(False)
        self.in_precio.setClearButtonEnabled(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.in_precio)

        self.label_descrip = QLabel(self.layoutWidget_2)
        self.label_descrip.setObjectName(u"label_descrip")
        self.label_descrip.setFont(font2)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_descrip)

        self.in_descrip = QLineEdit(self.layoutWidget_2)
        self.in_descrip.setObjectName(u"in_descrip")
        sizePolicy.setHeightForWidth(self.in_descrip.sizePolicy().hasHeightForWidth())
        self.in_descrip.setSizePolicy(sizePolicy)
        self.in_descrip.setFont(font3)
        self.in_descrip.setTabletTracking(False)
        self.in_descrip.setFocusPolicy(Qt.StrongFocus)
        self.in_descrip.setAutoFillBackground(False)
        self.in_descrip.setStyleSheet(u"QLineEdit {\n"
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
        self.in_descrip.setInputMethodHints(Qt.ImhNone)
        self.in_descrip.setMaxLength(32767)
        self.in_descrip.setFrame(True)
        self.in_descrip.setDragEnabled(False)
        self.in_descrip.setReadOnly(False)
        self.in_descrip.setClearButtonEnabled(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.in_descrip)

        self.horizontalLayoutWidget = QWidget(Agregar)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 240, 321, 41))
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
"}\n"
"QPushButton {\n"
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
"    backgroun"
                        "d-color: #88AEF1; /* Color celeste */\n"
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
        self.btn_aceptar.setInputMethodHints(Qt.ImhSensitiveData|Qt.ImhUppercaseOnly)
        self.btn_aceptar.setCheckable(True)
        self.btn_aceptar.setChecked(True)
        self.btn_aceptar.setAutoRepeat(True)
        self.btn_aceptar.setAutoRepeatDelay(150)
        self.btn_aceptar.setAutoDefault(True)
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
"}\n"
"\n"
"QPushButton {\n"
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
"    back"
                        "ground-color: #88AEF1; /* Color celeste */\n"
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
        self.btn_cancelar.setInputMethodHints(Qt.ImhSensitiveData|Qt.ImhUppercaseOnly)
        self.btn_cancelar.setCheckable(True)
        self.btn_cancelar.setChecked(True)
        self.btn_cancelar.setAutoRepeat(True)
        self.btn_cancelar.setAutoRepeatDelay(150)
        self.btn_cancelar.setAutoDefault(True)
        self.btn_cancelar.setFlat(False)

        self.horizontalLayout.addWidget(self.btn_cancelar)


        self.retranslateUi(Agregar)

        self.btn_aceptar.setDefault(False)
        self.btn_cancelar.setDefault(False)


        QMetaObject.connectSlotsByName(Agregar)
    # setupUi

    def retranslateUi(self, Agregar):
        Agregar.setWindowTitle(QCoreApplication.translate("Agregar", u"Dialog", None))
        self.titulo.setText(QCoreApplication.translate("Agregar", u"Nuevo articulo", None))
        self.notificacion.setText("")
        self.label_nombre.setText(QCoreApplication.translate("Agregar", u"Producto:", None))
        self.in_nombre.setInputMask("")
        self.in_nombre.setText("")
        self.in_nombre.setPlaceholderText(QCoreApplication.translate("Agregar", u"Ingrese nombre de producto", None))
        self.label_cant.setText(QCoreApplication.translate("Agregar", u"Cantidad:", None))
        self.in_cant.setInputMask("")
        self.in_cant.setText("")
        self.in_cant.setPlaceholderText(QCoreApplication.translate("Agregar", u"Ingrese valor numerico", None))
        self.label_precio_2.setText(QCoreApplication.translate("Agregar", u"Precio:", None))
        self.in_precio.setInputMask("")
        self.in_precio.setText("")
        self.in_precio.setPlaceholderText(QCoreApplication.translate("Agregar", u"Ingrese valor numerico", None))
        self.label_descrip.setText(QCoreApplication.translate("Agregar", u"Descripcion:", None))
        self.in_descrip.setInputMask("")
        self.in_descrip.setText("")
        self.in_descrip.setPlaceholderText(QCoreApplication.translate("Agregar", u"Ingrese una breve descripcion", None))
        self.btn_aceptar.setText(QCoreApplication.translate("Agregar", u"Aceptar", None))
        self.btn_cancelar.setText(QCoreApplication.translate("Agregar", u"Cancelar", None))
    # retranslateUi

