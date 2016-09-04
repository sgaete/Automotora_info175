# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_cliente.ui'
#
# Created: Thu Sep  1 00:15:42 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_widget_cliente(object):
    def setupUi(self, widget_cliente):
        widget_cliente.setObjectName("widget_cliente")
        widget_cliente.resize(534, 394)
        self.verticalLayout = QtGui.QVBoxLayout(widget_cliente)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_cli = QtGui.QTableView(widget_cliente)
        self.table_cli.setAlternatingRowColors(True)
        self.table_cli.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.table_cli.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_cli.setSortingEnabled(True)
        self.table_cli.setObjectName("table_cli")
        self.verticalLayout.addWidget(self.table_cli)
        self.widget = QtGui.QWidget(widget_cliente)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(463, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_agregar_cli = QtGui.QPushButton(self.widget)
        self.btn_agregar_cli.setObjectName("btn_agregar_cli")
        self.horizontalLayout.addWidget(self.btn_agregar_cli)
        self.btn_editar_cli = QtGui.QPushButton(self.widget)
        self.btn_editar_cli.setObjectName("btn_editar_cli")
        self.horizontalLayout.addWidget(self.btn_editar_cli)
        self.btn_borrar_cli = QtGui.QPushButton(self.widget)
        self.btn_borrar_cli.setObjectName("btn_borrar_cli")
        self.horizontalLayout.addWidget(self.btn_borrar_cli)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(widget_cliente)
        QtCore.QMetaObject.connectSlotsByName(widget_cliente)

    def retranslateUi(self, widget_cliente):
        widget_cliente.setWindowTitle(QtGui.QApplication.translate("widget_cliente", "Clientes", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_agregar_cli.setText(QtGui.QApplication.translate("widget_cliente", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_editar_cli.setText(QtGui.QApplication.translate("widget_cliente", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_borrar_cli.setText(QtGui.QApplication.translate("widget_cliente", "Borrar", None, QtGui.QApplication.UnicodeUTF8))

