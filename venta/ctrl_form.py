# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from ui_widget_form import Ui_Form_vent
import model_vent
import venta.model_vent as model_db

class FormVenta(QtGui.QDialog):
	def __init__(self, parent=None):

		super(FormVenta, self).__init__(parent)
		self.ui = Ui_Form_vent()
		self.ui.setupUi(self)
		self.llenar_combobox_rut()
		self.llenar_combobox1()
		self.llenar_combobox2()
		self.llenar_combobox3()
		self.llenar_total_venta()
		self.ui.precio_vent.setText(self.ui.precio_lista.text())


		QtCore.QObject.connect(self.ui.marca, QtCore.SIGNAL("currentIndexChanged(QString)"), self.llenar_combobox2)
		QtCore.QObject.connect(self.ui.modelo, QtCore.SIGNAL("currentIndexChanged(QString)"), self.llenar_combobox3)
		
		self.ui.btn_aceptar.clicked.connect(self.crear_venta)
		self.ui.btn_cancel.clicked.connect(self.close)

	def crear_venta(self):
		rut, marca, modelo, patente, color, precio_venta = self.capturar_datos()
		
		model_vent.crear_venta(rut, marca, modelo, patente, color, precio_venta)
		self.accepted.emit()
		msgBox = QtGui.QMessageBox()
		msgBox.setText(u"Venta realizada.")
		msgBox.exec_()
		self.close()
	def capturar_datos(self):
		rut = self.ui.rut.currentText()
		marca = self.ui.marca.currentText()
		modelo = self.ui.modelo.currentText()
		patente = self.ui.patente.text() 
		color = self.ui.color.text()
		precio_venta = self.ui.precio_vent.text()
		print patente
		print "holaaaaa"
		patente = patente.split(" ")
		patente = filter(lambda x: x !='',patente)
		patente = ''.join(patente)
		print "chaoooo"
		print patente

		
		if (len(patente) < 6) or (color =="") or (color.isspace()):
			if (len(patente) < 6):
				msgBox = QtGui.QMessageBox()
				msgBox.setText(u"Patente Incorrecta.")
				msgBox.exec_()
			if color =="" or (color.isspace()):
				msgBox = QtGui.QMessageBox()
				msgBox.setText(u"Faltan Datos.")
				msgBox.exec_()
		else:
			return (rut, marca, modelo, patente, color, precio_venta)

	def llenar_combobox_rut(self):
		clientes = model_db.obtenercliente()
		for cliente in clientes:
			x =str(cliente['rut'])
			self.ui.rut.addItem(x)	

	def llenar_combobox1(self):
		marcas = model_db.obtenermarcas()
		for marca in marcas:
			self.ui.marca.addItem(marca['nombre'])	
		

	def llenar_combobox2(self):
		self.ui.modelo.clear()
		marca = self.ui.marca.currentText()
		modelos = model_db.obtenermodelos(marca)
		for modelo in modelos:
			self.ui.modelo.addItem(modelo['modelo'])

	def llenar_combobox3(self):
		self.ui.precio_lista.clear()
		modelo = self.ui.modelo.currentText()
		precio = model_db.obtener_precio(modelo)['precio_lista']
		self.ui.precio_lista.setText(str(precio))
		self.llenar_total_venta()

	def llenar_total_venta(self):
		precio_lista = self.ui.precio_lista.text()
		self.ui.descuento.valueChanged.connect(lambda: self.desc(self.ui.descuento.value(), int(precio_lista)))

	def desc(self,a,b):
		descuento = b-(b*a/100)
		self.ui.precio_vent.setText(str(descuento))
		