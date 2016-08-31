# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_form.ui'
#
# Created: Tue Aug 30 03:36:58 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(265, 177)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.savemarca = QtGui.QPushButton(Form)
        self.savemarca.setObjectName("savemarca")
        self.gridLayout.addWidget(self.savemarca, 3, 2, 1, 1)
        self.label_marca = QtGui.QLabel(Form)
        self.label_marca.setObjectName("label_marca")
        self.gridLayout.addWidget(self.label_marca, 0, 0, 1, 1)
        self.label_pais = QtGui.QLabel(Form)
        self.label_pais.setObjectName("label_pais")
        self.gridLayout.addWidget(self.label_pais, 1, 0, 1, 1)
        self.cancel = QtGui.QPushButton(Form)
        self.cancel.setObjectName("cancel")
        self.gridLayout.addWidget(self.cancel, 3, 1, 1, 1)
        self.label_img = QtGui.QLabel(Form)
        self.label_img.setObjectName("label_img")
        self.gridLayout.addWidget(self.label_img, 2, 0, 1, 1)
        self.t_pais = QtGui.QLineEdit(Form)
        self.t_pais.setObjectName("t_pais")
        self.gridLayout.addWidget(self.t_pais, 1, 1, 1, 2)
        self.t_marca = QtGui.QLineEdit(Form)
        self.t_marca.setObjectName("t_marca")
        self.gridLayout.addWidget(self.t_marca, 0, 1, 1, 2)
        self.t_img = QtGui.QLineEdit(Form)
        self.t_img.setObjectName("t_img")
        self.gridLayout.addWidget(self.t_img, 2, 1, 1, 1)
        self.buscar_img = QtGui.QPushButton(Form)
        self.buscar_img.setObjectName("buscar_img")
        self.gridLayout.addWidget(self.buscar_img, 2, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Marca", None, QtGui.QApplication.UnicodeUTF8))
        self.savemarca.setText(QtGui.QApplication.translate("Form", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_marca.setText(QtGui.QApplication.translate("Form", "Marca", None, QtGui.QApplication.UnicodeUTF8))
        self.label_pais.setText(QtGui.QApplication.translate("Form", "Pais:", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel.setText(QtGui.QApplication.translate("Form", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_img.setText(QtGui.QApplication.translate("Form", "Imagen:", None, QtGui.QApplication.UnicodeUTF8))
        self.buscar_img.setText(QtGui.QApplication.translate("Form", "Buscar", None, QtGui.QApplication.UnicodeUTF8))

