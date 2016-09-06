# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Mon Sep  5 22:29:42 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1280, 705)
        self.centralwidget = QtGui.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 10, 631, 171))
        font = QtGui.QFont()
        font.setFamily("Abyssinica SIL")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 200, 1001, 441))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 25))
        self.menubar.setObjectName("menubar")
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menuAcerca_de = QtGui.QMenu(self.menubar)
        self.menuAcerca_de.setObjectName("menuAcerca_de")
        Main.setMenuBar(self.menubar)
        self.actionMarcas = QtGui.QAction(Main)
        self.actionMarcas.setObjectName("actionMarcas")
        self.actionModelos = QtGui.QAction(Main)
        self.actionModelos.setObjectName("actionModelos")
        self.actionClientes = QtGui.QAction(Main)
        self.actionClientes.setObjectName("actionClientes")
        self.actionVentas = QtGui.QAction(Main)
        self.actionVentas.setObjectName("actionVentas")
        self.actionCerrar_Sesi_n = QtGui.QAction(Main)
        self.actionCerrar_Sesi_n.setObjectName("actionCerrar_Sesi_n")
        self.actionSalir = QtGui.QAction(Main)
        self.actionSalir.setObjectName("actionSalir")
        self.actionAcerca_de = QtGui.QAction(Main)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.menu.addAction(self.actionMarcas)
        self.menu.addAction(self.actionModelos)
        self.menu.addAction(self.actionClientes)
        self.menu.addAction(self.actionVentas)
        self.menu.addSeparator()
        self.menu.addAction(self.actionSalir)
        self.menuAcerca_de.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuAcerca_de.menuAction())

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        Main.setWindowTitle(QtGui.QApplication.translate("Main", "Pantalla principal", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Abyssinica SIL\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir=\'rtl\' style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt; font-weight:600;\">Automotora INFO175</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.menu.setTitle(QtGui.QApplication.translate("Main", "Menú", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAcerca_de.setTitle(QtGui.QApplication.translate("Main", "Ayuda", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMarcas.setText(QtGui.QApplication.translate("Main", "Marcas", None, QtGui.QApplication.UnicodeUTF8))
        self.actionModelos.setText(QtGui.QApplication.translate("Main", "Modelos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClientes.setText(QtGui.QApplication.translate("Main", "Clientes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVentas.setText(QtGui.QApplication.translate("Main", "Ventas", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCerrar_Sesi_n.setText(QtGui.QApplication.translate("Main", "Cerrar Sesión", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setText(QtGui.QApplication.translate("Main", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAcerca_de.setText(QtGui.QApplication.translate("Main", "Acerca de...", None, QtGui.QApplication.UnicodeUTF8))

