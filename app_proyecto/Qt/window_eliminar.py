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
        Eliminar.resize(296, 153)
        self.btns_option = QDialogButtonBox(Eliminar)
        self.btns_option.setObjectName(u"btns_option")
        self.btns_option.setGeometry(QRect(60, 100, 171, 32))
        self.btns_option.setOrientation(Qt.Horizontal)
        self.btns_option.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.layoutWidget = QWidget(Eliminar)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 60, 231, 31))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_nombre = QLabel(self.layoutWidget)
        self.label_nombre.setObjectName(u"label_nombre")
        font = QFont()
        font.setPointSize(9)
        self.label_nombre.setFont(font)

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

        self.titulo = QLabel(Eliminar)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(30, 10, 221, 45))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.titulo.setFont(font1)
        self.titulo.setAlignment(Qt.AlignCenter)
        self.notificacion = QLabel(Eliminar)
        self.notificacion.setObjectName(u"notificacion")
        self.notificacion.setGeometry(QRect(100, 130, 161, 20))
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.notificacion.setFont(font2)
        self.notificacion.setLayoutDirection(Qt.LeftToRight)
        self.notificacion.setStyleSheet(u"color: #aa0000")
        self.notificacion.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.notificacion.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable)

        self.retranslateUi(Eliminar)

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
    # retranslateUi

