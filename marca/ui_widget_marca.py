# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_marca.ui'
#
# Created: Sun Aug 28 15:13:06 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_widget_marca(object):
    def setupUi(self, widget_marca):
        widget_marca.setObjectName("widget_marca")
        widget_marca.resize(1098, 722)
        self.gridLayout = QtGui.QGridLayout(widget_marca)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtGui.QWidget(widget_marca)
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtGui.QSpacerItem(509, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.btn_agrega_marc = QtGui.QPushButton(self.widget)
        self.btn_agrega_marc.setObjectName("btn_agrega_marc")
        self.horizontalLayout_5.addWidget(self.btn_agrega_marc)
        self.btn_edita_marc = QtGui.QPushButton(self.widget)
        self.btn_edita_marc.setObjectName("btn_edita_marc")
        self.horizontalLayout_5.addWidget(self.btn_edita_marc)
        self.btn_borra_marc = QtGui.QPushButton(self.widget)
        self.btn_borra_marc.setObjectName("btn_borra_marc")
        self.horizontalLayout_5.addWidget(self.btn_borra_marc)
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)
        self.table_marc = QtGui.QTableView(widget_marca)
        self.table_marc.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table_marc.setAlternatingRowColors(True)
        self.table_marc.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.table_marc.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_marc.setSortingEnabled(True)
        self.table_marc.setObjectName("table_marc")
        self.gridLayout.addWidget(self.table_marc, 0, 0, 1, 1)
        self.line = QtGui.QFrame(widget_marca)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 1, 2, 1)
        self.widget_4 = QtGui.QWidget(widget_marca)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtGui.QLabel(self.widget_4)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.gridLayout.addWidget(self.widget_4, 0, 2, 2, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(2, 1)

        self.retranslateUi(widget_marca)
        QtCore.QMetaObject.connectSlotsByName(widget_marca)

    def retranslateUi(self, widget_marca):
        widget_marca.setWindowTitle(QtGui.QApplication.translate("widget_marca", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_agrega_marc.setText(QtGui.QApplication.translate("widget_marca", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_edita_marc.setText(QtGui.QApplication.translate("widget_marca", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_borra_marc.setText(QtGui.QApplication.translate("widget_marca", "Borrar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("widget_marca", "Imagen", None, QtGui.QApplication.UnicodeUTF8))

