# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Fri Aug 26 23:49:45 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1280, 705)
        self.centralwidget = QtGui.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Abyssinica SIL")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 27))
        self.menubar.setObjectName("menubar")
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName("menu")
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
        self.menu.addAction(self.actionMarcas)
        self.menu.addAction(self.actionModelos)
        self.menu.addAction(self.actionClientes)
        self.menu.addAction(self.actionVentas)
        self.menu.addSeparator()
        self.menu.addAction(self.actionCerrar_Sesi_n)
        self.menu.addAction(self.actionSalir)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        Main.setWindowTitle(QtGui.QApplication.translate("Main", "Pantalla principal", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Main", "<html><head/><body><p>AQUI VA UNA IMAGEN BONITA!!!</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.menu.setTitle(QtGui.QApplication.translate("Main", "Menú", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMarcas.setText(QtGui.QApplication.translate("Main", "Marcas", None, QtGui.QApplication.UnicodeUTF8))
        self.actionModelos.setText(QtGui.QApplication.translate("Main", "Modelos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClientes.setText(QtGui.QApplication.translate("Main", "Clientes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVentas.setText(QtGui.QApplication.translate("Main", "Ventas", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCerrar_Sesi_n.setText(QtGui.QApplication.translate("Main", "Cerrar Sesión", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setText(QtGui.QApplication.translate("Main", "Salir", None, QtGui.QApplication.UnicodeUTF8))

