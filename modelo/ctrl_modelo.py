#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
from PySide import QtGui, QtCore
from ui_widget_modelo import Ui_widget_modelo
from modelo.ctrl_form import Widget_form
import modelo.model_modelo as model_db


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

	def load_data(self):
		modelos = model_db.get_all_modelos()
		self.load_tabla(modelos)

	def actions(self):
		self.ui.combo_Marcas.activated.connect(self.filter_marca)
		self.ui.busca_mod.editingFinished.connect(
			self.filter_busca)  # textChanged
		self.ui.table_mod.clicked.connect(self.load_desc)
		self.ui.btn_agrega_mod.clicked.connect(self.agregar)
		self.ui.btn_edita_mod.clicked.connect(self.edita)
		self.ui.btn_borra_mod.clicked.connect(self.borra)

	def agregar(self):
		self.ui.form = Widget_form(self)
		self.ui.form.accepted.connect(self.load_data)
		self.ui.form.exec_()
		self.ui.table_mod.clearSpans()
		self.load_data()

	def edita(self):
		data = self.ui.table_mod.model()
		index = self.ui.table_mod.currentIndex()
		if index.row() == -1:  # No se ha seleccionado una fila
			msgBox = QtGui.QMessageBox()
			msgBox.information(
				None, u"Error", u"Debe seleccionar una fila.", QtGui.QMessageBox.Ok)
			return False
		else:
			id_modelo = data.index(index.row(), 3, QtCore.QModelIndex()).data()
			self.ui.form = Widget_form(self, id_modelo)
			self.ui.form.accepted.connect(self.load_data)
			self.ui.form.exec_()

		self.ui.table_mod.clearSpans()
		self.load_data()

	def borra(self):
		data = self.ui.table_mod.model()
		index = self.ui.table_mod.currentIndex()
		msgBox = QtGui.QMessageBox()
		if index.row() == -1:  # No se ha seleccionado una fila
			msgBox.information(
				None, u"Error", u"Debe seleccionar una fila.", QtGui.QMessageBox.Ok)
			return False
		else:
			id_modelo = data.index(index.row(), 3, QtCore.QModelIndex()).data()
			id_marca =  data.index(index.row(), 9, QtCore.QModelIndex()).data()
			result = model_db.vendidos(id_modelo,id_marca)
			if result > 0:
				msgBox.information(
				None, u"Información", u"No se pudo elimiar el modelo\n"\
				+u"porque existen elementos en la\n"\
				+u"sección de ventas que depende de\n"\
				+u"el, si desea eliminar este modelo\n"\
				+u"debe eliminar esos elementos primero.", QtGui.QMessageBox.Ok)
			else:
				resp = msgBox.question(
				None, u"Eliminar?", u"Esta seguro de eliminar este modelo?", QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Ok)
			if(resp == 1024):
				model_db.borra_modelo(id_modelo, id_marca)
				img = 'modelo/imagenes/%d_%d.jpg'%(id_marca, id_modelo)
				os.remove(img)
				msgBox.information(
				None, u"Informacion", u"El modelo fue eliminado exitosamente.", QtGui.QMessageBox.Ok)
		self.ui.table_mod.clearSpans()
		self.load_data()

	# filtra segun el buscador de texto
	def filter_busca(self):
		self.ui.table_mod.clearSpans()
		if(len(self.ui.busca_mod.text()) > 0):  # falta trimear
			modelos = model_db.filter_by_busca(self.ui.busca_mod.text())
			self.load_tabla(modelos)
		else:
			self.load_data()

	# filtra segun las marcas del combobox
	def filter_marca(self):
		self.ui.table_mod.clearSpans()
		self.ui.busca_mod.clear()
		# considerar si hay algo en el busca?
		if (self.ui.combo_Marcas.currentIndex() > 0):
			modelos = model_db.filter_by_marca(
				self.ui.combo_Marcas.currentText())
			self.load_tabla(modelos)
		else:
			self.load_data()

	def load_desc(self, index):
		index = self.ui.table_mod.currentIndex()
		if index.row() == -1:
			return
		data = self.ui.table_mod.model()
		descrip = data.index(index.row(), 6, QtCore.QModelIndex()).data()
		detalles = u"<pre><b>Motor:  </b>" + str(data.index(index.row(), 4, QtCore.QModelIndex()).data()) +\
			u"<br/><b>Peso:  </b>" + str(data.index(index.row(), 5, QtCore.QModelIndex()).data()) + " Km"\
			u"<br/><b>Rendimiento:  </b>" + str(data.index(index.row(), 7, QtCore.QModelIndex()).data()) + " Km/L"\
			u"<br/><b>Fecha de Creación:  </b>" + \
			str(data.index(index.row(), 8, QtCore.QModelIndex()).data()) + "</pre>"

		self.ui.lbl_detalles.setText(detalles)
		modelo_id = data.index(index.row(), 3, QtCore.QModelIndex()).data()
		marca_id = data.index(index.row(), 9, QtCore.QModelIndex()).data()
		img = QtGui.QPixmap(str(model_db.get_img(modelo_id, marca_id)))
		width = self.ui.widget_3.frameGeometry().width()
		height = self.ui.widget_3.frameGeometry().height() / 2
		img = img.scaled(width, height, QtCore.Qt.KeepAspectRatio)
		self.ui.lbl_imagen.setPixmap(img)
		self.ui.lbl_descrip.setWordWrap(True)
		self.ui.lbl_descrip.setMaximumWidth(width)
		self.ui.lbl_descrip.setText(descrip)

	# Carga las marcas al combobox
	def load_combo(self):
		marcas = model_db.get_marcas()
		self.ui.combo_Marcas.addItem("TODO")
		for marca in marcas:
			self.ui.combo_Marcas.addItem(marca['nombre'])

	# Carga los modelos a la tabla
	def load_tabla(self, modelos):
		self.data = QtGui.QStandardItemModel(len(modelos), 10)
		self.data.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Modelo"))
		self.data.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Marca"))
		self.data.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Precio($)"))

		for r, row in enumerate(modelos):
			index = self.data.index(r, 0, QtCore.QModelIndex())
			self.data.setData(index, row[2])  # modelo
			index = self.data.index(r, 1, QtCore.QModelIndex())
			self.data.setData(index, row[9])  # marca
			index = self.data.index(r, 2, QtCore.QModelIndex())
			self.data.setData(index, row[8])  # precio_lista
			# setHidden
			index = self.data.index(r, 3, QtCore.QModelIndex())
			self.data.setData(index, row[0])  # id modelo
			index = self.data.index(r, 4, QtCore.QModelIndex())
			self.data.setData(index, row[3])  # motor
			index = self.data.index(r, 5, QtCore.QModelIndex())
			self.data.setData(index, row[4])  # peso
			index = self.data.index(r, 6, QtCore.QModelIndex())
			self.data.setData(index, row[5])  # descripcion
			index = self.data.index(r, 7, QtCore.QModelIndex())
			self.data.setData(index, row[6])  # rendimiento
			index = self.data.index(r, 8, QtCore.QModelIndex())
			self.data.setData(index, row[7])  # fecha_creacion
			index = self.data.index(r, 9, QtCore.QModelIndex())
			self.data.setData(index, row[1])  # id_marca

		self.ui.table_mod.setModel(self.data)
		self.ui.table_mod.setColumnHidden(3, True)
		self.ui.table_mod.setColumnHidden(4, True)
		self.ui.table_mod.setColumnHidden(5, True)
		self.ui.table_mod.setColumnHidden(6, True)
		self.ui.table_mod.setColumnHidden(7, True)
		self.ui.table_mod.setColumnHidden(8, True)
		self.ui.table_mod.setColumnHidden(9, True)
		self.ui.table_mod.horizontalHeader().setResizeMode(
			0, self.ui.table_mod.horizontalHeader().Stretch)
		self.ui.table_mod.horizontalHeader().setResizeMode(
			1, self.ui.table_mod.horizontalHeader().Stretch)
		self.ui.table_mod.horizontalHeader().setResizeMode(
			2, self.ui.table_mod.horizontalHeader().Stretch)
