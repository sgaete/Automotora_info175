#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from ui_widget_modelo import Ui_widget_modelo
import model as model_db


class Widget_modelo(QtGui.QWidget):
    """
    Modelo
    """
    def __init__(self, parent=None):
        super(Widget_modelo, self).__init__(parent)
        self.ui = Ui_widget_modelo()
        self.ui.setupUi(self)
        self.load_data()
        self.load_combo()
        self.actions()

    def actions(self):
    	self.ui.btn_resetmarca.clicked.connect(self.ui.comboMarcas.clear) 
    	self.ui.busca_modelo.editingFinished.connect(self.filter_busca)#textChanged

    def load_data(self):
    	modelos = model_db.get_all_modelos()
    	self.data = QtGui.QStandardItemModel(len(modelos), 3)

    	self.data.setHorizontalHeaderItem(0,QtGui.QStandardItem(u"Modelo"))
    	self.data.setHorizontalHeaderItem(1,QtGui.QStandardItem(u"Marca"))
    	self.data.setHorizontalHeaderItem(2,QtGui.QStandardItem(u"Precio"))

    	for r, row in enumerate(modelos):
            index = self.data.index(r, 0, QtCore.QModelIndex())
            self.data.setData(index, row['modelo'])
            index = self.data.index(r, 1, QtCore.QModelIndex())
            self.data.setData(index, row['marca_id'])
            index = self.data.index(r, 2, QtCore.QModelIndex())
            self.data.setData(index, row['precio_lista'])
        self.ui.table_mod.setModel(self.data)
    	self.ui.table_mod.horizontalHeader().setResizeMode(0, self.ui.table_mod.horizontalHeader().Stretch)
        self.ui.table_mod.horizontalHeader().setResizeMode(1, self.ui.table_mod.horizontalHeader().Stretch)
        self.ui.table_mod.horizontalHeader().setResizeMode(2, self.ui.table_mod.horizontalHeader().Stretch)


    def load_combo(self):
    	marcas = model_db.get_marcas()
    	#self.ui.comboMarcas.addItem(marcas['nombre'][1])