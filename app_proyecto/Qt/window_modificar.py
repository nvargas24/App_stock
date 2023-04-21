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
            Modificar.setObjectName(u"Modificar")
        Modificar.resize(291, 232)
        self.titulo = QLabel(Modificar)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(30, 10, 221, 45))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setAlignment(Qt.AlignCenter)
        self.btns_option = QDialogButtonBox(Modificar)
        self.btns_option.setObjectName(u"btns_option")
        self.btns_option.setGeometry(QRect(60, 180, 171, 32))
        self.btns_option.setOrientation(Qt.Horizontal)
        self.btns_option.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)
        self.layoutWidget = QWidget(Modificar)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 60, 231, 111))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_nombre = QLabel(self.layoutWidget)
        self.label_nombre.setObjectName(u"label_nombre")
        font1 = QFont()
        font1.setPointSize(9)
        self.label_nombre.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_nombre)

        self.in_nombre = QLineEdit(self.layoutWidget)
        self.in_nombre.setObjectName(u"in_nombre")
        self.in_nombre.setTabletTracking(False)
        self.in_nombre.setFocusPolicy(Qt.StrongFocus)
        self.in_nombre.setAutoFillBackground(False)
        self.in_nombre.setInputMethodHints(Qt.ImhNone)
        self.in_nombre.setMaxLength(32767)
        self.in_nombre.setFrame(True)
        self.in_nombre.setDragEnabled(False)
        self.in_nombre.setReadOnly(False)
        self.in_nombre.setClearButtonEnabled(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.in_nombre)

        self.label_cant = QLabel(self.layoutWidget)
        self.label_cant.setObjectName(u"label_cant")
        self.label_cant.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_cant)

        self.in_cant = QLineEdit(self.layoutWidget)
        self.in_cant.setObjectName(u"in_cant")
        self.in_cant.setTabletTracking(False)
        self.in_cant.setFocusPolicy(Qt.StrongFocus)
        self.in_cant.setAutoFillBackground(False)
        self.in_cant.setInputMethodHints(Qt.ImhNone)
        self.in_cant.setMaxLength(32767)
        self.in_cant.setFrame(True)
        self.in_cant.setDragEnabled(False)
        self.in_cant.setReadOnly(False)
        self.in_cant.setClearButtonEnabled(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.in_cant)

        self.label_precio = QLabel(self.layoutWidget)
        self.label_precio.setObjectName(u"label_precio")
        self.label_precio.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_precio)

        self.in_precio = QLineEdit(self.layoutWidget)
        self.in_precio.setObjectName(u"in_precio")
        self.in_precio.setTabletTracking(False)
        self.in_precio.setFocusPolicy(Qt.StrongFocus)
        self.in_precio.setAutoFillBackground(False)
        self.in_precio.setInputMethodHints(Qt.ImhNone)
        self.in_precio.setMaxLength(32767)
        self.in_precio.setFrame(True)
        self.in_precio.setDragEnabled(False)
        self.in_precio.setReadOnly(False)
        self.in_precio.setClearButtonEnabled(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.in_precio)

        self.label_descrip = QLabel(self.layoutWidget)
        self.label_descrip.setObjectName(u"label_descrip")
        self.label_descrip.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_descrip)

        self.in_descrip = QLineEdit(self.layoutWidget)
        self.in_descrip.setObjectName(u"in_descrip")
        self.in_descrip.setTabletTracking(False)
        self.in_descrip.setFocusPolicy(Qt.StrongFocus)
        self.in_descrip.setAutoFillBackground(False)
        self.in_descrip.setInputMethodHints(Qt.ImhNone)
        self.in_descrip.setMaxLength(32767)
        self.in_descrip.setFrame(True)
        self.in_descrip.setDragEnabled(False)
        self.in_descrip.setReadOnly(False)
        self.in_descrip.setClearButtonEnabled(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.in_descrip)

        self.notificacion = QLabel(Modificar)
        self.notificacion.setObjectName(u"notificacion")
        self.notificacion.setGeometry(QRect(100, 210, 161, 20))
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.notificacion.setFont(font2)
        self.notificacion.setLayoutDirection(Qt.LeftToRight)
        self.notificacion.setStyleSheet(u"color: #aa0000")
        self.notificacion.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.notificacion.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable)

        self.retranslateUi(Modificar)

        QMetaObject.connectSlotsByName(Modificar)
    # setupUi

    def retranslateUi(self, Modificar):
        Modificar.setWindowTitle(QCoreApplication.translate("Modificar", u"Dialog", None))
        self.titulo.setText(QCoreApplication.translate("Modificar", u"Modificar articulo", None))
        self.label_nombre.setText(QCoreApplication.translate("Modificar", u"Producto:", None))
        self.in_nombre.setInputMask("")
        self.in_nombre.setText("")
        self.in_nombre.setPlaceholderText(QCoreApplication.translate("Modificar", u"Ingrese nombre de producto", None))
        self.label_cant.setText(QCoreApplication.translate("Modificar", u"Cantidad:", None))
        self.in_cant.setInputMask("")
        self.in_cant.setText("")
        self.in_cant.setPlaceholderText(QCoreApplication.translate("Modificar", u"Ingrese valor numerico", None))
        self.label_precio.setText(QCoreApplication.translate("Modificar", u"Precio:", None))
        self.in_precio.setInputMask("")
        self.in_precio.setText("")
        self.in_precio.setPlaceholderText(QCoreApplication.translate("Modificar", u"Ingrese valor numerico", None))
        self.label_descrip.setText(QCoreApplication.translate("Modificar", u"Descripcion:", None))
        self.in_descrip.setInputMask("")
        self.in_descrip.setText("")
        self.in_descrip.setPlaceholderText(QCoreApplication.translate("Modificar", u"Ingrese una breve descripcion", None))
        self.notificacion.setText("")
    # retranslateUi

