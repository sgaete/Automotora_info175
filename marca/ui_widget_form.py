# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_form.ui'
#
# Created: Mon Sep  5 14:00:27 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(583, 177)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        Form.setFont(font)
        self.savemarca = QtGui.QPushButton(Form)
        self.savemarca.setGeometry(QtCore.QRect(170, 130, 181, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.savemarca.setFont(font)
        self.savemarca.setCursor(QtCore.Qt.PointingHandCursor)
        self.savemarca.setObjectName("savemarca")
        self.label_marca = QtGui.QLabel(Form)
        self.label_marca.setGeometry(QtCore.QRect(30, 20, 61, 17))
        self.label_marca.setObjectName("label_marca")
        self.label_pais = QtGui.QLabel(Form)
        self.label_pais.setGeometry(QtCore.QRect(30, 60, 41, 17))
        self.label_pais.setObjectName("label_pais")
        self.cancel = QtGui.QPushButton(Form)
        self.cancel.setGeometry(QtCore.QRect(380, 130, 181, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.cancel.setFont(font)
        self.cancel.setCursor(QtCore.Qt.PointingHandCursor)
        self.cancel.setObjectName("cancel")
        self.label_img = QtGui.QLabel(Form)
        self.label_img.setGeometry(QtCore.QRect(30, 100, 55, 17))
        self.label_img.setObjectName("label_img")
        self.t_pais = QtGui.QLineEdit(Form)
        self.t_pais.setGeometry(QtCore.QRect(90, 54, 471, 27))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.t_pais.setFont(font)
        self.t_pais.setObjectName("t_pais")
        self.t_marca = QtGui.QLineEdit(Form)
        self.t_marca.setGeometry(QtCore.QRect(90, 15, 471, 27))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.t_marca.setFont(font)
        self.t_marca.setObjectName("t_marca")
        self.t_img = QtGui.QLineEdit(Form)
        self.t_img.setGeometry(QtCore.QRect(90, 93, 371, 27))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.t_img.setFont(font)
        self.t_img.setReadOnly(True)
        self.t_img.setObjectName("t_img")
        self.buscar_img = QtGui.QPushButton(Form)
        self.buscar_img.setGeometry(QtCore.QRect(470, 90, 91, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.buscar_img.setFont(font)
        self.buscar_img.setCursor(QtCore.Qt.PointingHandCursor)
        self.buscar_img.setObjectName("buscar_img")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.t_marca, self.t_pais)
        Form.setTabOrder(self.t_pais, self.t_img)
        Form.setTabOrder(self.t_img, self.buscar_img)
        Form.setTabOrder(self.buscar_img, self.savemarca)
        Form.setTabOrder(self.savemarca, self.cancel)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Marca", None, QtGui.QApplication.UnicodeUTF8))
        self.savemarca.setText(QtGui.QApplication.translate("Form", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_marca.setText(QtGui.QApplication.translate("Form", "Marca:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_pais.setText(QtGui.QApplication.translate("Form", "País:", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel.setText(QtGui.QApplication.translate("Form", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_img.setText(QtGui.QApplication.translate("Form", "Logo:", None, QtGui.QApplication.UnicodeUTF8))
        self.t_pais.setPlaceholderText(QtGui.QApplication.translate("Form", "Ingrese país", None, QtGui.QApplication.UnicodeUTF8))
        self.t_marca.setPlaceholderText(QtGui.QApplication.translate("Form", "Ingrese marca", None, QtGui.QApplication.UnicodeUTF8))
        self.t_img.setPlaceholderText(QtGui.QApplication.translate("Form", "Seleccione la ruta presionando en Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.buscar_img.setText(QtGui.QApplication.translate("Form", "Buscar", None, QtGui.QApplication.UnicodeUTF8))

