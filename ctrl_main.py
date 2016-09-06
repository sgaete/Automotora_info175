#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui
from ui_main import Ui_Main
from modelo.ctrl_modelo import Widget_modelo
from marca.ctrl_marca import Widget_marca
from cliente.ctrl_cliente import Widget_cliente
from venta.ctrl_vent import Widget_vent

class Main(QtGui.QMainWindow):
	"""
	Módulo principal del sistema
	"""
	def __init__(self):
		super(Main, self).__init__()
		self.ui = Ui_Main()   
		self.ui.setupUi(self)
		# Cargamos las acciones al presionar el menú
		self.menu_actions()
		self.show()

	def menu_actions(self):
		self.ui.label_2.setPixmap(QtGui.QPixmap("banner/3.png")) 
		self.ui.actionModelos.triggered.connect(self.load_modelo)
		self.ui.actionMarcas.triggered.connect(self.load_marca)
		self.ui.actionClientes.triggered.connect(self.load_cliente)
		self.ui.actionVentas.triggered.connect(self.load_venta)
		self.ui.actionAcerca_de.triggered.connect(self.acercade)
		self.ui.actionCerrar_Sesi_n.triggered.connect(self.logout)
		self.ui.actionSalir.triggered.connect(exit)

	def load_modelo(self):
		main.setWindowTitle("Modulo Modelo")
		widget = Widget_modelo(self)
		self.setCentralWidget(widget)

	def load_marca(self):
		main.setWindowTitle("Modulo Marca")
		widget = Widget_marca(self)
		self.setCentralWidget(widget)

	def load_cliente(self):
		main.setWindowTitle("Modulo Cliente")
		widget = Widget_cliente(self)
		self.setCentralWidget(widget)

	def load_venta(self):
		main.setWindowTitle("Modulo Venta")
		widget = Widget_venta(self)
		self.setCentralWidget(widget)

	def logout(self):
		print "Cerrando sesion..."

	def acercade(self):
		main.setWindowTitle("Acerca de")
		print "Acerca de ... "
		msg = QtGui.QMessageBox()
		msg.setWindowTitle("Acerca de")
		msg.setText("Integrantes: \n- Camilo Alexander Alarcon Romero\n- Sebastian Andres Gaete Velasquez\n- Lucia Berenice Marquez Esprel\n- Cristian Alonso Ordonez Figueroa\n\n"
			"Profesor: \n- Cristian Rojas Perez\n\n"
			"Asignatura: \n- Info175 - Taller de Construccion de Software\n\n"
			"Ingenieria Civil en Informatica, Universidad Austral de Chile, Valdivia, 2016\n\n")
		msg.exec_()
		msg.show()

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	main = Main()
	sys.exit(app.exec_())
