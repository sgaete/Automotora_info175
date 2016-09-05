#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui
from ui_widget_form_cli import Ui_form_cliente
import model_cli


class FormCliente(QtGui.QDialog):
	def __init__(self, parent=None, rut=None):
		super(FormCliente, self).__init__(parent)
		self.ui = Ui_form_cliente()
		self.ui.setupUi(self)
		if rut is None:
			self.ui.btn_aceptar.clicked.connect(self.crear_cliente)
		else:
			self.colocar_datos(rut)
			self.ui.btn_aceptar.clicked.connect(lambda: self.editar_cliente(rut))
		self.ui.btn_cancelar.clicked.connect(self.close)

	def colocar_datos(self, rut):
		cliente = model_cli.cliente(rut)
		self.ui.rut.setText(str(cliente["rut"]))
		self.ui.nombres.setText(cliente["nombres"])
		self.ui.apellidos.setText(cliente["apellidos"])
		self.ui.telefono.setText(cliente["telefono"])
		self.ui.correo.setText(cliente["correo"])
	
	def obtener_datos(self):
		rut = self.ui.rut.text()
		nombres = self.ui.nombres.text()
		apellidos = self.ui.apellidos.text()
		telefono = self.ui.telefono.text()
		correo = self.ui.correo.text()
		return (rut, nombres, apellidos, telefono, correo)

	def valida_datos(self, rut, nombres, apellidos, telefono):
		try:
			rut = int(rut)
			telefono = int(telefono)
			if (len(str(rut)) < 7 or len(str(telefono)) < 9):
				msgBox = QtGui.QMessageBox()
				msgBox.critical(None, u"Error", u"Dato inválido.", QtGui.QMessageBox.Ok)
				return False
			elif (len(nombres.strip()) == 0 or len(apellidos.strip()) == 0 or len(str(telefono).strip()) == 0):
				msgBox = QtGui.QMessageBox()
				msgBox.critical(None, u"Error", u"Campo vacío.", QtGui.QMessageBox.Ok)
				return False
			else:
				return True
		except ValueError:
			msgBox = QtGui.QMessageBox()
			msgBox.critical(None, u"Error", u"Dato inválido.", QtGui.QMessageBox.Ok)
			return False

	def crear_cliente(self):
		rut, nombres, apellidos, telefono, correo = self.obtener_datos()
		val = self.valida_datos(rut, nombres, apellidos, telefono)
		if (val):
			dato = model_cli.valida(rut)
			if dato != None:
				msgBox = QtGui.QMessageBox()
				msgBox.critical(None, u"Error", u"El cliente ingresado ya existe.", QtGui.QMessageBox.Ok)
			else:
				model_cli.crear_cliente(rut, nombres, apellidos, telefono, correo)
				self.accepted.emit()
				msgBox = QtGui.QMessageBox()
				msgBox.setText(u"El cliente ha sido creado.")
				msgBox.exec_()
				self.close()

	def editar_cliente(self, old_rut):
		rut, nombres, apellidos, telefono, correo = self.obtener_datos()
		val = self.valida_datos(rut, nombres, apellidos, telefono)
		if (val):
			dato = model_cli.valida(rut, old_rut)
			if dato != None:
				msgBox = QtGui.QMessageBox()
				msgBox.critical(None, u"Error", u"El cliente ingresado ya existe.", QtGui.QMessageBox.Ok)
			else:
				model_cli.editar(old_rut, rut, nombres, apellidos, telefono, correo)
				self.accepted.emit()
				self.close()