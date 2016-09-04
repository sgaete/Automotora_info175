# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_form_cli.ui'
#
# Created: Sat Sep  3 23:04:40 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_form_cliente(object):
    def setupUi(self, form_cliente):
        form_cliente.setObjectName("form_cliente")
        form_cliente.resize(352, 210)
        self.gridLayout = QtGui.QGridLayout(form_cliente)
        self.gridLayout.setObjectName("gridLayout")
        self.label_1 = QtGui.QLabel(form_cliente)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.telefono = QtGui.QLineEdit(form_cliente)
	self.telefono.setMaxLength(12)
        self.telefono.setObjectName("telefono")
        self.gridLayout.addWidget(self.telefono, 3, 1, 1, 2)
        self.label_5 = QtGui.QLabel(form_cliente)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_3 = QtGui.QLabel(form_cliente)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.rut = QtGui.QLineEdit(form_cliente)
        self.rut.setMaxLength(8)
        self.rut.setObjectName("rut")
        self.gridLayout.addWidget(self.rut, 0, 1, 1, 2)
        self.apellidos = QtGui.QLineEdit(form_cliente)
        self.apellidos.setObjectName("apellidos")
        self.gridLayout.addWidget(self.apellidos, 2, 1, 1, 2)
        self.label_4 = QtGui.QLabel(form_cliente)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.correo = QtGui.QLineEdit(form_cliente)
        self.correo.setObjectName("correo")
        self.gridLayout.addWidget(self.correo, 4, 1, 1, 2)
        self.label_2 = QtGui.QLabel(form_cliente)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.nombres = QtGui.QLineEdit(form_cliente)
        self.nombres.setObjectName("nombres")
        self.gridLayout.addWidget(self.nombres, 1, 1, 1, 2)
        self.btn_aceptar = QtGui.QPushButton(form_cliente)
        self.btn_aceptar.setObjectName("btn_aceptar")
        self.gridLayout.addWidget(self.btn_aceptar, 6, 1, 1, 1)
        self.btn_cancelar = QtGui.QPushButton(form_cliente)
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.gridLayout.addWidget(self.btn_cancelar, 6, 2, 1, 1)

        self.retranslateUi(form_cliente)
        QtCore.QMetaObject.connectSlotsByName(form_cliente)
        form_cliente.setTabOrder(self.rut, self.nombres)
        form_cliente.setTabOrder(self.nombres, self.apellidos)
        form_cliente.setTabOrder(self.apellidos, self.telefono)
        form_cliente.setTabOrder(self.telefono, self.correo)
        form_cliente.setTabOrder(self.correo, self.btn_aceptar)
        form_cliente.setTabOrder(self.btn_aceptar, self.btn_cancelar)

    def retranslateUi(self, form_cliente):
        form_cliente.setWindowTitle(QtGui.QApplication.translate("form_cliente", "Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.label_1.setText(QtGui.QApplication.translate("form_cliente", "RUT:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("form_cliente", "Correo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("form_cliente", "Apellidos:", None, QtGui.QApplication.UnicodeUTF8))
        self.rut.setPlaceholderText(QtGui.QApplication.translate("form_cliente", "Sin puntos ni dígito verificador", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("form_cliente", "Teléfono:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("form_cliente", "Nombres:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_aceptar.setText(QtGui.QApplication.translate("form_cliente", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancelar.setText(QtGui.QApplication.translate("form_cliente", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

