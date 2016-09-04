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

		QtCore.QObject.connect(self.ui.marca, QtCore.SIGNAL("currentIndexChanged(QString)"), self.llenar_combobox2)
		QtCore.QObject.connect(self.ui.modelo, QtCore.SIGNAL("currentIndexChanged(QString)"), self.llenar_combobox3)
		QtCore.QObject.connect(self.ui.precio_lista, QtCore.SIGNAL("currentIndexChanged(QString)"), self.llenar_total_venta)
		
		self.ui.btn_aceptar.clicked.connect(self.crear_venta)

	def crear_venta(self):
		rut, marca, modelo, patente, color, precio_venta = self.obtener_datos()
		
		model_vent.crear_venta(rut, marca, modelo, patente, color, precio_venta)
		self.accepted.emit()
		msgBox = QtGui.QMessageBox()
		msgBox.setText(u"Venta realizada.")
		msgBox.exec_()
		self.close()
	"""def obtener_datos(self):
		rut = self.ui.rut.text()
		marca = self.ui.marca.text()
		modelo = self.ui.modelo.text()
		patente = self.ui.patente.text()
		color = self.ui.color.text()
		

		precio_venta = self.ui.precio_vent.text()

		return (rut, marca, modelo, patente, color, precio_venta)"""

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
		descuento = self.ui.descuento.value()
		print "jajajajajaja"
		print precio_lista
		print descuento
		print "jijijijijij"
		tota_venta = int(precio_lista)-((int(precio_lista) *int(descuento))/100)
		print tota_venta
		color = self.ui.precio_vent.setText(str(tota_venta))

		
