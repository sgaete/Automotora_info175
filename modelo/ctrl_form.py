#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import shutil
from PySide import QtGui, QtCore
from ui_widget_form import Ui_Form
import modelo.model_modelo as model_db


class Widget_form(QtGui.QDialog):

	def __init__(self, parent=None, id_modelo=None):

		super(Widget_form, self).__init__(parent)
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		# se trae marcas de la base de datos y se hace un arreglo
		marcas_lista = []
		marcas = model_db.get_marcas()
		for marca in marcas:
			self.ui.n_marca.addItem(marca['nombre'])
			marcas_lista.append(marca['nombre'])

		# agregar o editar respectivamente
		if id_modelo is None:
			self.ui.acepta_mod.clicked.connect(self.crea_mod)
		else:

			self.colocar_datos(id_modelo, marcas_lista)
			self.ui.acepta_mod.clicked.connect(
				lambda: self.edita_mod(id_modelo))
		self.ui.open_qfile.clicked.connect(self.open_img)
		self.ui.cancel.clicked.connect(self.close)

	def open_img(self):
		fileName = QtGui.QFileDialog.getOpenFileName(
			self, "Abrir imagen", "/home/", "Image Files (*.png *.jpg *.bmp)")[0]
		self.ui.n_img.setText(fileName)

	# action para crear un modelo
	def crea_mod(self):

		modelo = self.captura_datos()
		modelo[1] = self.valida_espacios(modelo[1])
		valido = self.valida_campos(modelo)
		if (valido == True):
			modelo[0] = model_db.get_id_marca(modelo[0])
			model_db.insert_modelo(modelo)
			id_modelo = model_db.id_modelo(modelo[1])
			img = 'modelo/imagenes/%d_%d.jpg'%(modelo[0], id_modelo)
			model_db.inserta_imagen(modelo[0], id_modelo, img)
			shutil.copyfile(modelo[8], img)
			self.close()


	# action para editar un modelo
	def edita_mod(self, id_modelo):
		modelo = self.captura_datos()
		modelo[1] = self.valida_espacios(modelo[1])
		valido = self.valida_campos(modelo, id_modelo)
		if (valido == True):
			#id marca nueva
			modelo[0] = model_db.get_id_marca(modelo[0])
			#id marca antigua
			id_marca = model_db.get_idmarca(id_modelo)
			model_db.borra_modelo(id_modelo, id_marca)
			img = 'modelo/imagenes/%d_%d.jpg'%(id_marca, id_modelo)
			os.remove(img)
			model_db.insert_modelo(modelo)
			id_modelo = model_db.id_modelo(modelo[1])
			img = 'modelo/imagenes/%d_%d.jpg' %(modelo[0], id_modelo)
			model_db.inserta_imagen(modelo[0], id_modelo, img)
			shutil.copyfile(modelo[8], img)
			self.close()
		
	# pide datos a la db y los situa en los campos del formulario
	def colocar_datos(self, id_modelo, marcas_lista):

		modelo = model_db.get_modelo(id_modelo)
		self.ui.n_modelo.setText(modelo['modelo'])
		i = marcas_lista.index(modelo['nombre'])
		self.ui.n_marca.setCurrentIndex(i)
		self.ui.n_motor.setText(modelo['motor'])
		self.ui.n_peso.setValue(modelo['peso'])
		self.ui.n_rend.setValue(modelo['rendimiento'])
		datestr = modelo['fecha_creacion'].split("-")
		datestr = map(int, datestr)
		date = QtCore.QDate(datestr[0], datestr[1], datestr[2])
		self.ui.n_fecha.setDate(date)
		self.ui.n_precio.setValue(modelo['precio_lista'])
		self.ui.n_img.setText(modelo['archivo'])
		self.ui.n_descrip.setText(modelo['descripcion'])


	# captura los datos de los campos del formulario
	def captura_datos(self):

		modelo = [
			self.ui.n_marca.currentText(),
			self.ui.n_modelo.text(),
			self.ui.n_motor.text(),
			self.ui.n_peso.value(),
			self.ui.n_descrip.toPlainText(),
			self.ui.n_rend.value(),
			self.ui.n_fecha.date(),
			self.ui.n_precio.value(),
			self.ui.n_img.text()]

		return modelo

	def valida_espacios(self, palabra):
		palabra = palabra.split(" ")
		palabra = filter(lambda x: x != '', palabra)
		palabra = " ".join(palabra)
		palabra = palabra.upper()

		return palabra

	def valida_campos(self, modelo, id_modelo  = None):
		if(len(modelo[1]) == 0):
			self.ui.n_modelo.setText("")
			msgBox = QtGui.QMessageBox()
			msgBox.critical(
				None, u"Error", u"Modelo invalido.", QtGui.QMessageBox.Ok)
		else:
			# falta considerar modelo ya existente
			if id_modelo == None:
				count = model_db.valida(modelo[1], modelo[0])
			else:
				count = model_db.valida(modelo[1], modelo[0], id_modelo)
			if count != None:
				msgBox = QtGui.QMessageBox()
				msgBox.critical(
					None, u"Error", u"El modelo ingresado ya existe.", QtGui.QMessageBox.Ok)
			else:
				modelo[2] = self.valida_espacios(modelo[2])
				if(len(modelo[2]) == 0):
					self.ui.n_motor.setText("")
					msgBox = QtGui.QMessageBox()
					msgBox.critical(
						None, u"Error", u"Motor invalido.", QtGui.QMessageBox.Ok)
				else:
					if(len(modelo[8]) == 0):
						msgBox = QtGui.QMessageBox()
						msgBox.critical(
							None, u"Error", u"Imagen invalida.", QtGui.QMessageBox.Ok)
					else:
						return True
						