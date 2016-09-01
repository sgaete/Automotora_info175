#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from ui_widget_modelo import Ui_widget_modelo
import modelo.model_modelo as model_db


class Widget_modelo(QtGui.QWidget):
    """
    Modelo
    """
    #setColumnHidden(column, hide) para manejar ids con imagenes
    def __init__(self, parent=None):
        super(Widget_modelo, self).__init__(parent)
        self.ui = Ui_widget_modelo()
        self.ui.setupUi(self)
        self.load_data()
        self.load_combo()
        self.actions()

    def load_data(self):
    	modelos = model_db.get_all_modelos()
    	self.load_tabla(modelos)

    def actions(self):
    	#self.ui.btn_reset_marca.clicked.connect()
    	self.ui.combo_Marcas.activated.connect(self.filter_marca)
    	self.ui.busca_mod.editingFinished.connect(self.filter_busca)#textChanged
    	self.ui.table_mod.clicked.connect(self.load_desc)

    #filtra segun el buscador de texto
    def filter_busca(self):
    	self.ui.table_mod.clearSpans()
    	if(len(self.ui.busca_mod.text()) > 0):#falta trimear
	    	modelos = model_db.filter_by_busca(self.ui.busca_mod.text())
	    	self.load_tabla(modelos)
    	else:
    		self.load_data()

    #filtra segun las marcas del combobox
    def filter_marca(self):
    	self.ui.table_mod.clearSpans()
    	self.ui.busca_mod.clear()
    	#considerar si hay algo en el busca?
    	if (self.ui.combo_Marcas.currentIndex()>0):
    		modelos = model_db.filter_by_marca(self.ui.combo_Marcas.currentText())
    		self.load_tabla(modelos)
    	else:
    		self.load_data()

    def load_desc(self, index):
    	index = self.ui.table_mod.currentIndex()
    	if index.row() == -1:
    		return
    	data = self.ui.table_mod.model()
        descrip = data.index(index.row(), 6, QtCore.QModelIndex()).data()
        detalles = u"<pre><b>Motor:  </b>"+str(data.index(index.row(), 4, QtCore.QModelIndex()).data())+\
        	  u"<br/><b>Peso:  </b>"+str(data.index(index.row(), 5, QtCore.QModelIndex()).data())+" Km"\
        	  u"<br/><b>Rendimiento:  </b>"+str(data.index(index.row(), 7, QtCore.QModelIndex()).data())+" Km/L"\
        	  u"<br/><b>Fecha de Creación:  </b>"+str(data.index(index.row(), 8, QtCore.QModelIndex()).data())+"</pre>"

        #que pasa cuando no hay imagen
        modelo_id = data.index(index.row(), 9, QtCore.QModelIndex()).data()
        marca_id = data.index(index.row(), 3, QtCore.QModelIndex()).data()
        img = QtGui.QPixmap(str(model_db.get_img(modelo_id, marca_id)))
        width = self.ui.widget_3.frameGeometry().width()
        height = self.ui.widget_3.frameGeometry().height()/2
        img = img.scaled(width, height, QtCore.Qt.KeepAspectRatio) 
        self.ui.lbl_imagen.setPixmap(img)
        self.ui.lbl_detalles.setText(detalles)
        self.ui.lbl_descrip.setWordWrap(True)
        self.ui.lbl_descrip.setMaximumWidth(width)
        self.ui.lbl_descrip.setText(descrip)


    #Carga las marcas al combobox
    def load_combo(self):
    	marcas = model_db.get_marcas()
    	self.ui.combo_Marcas.addItem("TODO")
    	for marca in marcas:
    		self.ui.combo_Marcas.addItem(marca['nombre'])

    #Carga los modelos a la tabla
    def load_tabla(self, modelos):
    	self.data = QtGui.QStandardItemModel(len(modelos), 10)
    	self.data.setHorizontalHeaderItem(0,QtGui.QStandardItem(u"Modelo"))
    	self.data.setHorizontalHeaderItem(1,QtGui.QStandardItem(u"Marca"))
    	self.data.setHorizontalHeaderItem(2,QtGui.QStandardItem(u"Precio($)"))

    	for r, row in enumerate(modelos):
            index = self.data.index(r, 0, QtCore.QModelIndex())
            self.data.setData(index, row[2])#modelo
            index = self.data.index(r, 1, QtCore.QModelIndex())
            self.data.setData(index, row[9])#marca
            index = self.data.index(r, 2, QtCore.QModelIndex())
            self.data.setData(index, row[8])#precio_lista
            #setHidden
            index = self.data.index(r, 3, QtCore.QModelIndex())
            self.data.setData(index, row[0])#id modelo
            index = self.data.index(r, 4, QtCore.QModelIndex())
            self.data.setData(index, row[3])#motor
            index = self.data.index(r, 5, QtCore.QModelIndex())
            self.data.setData(index, row[4])#peso
            index = self.data.index(r, 6, QtCore.QModelIndex())
            self.data.setData(index, row[5])#descripcion
            index = self.data.index(r, 7, QtCore.QModelIndex())
            self.data.setData(index, row[6])#rendimiento
            index = self.data.index(r, 8, QtCore.QModelIndex())
            self.data.setData(index, row[7])#fecha_creacion
            index = self.data.index(r, 9, QtCore.QModelIndex())
            self.data.setData(index, row[1])#id_marca

        self.ui.table_mod.setModel(self.data)
        self.ui.table_mod.setColumnHidden(3,True)
        self.ui.table_mod.setColumnHidden(4,True)
        self.ui.table_mod.setColumnHidden(5,True)
        self.ui.table_mod.setColumnHidden(6,True)
        self.ui.table_mod.setColumnHidden(7,True)
        self.ui.table_mod.setColumnHidden(8,True)
        self.ui.table_mod.setColumnHidden(9,True)
        self.ui.table_mod.horizontalHeader().setResizeMode(0, self.ui.table_mod.horizontalHeader().Stretch)
        self.ui.table_mod.horizontalHeader().setResizeMode(1, self.ui.table_mod.horizontalHeader().Stretch)
        self.ui.table_mod.horizontalHeader().setResizeMode(2, self.ui.table_mod.horizontalHeader().Stretch)
