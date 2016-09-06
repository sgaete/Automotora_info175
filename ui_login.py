# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(270, 110)
        Form.setMinimumSize(QtCore.QSize(270, 110))
        Form.setMaximumSize(QtCore.QSize(270, 110))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.usuario = QtGui.QLineEdit(Form)
        self.usuario.setObjectName("usuario")
        self.gridLayout.addWidget(self.usuario, 0, 1, 1, 2)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pass_ = QtGui.QLineEdit(Form)
        self.pass_.setEchoMode(QtGui.QLineEdit.Password)
        self.pass_.setObjectName("pass_")
        self.gridLayout.addWidget(self.pass_, 1, 1, 1, 2)
        self.btn_ca = QtGui.QPushButton(Form)
        self.btn_ca.setObjectName("btn_ca")
        self.gridLayout.addWidget(self.btn_ca, 2, 2, 1, 1)
        self.btn_ac = QtGui.QPushButton(Form)
        self.btn_ac.setObjectName("btn_ac")
        self.gridLayout.addWidget(self.btn_ac, 2, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Usuario:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Contraseña:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_ca.setText(QtGui.QApplication.translate("Form", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_ac.setText(QtGui.QApplication.translate("Form", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))

