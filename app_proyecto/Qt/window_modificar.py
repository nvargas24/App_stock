# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_modificar.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Modificar(object):
    def setupUi(self, Modificar):
        if not Modificar.objectName():
            Modificar.setObjectName("Modificar")
        Modificar.resize(379, 320)
        self.titulo = QLabel(Modificar)
        self.titulo.setObjectName("titulo")
        self.titulo.setGeometry(QRect(70, 20, 221, 25))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(Modificar)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 60, 321, 161))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName("formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_nombre = QLabel(self.layoutWidget)
        self.label_nombre.setObjectName("label_nombre")
        font1 = QFont()
        font1.setFamily("Segoe UI")
        font1.setPointSize(14)
        self.label_nombre.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_nombre)

        self.in_nombre = QLineEdit(self.layoutWidget)
        self.in_nombre.setObjectName("in_nombre")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.in_nombre.sizePolicy().hasHeightForWidth())
        self.in_nombre.setSizePolicy(sizePolicy)
        font2 = QFont()
        self.in_nombre.setFont(font2)
        self.in_nombre.setTabletTracking(False)
        self.in_nombre.setFocusPolicy(Qt.StrongFocus)
        self.in_nombre.setAutoFillBackground(False)
        self.in_nombre.setStyleSheet(
            "QLineEdit {\n"
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
            ""
        )
        self.in_nombre.setInputMethodHints(Qt.ImhNone)
        self.in_nombre.setMaxLength(32767)
        self.in_nombre.setFrame(True)
        self.in_nombre.setDragEnabled(False)
        self.in_nombre.setReadOnly(False)
        self.in_nombre.setClearButtonEnabled(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.in_nombre)

        self.label_cant = QLabel(self.layoutWidget)
        self.label_cant.setObjectName("label_cant")
        self.label_cant.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_cant)

        self.in_cant = QLineEdit(self.layoutWidget)
        self.in_cant.setObjectName("in_cant")
        sizePolicy.setHeightForWidth(self.in_cant.sizePolicy().hasHeightForWidth())
        self.in_cant.setSizePolicy(sizePolicy)
        self.in_cant.setFont(font2)
        self.in_cant.setTabletTracking(False)
        self.in_cant.setFocusPolicy(Qt.StrongFocus)
        self.in_cant.setAutoFillBackground(False)
        self.in_cant.setStyleSheet(
            "QLineEdit {\n"
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
            ""
        )
        self.in_cant.setInputMethodHints(Qt.ImhNone)
        self.in_cant.setMaxLength(32767)
        self.in_cant.setFrame(True)
        self.in_cant.setDragEnabled(False)
        self.in_cant.setReadOnly(False)
        self.in_cant.setClearButtonEnabled(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.in_cant)

        self.label_precio = QLabel(self.layoutWidget)
        self.label_precio.setObjectName("label_precio")
        self.label_precio.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_precio)

        self.in_precio = QLineEdit(self.layoutWidget)
        self.in_precio.setObjectName("in_precio")
        sizePolicy.setHeightForWidth(self.in_precio.sizePolicy().hasHeightForWidth())
        self.in_precio.setSizePolicy(sizePolicy)
        self.in_precio.setFont(font2)
        self.in_precio.setTabletTracking(False)
        self.in_precio.setFocusPolicy(Qt.StrongFocus)
        self.in_precio.setAutoFillBackground(False)
        self.in_precio.setStyleSheet(
            "QLineEdit {\n"
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
            ""
        )
        self.in_precio.setInputMethodHints(Qt.ImhNone)
        self.in_precio.setMaxLength(32767)
        self.in_precio.setFrame(True)
        self.in_precio.setDragEnabled(False)
        self.in_precio.setReadOnly(False)
        self.in_precio.setClearButtonEnabled(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.in_precio)

        self.label_descrip = QLabel(self.layoutWidget)
        self.label_descrip.setObjectName("label_descrip")
        self.label_descrip.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_descrip)

        self.in_descrip = QLineEdit(self.layoutWidget)
        self.in_descrip.setObjectName("in_descrip")
        sizePolicy.setHeightForWidth(self.in_descrip.sizePolicy().hasHeightForWidth())
        self.in_descrip.setSizePolicy(sizePolicy)
        self.in_descrip.setFont(font2)
        self.in_descrip.setTabletTracking(False)
        self.in_descrip.setFocusPolicy(Qt.StrongFocus)
        self.in_descrip.setAutoFillBackground(False)
        self.in_descrip.setStyleSheet(
            "QLineEdit {\n"
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
            ""
        )
        self.in_descrip.setInputMethodHints(Qt.ImhNone)
        self.in_descrip.setMaxLength(32767)
        self.in_descrip.setFrame(True)
        self.in_descrip.setDragEnabled(False)
        self.in_descrip.setReadOnly(False)
        self.in_descrip.setClearButtonEnabled(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.in_descrip)

        self.horizontalLayoutWidget = QWidget(Modificar)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 240, 321, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, 0, 15, 0)
        self.btn_aceptar = QPushButton(self.horizontalLayoutWidget)
        self.btn_aceptar.setObjectName("btn_aceptar")
        self.btn_aceptar.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_aceptar.sizePolicy().hasHeightForWidth())
        self.btn_aceptar.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamily("Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.btn_aceptar.setFont(font3)
        self.btn_aceptar.setStyleSheet(
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
            "}"
        )
        self.btn_aceptar.setInputMethodHints(Qt.ImhSensitiveData | Qt.ImhUppercaseOnly)
        self.btn_aceptar.setCheckable(True)
        self.btn_aceptar.setChecked(True)
        self.btn_aceptar.setAutoRepeat(True)
        self.btn_aceptar.setAutoRepeatDelay(150)
        self.btn_aceptar.setAutoDefault(True)
        self.btn_aceptar.setFlat(False)

        self.horizontalLayout.addWidget(self.btn_aceptar)

        self.btn_cancelar = QPushButton(self.horizontalLayoutWidget)
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.btn_cancelar.setEnabled(True)
        sizePolicy1.setHeightForWidth(
            self.btn_cancelar.sizePolicy().hasHeightForWidth()
        )
        self.btn_cancelar.setSizePolicy(sizePolicy1)
        self.btn_cancelar.setFont(font3)
        self.btn_cancelar.setStyleSheet(
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
            "}"
        )
        self.btn_cancelar.setInputMethodHints(Qt.ImhSensitiveData | Qt.ImhUppercaseOnly)
        self.btn_cancelar.setCheckable(True)
        self.btn_cancelar.setChecked(True)
        self.btn_cancelar.setAutoRepeat(True)
        self.btn_cancelar.setAutoRepeatDelay(150)
        self.btn_cancelar.setAutoDefault(True)
        self.btn_cancelar.setFlat(False)

        self.horizontalLayout.addWidget(self.btn_cancelar)

        self.notificacion = QLabel(Modificar)
        self.notificacion.setObjectName("notificacion")
        self.notificacion.setGeometry(QRect(110, 290, 161, 20))
        font4 = QFont()
        font4.setFamily("Segoe UI")
        font4.setPointSize(9)
        font4.setBold(True)
        font4.setWeight(75)
        self.notificacion.setFont(font4)
        self.notificacion.setLayoutDirection(Qt.LeftToRight)
        self.notificacion.setStyleSheet("color: #aa0000")
        self.notificacion.setAlignment(Qt.AlignCenter)
        self.notificacion.setTextInteractionFlags(
            Qt.LinksAccessibleByMouse | Qt.TextEditable
        )

        self.retranslateUi(Modificar)

        self.btn_aceptar.setDefault(False)
        self.btn_cancelar.setDefault(False)

        QMetaObject.connectSlotsByName(Modificar)

    # setupUi

    def retranslateUi(self, Modificar):
        Modificar.setWindowTitle(
            QCoreApplication.translate("Modificar", "Dialog", None)
        )
        self.titulo.setText(
            QCoreApplication.translate("Modificar", "Modificar artículo", None)
        )
        self.label_nombre.setText(
            QCoreApplication.translate("Modificar", "Producto:", None)
        )
        self.in_nombre.setInputMask("")
        self.in_nombre.setText("")
        self.in_nombre.setPlaceholderText(
            QCoreApplication.translate("Modificar", "Ingrese nombre de producto", None)
        )
        self.label_cant.setText(
            QCoreApplication.translate("Modificar", "Cantidad:", None)
        )
        self.in_cant.setInputMask("")
        self.in_cant.setText("")
        self.in_cant.setPlaceholderText(
            QCoreApplication.translate("Modificar", "Ingrese valor numérico", None)
        )
        self.label_precio.setText(
            QCoreApplication.translate("Modificar", "Precio:", None)
        )
        self.in_precio.setInputMask("")
        self.in_precio.setText("")
        self.in_precio.setPlaceholderText(
            QCoreApplication.translate("Modificar", "Ingrese valor numérico", None)
        )
        self.label_descrip.setText(
            QCoreApplication.translate("Modificar", "Descripción:", None)
        )
        self.in_descrip.setInputMask("")
        self.in_descrip.setText("")
        self.in_descrip.setPlaceholderText(
            QCoreApplication.translate(
                "Modificar", "Ingrese una breve descripción", None
            )
        )
        self.btn_aceptar.setText(
            QCoreApplication.translate("Modificar", "Aceptar", None)
        )
        self.btn_cancelar.setText(
            QCoreApplication.translate("Modificar", "Cancelar", None)
        )
        self.notificacion.setText("")

    # retranslateUi
