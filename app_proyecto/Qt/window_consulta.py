# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_consulta.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Consulta(object):
    def setupUi(self, Consulta):
        if not Consulta.objectName():
            Consulta.setObjectName(u"Consulta")
        Consulta.resize(564, 352)
        Consulta.setToolTipDuration(0)
        Consulta.setStyleSheet(u"QApplication::setStyle(\"fusion\");\n"
"")
        self.catalogo_list = QTableWidget(Consulta)
        if (self.catalogo_list.columnCount() < 5):
            self.catalogo_list.setColumnCount(5)
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QFont.PreferAntialias)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font);
        self.catalogo_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.catalogo_list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.catalogo_list.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.catalogo_list.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.catalogo_list.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.catalogo_list.rowCount() < 7):
            self.catalogo_list.setRowCount(7)
        font1 = QFont()
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        __qtablewidgetitem5.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsEnabled);
        self.catalogo_list.setItem(0, 0, __qtablewidgetitem5)
        self.catalogo_list.setObjectName(u"catalogo_list")
        self.catalogo_list.setGeometry(QRect(20, 90, 521, 211))
        self.catalogo_list.setMinimumSize(QSize(521, 0))
        self.catalogo_list.setFrameShadow(QFrame.Raised)
        self.catalogo_list.setAutoScroll(True)
        self.catalogo_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.catalogo_list.setAlternatingRowColors(True)
        self.catalogo_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.catalogo_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.catalogo_list.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.catalogo_list.setShowGrid(True)
        self.catalogo_list.setGridStyle(Qt.CustomDashLine)
        self.catalogo_list.setSortingEnabled(True)
        self.catalogo_list.setWordWrap(True)
        self.catalogo_list.setCornerButtonEnabled(True)
        self.catalogo_list.setRowCount(7)
        self.catalogo_list.horizontalHeader().setVisible(True)
        self.catalogo_list.horizontalHeader().setCascadingSectionResizes(False)
        self.catalogo_list.horizontalHeader().setMinimumSectionSize(30)
        self.catalogo_list.horizontalHeader().setDefaultSectionSize(101)
        self.catalogo_list.horizontalHeader().setHighlightSections(False)
        self.catalogo_list.horizontalHeader().setProperty("showSortIndicator", False)
        self.catalogo_list.horizontalHeader().setStretchLastSection(True)
        self.catalogo_list.verticalHeader().setVisible(False)
        self.catalogo_list.verticalHeader().setCascadingSectionResizes(False)
        self.catalogo_list.verticalHeader().setMinimumSectionSize(23)
        self.catalogo_list.verticalHeader().setDefaultSectionSize(26)
        self.catalogo_list.verticalHeader().setHighlightSections(False)
        self.catalogo_list.verticalHeader().setProperty("showSortIndicator", True)
        self.catalogo_list.verticalHeader().setStretchLastSection(True)
        self.btn_cat_full = QPushButton(Consulta)
        self.btn_cat_full.setObjectName(u"btn_cat_full")
        self.btn_cat_full.setGeometry(QRect(150, 310, 121, 31))
        self.btn_volver = QPushButton(Consulta)
        self.btn_volver.setObjectName(u"btn_volver")
        self.btn_volver.setGeometry(QRect(280, 310, 121, 31))
        self.layoutWidget = QWidget(Consulta)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(19, 60, 521, 25))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_nombre = QLabel(self.layoutWidget)
        self.label_nombre.setObjectName(u"label_nombre")
        font2 = QFont()
        font2.setPointSize(9)
        self.label_nombre.setFont(font2)

        self.horizontalLayout.addWidget(self.label_nombre)

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

        self.horizontalLayout.addWidget(self.in_nombre)

        self.label_descripcion = QLabel(self.layoutWidget)
        self.label_descripcion.setObjectName(u"label_descripcion")
        self.label_descripcion.setFont(font2)

        self.horizontalLayout.addWidget(self.label_descripcion)

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

        self.horizontalLayout.addWidget(self.in_descrip)

        self.btn_buscar = QPushButton(self.layoutWidget)
        self.btn_buscar.setObjectName(u"btn_buscar")

        self.horizontalLayout.addWidget(self.btn_buscar)

        self.titulo = QLabel(Consulta)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(160, 10, 221, 45))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.titulo.setFont(font3)
        self.titulo.setAlignment(Qt.AlignCenter)
        self.notificacion = QLabel(Consulta)
        self.notificacion.setObjectName(u"notificacion")
        self.notificacion.setGeometry(QRect(310, 30, 231, 20))
        font4 = QFont()
        font4.setBold(True)
        font4.setWeight(75)
        self.notificacion.setFont(font4)
        self.notificacion.setLayoutDirection(Qt.LeftToRight)
        self.notificacion.setStyleSheet(u"color: #aa0000")
        self.notificacion.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.notificacion.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable)

        self.retranslateUi(Consulta)

        QMetaObject.connectSlotsByName(Consulta)
    # setupUi

    def retranslateUi(self, Consulta):
        Consulta.setWindowTitle(QCoreApplication.translate("Consulta", u"Form", None))
        ___qtablewidgetitem = self.catalogo_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Consulta", u"ID", None));
        ___qtablewidgetitem1 = self.catalogo_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Consulta", u"Producto", None));
        ___qtablewidgetitem2 = self.catalogo_list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Consulta", u"Cantidad", None));
        ___qtablewidgetitem3 = self.catalogo_list.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Consulta", u"Precio", None));
        ___qtablewidgetitem4 = self.catalogo_list.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Consulta", u"Descripcion", None));

        __sortingEnabled = self.catalogo_list.isSortingEnabled()
        self.catalogo_list.setSortingEnabled(False)
        self.catalogo_list.setSortingEnabled(__sortingEnabled)

        self.btn_cat_full.setText(QCoreApplication.translate("Consulta", u"Catalogo completo", None))
        self.btn_volver.setText(QCoreApplication.translate("Consulta", u"Volver", None))
        self.label_nombre.setText(QCoreApplication.translate("Consulta", u"Producto:", None))
        self.in_nombre.setInputMask("")
        self.in_nombre.setText("")
        self.in_nombre.setPlaceholderText(QCoreApplication.translate("Consulta", u"Ingrese nombre de producto", None))
        self.label_descripcion.setText(QCoreApplication.translate("Consulta", u"Descripcion", None))
        self.in_descrip.setInputMask("")
        self.in_descrip.setText("")
        self.in_descrip.setPlaceholderText(QCoreApplication.translate("Consulta", u"Ingrese descripcion", None))
        self.btn_buscar.setText(QCoreApplication.translate("Consulta", u"Buscar", None))
        self.titulo.setText(QCoreApplication.translate("Consulta", u"Catalogo", None))
        self.notificacion.setText("")
    # retranslateUi

