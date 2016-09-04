# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_vent.ui'
#
# Created: Wed Aug 31 20:25:22 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_widget_vent(object):
    def setupUi(self, widget_vent):
        widget_vent.setObjectName("widget_vent")
        widget_vent.resize(671, 503)
        self.verticalLayout = QtGui.QVBoxLayout(widget_vent)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_vent = QtGui.QTableView(widget_vent)
        self.table_vent.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)

        self.table_vent.setObjectName("table_vent")
        self.verticalLayout.addWidget(self.table_vent)
        self.widget = QtGui.QWidget(widget_vent)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(450, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_agregar_vent = QtGui.QPushButton(self.widget)
        self.btn_agregar_vent.setObjectName("btn_agregar_vent")
        self.horizontalLayout.addWidget(self.btn_agregar_vent)
        self.btn_eliminar_vent = QtGui.QPushButton(self.widget)
        self.btn_eliminar_vent.setObjectName("btn_eliminar_vent")
        self.horizontalLayout.addWidget(self.btn_eliminar_vent)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(widget_vent)
        QtCore.QMetaObject.connectSlotsByName(widget_vent)

    def retranslateUi(self, widget_vent):
        widget_vent.setWindowTitle(QtGui.QApplication.translate("widget_vent", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_agregar_vent.setText(QtGui.QApplication.translate("widget_vent", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_eliminar_vent.setText(QtGui.QApplication.translate("widget_vent", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
