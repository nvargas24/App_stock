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
        Consulta.resize(744, 510)
        Consulta.setToolTipDuration(0)
        Consulta.setStyleSheet(u"/*QApplication::setStyle(\"fusion\");*/\n"
"\n"
"background-color: #EAEAEA;\n"
"")
        self.catalogo_list = QTableWidget(Consulta)
        if (self.catalogo_list.columnCount() < 5):
            self.catalogo_list.setColumnCount(5)
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QFont.PreferAntialias)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font);
        self.catalogo_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font1 = QFont()
        font1.setPointSize(12)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font1);
        self.catalogo_list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font1);
        self.catalogo_list.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font1);
        self.catalogo_list.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font1);
        self.catalogo_list.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.catalogo_list.rowCount() < 10):
            self.catalogo_list.setRowCount(10)
        font2 = QFont()
        font2.setPointSize(12)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferDefault)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font2);
        __qtablewidgetitem5.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsEnabled);
        self.catalogo_list.setItem(0, 0, __qtablewidgetitem5)
        self.catalogo_list.setObjectName(u"catalogo_list")
        self.catalogo_list.setGeometry(QRect(31, 116, 671, 301))
        self.catalogo_list.setMinimumSize(QSize(521, 0))
        self.catalogo_list.setFont(font1)
        self.catalogo_list.setAutoFillBackground(False)
        self.catalogo_list.setStyleSheet(u"QTableWidget {\n"
"    background-color: #ffffff; /* Color de fondo de la tabla */\n"
"    border: 1px solid #c2c2c2; /* Borde de la tabla */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #0078D7; /* Tono celeste medio oscuro */\n"
"    color: white; /* Texto en blanco */\n"
"    selection-color: white; /* Texto en blanco al seleccionar */\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #8CB8E6; /* Color de fondo de celda seleccionada */\n"
"    color: #ffffff; /* Color de texto de celda seleccionada */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #ffffff;\n"
"    width: 10px;\n"
"    margin: 0px 0 0px 0;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #e1e1e1;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #c2c2c2;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background: #ffffff;\n"
"    height: 0px;\n"
"    subcontrol-positi"
                        "on: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: #ffffff;\n"
"    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"    color: none;\n"
"    margin: 0px 0 0px 0;\n"
"    padding: 0px;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
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
        self.catalogo_list.setRowCount(10)
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
        self.titulo = QLabel(Consulta)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(250, 20, 221, 45))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setWeight(75)
        self.titulo.setFont(font3)
        self.titulo.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(Consulta)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(31, 426, 671, 41))
        self.horizontalLayout_1 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.horizontalLayout_1.setContentsMargins(150, 0, 150, 0)
        self.btn_cat_full = QPushButton(self.layoutWidget)
        self.btn_cat_full.setObjectName(u"btn_cat_full")
        self.btn_cat_full.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cat_full.sizePolicy().hasHeightForWidth())
        self.btn_cat_full.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setBold(True)
        font4.setWeight(75)
        self.btn_cat_full.setFont(font4)
        self.btn_cat_full.setStyleSheet(u"QPushButton {\n"
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
        self.btn_cat_full.setInputMethodHints(Qt.ImhSensitiveData|Qt.ImhUppercaseOnly)
        self.btn_cat_full.setCheckable(True)
        self.btn_cat_full.setChecked(True)
        self.btn_cat_full.setAutoRepeat(True)
        self.btn_cat_full.setAutoRepeatDelay(150)
        self.btn_cat_full.setAutoDefault(False)
        self.btn_cat_full.setFlat(False)

        self.horizontalLayout_1.addWidget(self.btn_cat_full)

        self.btn_volver = QPushButton(self.layoutWidget)
        self.btn_volver.setObjectName(u"btn_volver")
        sizePolicy.setHeightForWidth(self.btn_volver.sizePolicy().hasHeightForWidth())
        self.btn_volver.setSizePolicy(sizePolicy)
        self.btn_volver.setFont(font4)
        self.btn_volver.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_1.addWidget(self.btn_volver)

        self.notificacion = QLabel(Consulta)
        self.notificacion.setObjectName(u"notificacion")
        self.notificacion.setGeometry(QRect(180, 470, 241, 20))
        font5 = QFont()
        font5.setBold(True)
        font5.setWeight(75)
        self.notificacion.setFont(font5)
        self.notificacion.setLayoutDirection(Qt.LeftToRight)
        self.notificacion.setStyleSheet(u"color: #aa0000")
        self.notificacion.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.notificacion.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable)
        self.layoutWidget_2 = QWidget(Consulta)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(30, 70, 671, 37))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_nombre = QLabel(self.layoutWidget_2)
        self.label_nombre.setObjectName(u"label_nombre")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_nombre.sizePolicy().hasHeightForWidth())
        self.label_nombre.setSizePolicy(sizePolicy1)
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(14)
        self.label_nombre.setFont(font6)

        self.horizontalLayout_2.addWidget(self.label_nombre)

        self.in_nombre = QLineEdit(self.layoutWidget_2)
        self.in_nombre.setObjectName(u"in_nombre")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.in_nombre.sizePolicy().hasHeightForWidth())
        self.in_nombre.setSizePolicy(sizePolicy2)
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setBold(False)
        font7.setWeight(50)
        self.in_nombre.setFont(font7)
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
"}\n"
"")
        self.in_nombre.setInputMethodHints(Qt.ImhNone)
        self.in_nombre.setMaxLength(32767)
        self.in_nombre.setFrame(True)
        self.in_nombre.setDragEnabled(False)
        self.in_nombre.setReadOnly(False)
        self.in_nombre.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.in_nombre)

        self.label_descripcion = QLabel(self.layoutWidget_2)
        self.label_descripcion.setObjectName(u"label_descripcion")
        sizePolicy1.setHeightForWidth(self.label_descripcion.sizePolicy().hasHeightForWidth())
        self.label_descripcion.setSizePolicy(sizePolicy1)
        self.label_descripcion.setFont(font6)

        self.horizontalLayout_2.addWidget(self.label_descripcion)

        self.in_descrip = QLineEdit(self.layoutWidget_2)
        self.in_descrip.setObjectName(u"in_descrip")
        sizePolicy2.setHeightForWidth(self.in_descrip.sizePolicy().hasHeightForWidth())
        self.in_descrip.setSizePolicy(sizePolicy2)
        self.in_descrip.setFont(font7)
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
"}\n"
"")
        self.in_descrip.setInputMethodHints(Qt.ImhNone)
        self.in_descrip.setMaxLength(32767)
        self.in_descrip.setFrame(True)
        self.in_descrip.setDragEnabled(False)
        self.in_descrip.setReadOnly(False)
        self.in_descrip.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.in_descrip)

        self.btn_buscar = QPushButton(self.layoutWidget_2)
        self.btn_buscar.setObjectName(u"btn_buscar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_buscar.sizePolicy().hasHeightForWidth())
        self.btn_buscar.setSizePolicy(sizePolicy3)
        self.btn_buscar.setFont(font4)
        self.btn_buscar.setStyleSheet(u"QPushButton {\n"
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
        self.btn_buscar.setCheckable(False)
        self.btn_buscar.setChecked(False)
        self.btn_buscar.setAutoRepeat(False)
        self.btn_buscar.setAutoExclusive(False)

        self.horizontalLayout_2.addWidget(self.btn_buscar)


        self.retranslateUi(Consulta)

        self.btn_cat_full.setDefault(False)


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

        self.titulo.setText(QCoreApplication.translate("Consulta", u"Catalogo", None))
        self.btn_cat_full.setText(QCoreApplication.translate("Consulta", u"Catalogo completo", None))
        self.btn_volver.setText(QCoreApplication.translate("Consulta", u"Volver", None))
        self.notificacion.setText("")
        self.label_nombre.setText(QCoreApplication.translate("Consulta", u"Producto:", None))
        self.in_nombre.setInputMask("")
        self.in_nombre.setText("")
        self.in_nombre.setPlaceholderText(QCoreApplication.translate("Consulta", u"Ingrese nombre de producto", None))
        self.label_descripcion.setText(QCoreApplication.translate("Consulta", u"Descripcion", None))
        self.in_descrip.setInputMask("")
        self.in_descrip.setText("")
        self.in_descrip.setPlaceholderText(QCoreApplication.translate("Consulta", u"Ingrese descripcion", None))
        self.btn_buscar.setText(QCoreApplication.translate("Consulta", u"Buscar", None))
    # retranslateUi

