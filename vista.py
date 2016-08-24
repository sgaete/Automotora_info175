# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'base.ui'
#
# Created: Wed Aug 24 19:08:21 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 705)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 705))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 705))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(5, 0, 1270, 700))
        self.tabWidget.setObjectName("tabWidget")
        self.marca_tab = QtGui.QWidget()
        self.marca_tab.setObjectName("marca_tab")
        self.tabWidget.addTab(self.marca_tab, "")
        self.modelo_tab = QtGui.QWidget()
        self.modelo_tab.setObjectName("modelo_tab")
        self.tabWidget.addTab(self.modelo_tab, "")
        self.cliente_tab = QtGui.QWidget()
        self.cliente_tab.setObjectName("cliente_tab")
        self.tabWidget.addTab(self.cliente_tab, "")
        self.venta_tab = QtGui.QWidget()
        self.venta_tab.setObjectName("venta_tab")
        self.tabWidget.addTab(self.venta_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Automotora INFO175", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.marca_tab), QtGui.QApplication.translate("MainWindow", "Marcas", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.modelo_tab), QtGui.QApplication.translate("MainWindow", "Modelos", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cliente_tab), QtGui.QApplication.translate("MainWindow", "Clientes", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.venta_tab), QtGui.QApplication.translate("MainWindow", "Ventas", None, QtGui.QApplication.UnicodeUTF8))

