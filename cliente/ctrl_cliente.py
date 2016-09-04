#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from ctrl_form_cli import FormCliente
from ui_widget_cliente import Ui_widget_cliente
import model_cli as db_model


class Widget_cliente(QtGui.QWidget):
	def __init__(self, parent=None):
		super(Widget_cliente, self).__init__(parent)
		self.ui = Ui_widget_cliente()
		self.ui.setupUi(self)
		self.load_data()
		self.actions()

	def actions(self):
		self.ui.btn_agregar_cli.clicked.connect(self.agregar_cli)
		self.ui.btn_borrar_cli.clicked.connect(self.borrar_cli)
		self.ui.btn_editar_cli.clicked.connect(self.editar_cli)

	def agregar_cli(self):
		self.ui.form = FormCliente(self)
		self.ui.form.accepted.connect(self.load_data)
		self.ui.form.exec_()

	def load_data(self):		
		clientes = db_model.obtener_clientes()

		self.data = QtGui.QStandardItemModel(len(clientes), 6)
		self.data.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"RUT"))
		self.data.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombres"))
		self.data.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Apellidos"))
		self.data.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Telefono"))
		self.data.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Correo"))
		self.data.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Compras"))
		
		for r, row in enumerate(clientes):
			index = self.data.index(r, 0, QtCore.QModelIndex())
			self.data.setData(index, row['rut'])
			index = self.data.index(r, 1, QtCore.QModelIndex())
			self.data.setData(index, row['nombres'])
			index = self.data.index(r, 2, QtCore.QModelIndex())
			self.data.setData(index, row['apellidos'])
			index = self.data.index(r, 3, QtCore.QModelIndex())
			self.data.setData(index, row['telefono'])
			index = self.data.index(r, 4, QtCore.QModelIndex())
			self.data.setData(index, row['correo'])
			index = self.data.index(r, 5, QtCore.QModelIndex())
			self.data.setData(index, row['cantidad'])

		self.ui.table_cli.setModel(self.data)
			
		self.ui.table_cli.horizontalHeader().setResizeMode(0, self.ui.table_cli.horizontalHeader().Stretch)
		self.ui.table_cli.horizontalHeader().setResizeMode(1, self.ui.table_cli.horizontalHeader().Stretch)
		self.ui.table_cli.horizontalHeader().setResizeMode(2, self.ui.table_cli.horizontalHeader().Stretch)
		self.ui.table_cli.horizontalHeader().setResizeMode(3, self.ui.table_cli.horizontalHeader().Stretch)
		self.ui.table_cli.horizontalHeader().setResizeMode(4, self.ui.table_cli.horizontalHeader().Stretch)
		self.ui.table_cli.horizontalHeader().setResizeMode(5, self.ui.table_cli.horizontalHeader().Stretch)

	def borrar_cli(self):
		data = self.ui.table_cli.model()
		index = self.ui.table_cli.currentIndex()
		if index.row() == -1:  # No se ha seleccionado una fila
			self.errorMessageDialog = QtGui.QErrorMessage(self)
			self.errorMessageDialog.showMessage(u"Debe seleccionar una fila")
			return False
		else:
			msgBox = QtGui.QMessageBox()
			result= msgBox.question(None, u"Eliminar", u"¿Está seguro de eliminar este registro?", QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel)
			if (result == 1024):#botón ok
				rut = data.index(index.row(), 0, QtCore.QModelIndex()).data()
				cant = db_model.consul_compra(rut)
				if (cant == None):
					if (db_model.borrar(rut)):
						self.load_data()
						msgBox = QtGui.QMessageBox()
						msgBox.setText(u"El registro fue eliminado.")
						msgBox.exec_()
						return True
					else:
						self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
						self.ui.errorMessageDialog.showMessage(u"Error al eliminar el registro.")
						return False
				else:
					db_model.cambia_estado(rut)
					self.load_data()
					msgBox = QtGui.QMessageBox()
					msgBox.setText(u"El registro fue eliminado.")
					msgBox.exec_()
			else:
				msgBox = QtGui.QMessageBox()
				msgBox.setText(u"Se ha cancelado la operación.")
				msgBox.exec_()

	def editar_cli(self):
		data = self.ui.table_cli.model()
		index = self.ui.table_cli.currentIndex()
		if index.row() == -1:  # No se ha seleccionado una fila
			self.errorMessageDialog = QtGui.QErrorMessage(self)
			self.errorMessageDialog.showMessage(u"Debe seleccionar una fila")
			return False
		else:
			rut = data.index(index.row(), 0, QtCore.QModelIndex()).data()
			self.ui.form = FormCliente(self, rut)
			self.ui.form.accepted.connect(self.load_data)
			self.ui.form.exec_()