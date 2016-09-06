#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: 850 -*-
import os
import sys
from PySide import QtGui, QtCore

from ui_widget_marca import Ui_widget_marca
from marca.ctrl_form import Widget_form
import marca.model_marca as model_db

class Widget_marca(QtGui.QWidget):
	"""
	Marca
	"""
	table_columns = (
		(u"Marca", 50),
		(u"Pais", 410),
		(u"Cantidad de Modelos", 200))
	def __init__(self, parent=None):
		super(Widget_marca, self).__init__(parent)
		self.ui = Ui_widget_marca()
		self.ui.setupUi(self)
		self.load_data()
		self.signals()
		self.show()

	def signals(self):
		self.ui.table_marc.clicked.connect(self.show_logo)
		self.ui.table_marc.clicked.connect(self.cantModelos)
		self.ui.btn_agrega_marc.clicked.connect(self.add)
		self.ui.btn_borra_marc.clicked.connect(self.borrar)
		self.ui.btn_edita_marc.clicked.connect(self.edit)
	
	def add(self):
		print "Creacion de nueva marca en progreso..."
		self.ui.form = Widget_form(self)
		self.ui.form.setWindowTitle("Agregar Marca")
		self.ui.form.accepted.connect(self.load_data)
		self.ui.form.exec_()

	def edit(self):
		print "Actualizacion de marca en progreso..."
		data = self.ui.table_marc.model()
		index = self.ui.table_marc.currentIndex()
		if (index.row() == -1): #No se ha seleccionado una fila
			QtGui.QMessageBox.information(self, "Aviso","Debe seleccionar una fila para editar.")

			return False
		else:
			marc_id = data.index(index.row(), 0, QtCore.QModelIndex()).data()
			self.ui.form = Widget_form(self, marc_id)
			self.ui.form.setWindowTitle("Editar Marca")
			#self.ui.form.setWindowTitle("Editar Marca "+str(self.marca_id["nombre"]))
			self.ui.form.accepted.connect(self.load_data)
			self.ui.form.exec_()
			#self.ui.form.show()
			img = QtGui.QPixmap('/logos/null.png')
			self.ui.label_5.setPixmap(img)   

	def show_logo(self, index):
		index = index if index is not None\
			else self.ui.table_marc.currentIndex()
		#print index
		data = self.ui.table_marc.model()
		marca = data.item(index.row(),0).marca
		img = QtGui.QPixmap(str(marca['imagen']))
		width = self.ui.widget_4.frameGeometry().width()
		height = self.ui.widget_4.frameGeometry().height()
		img = img.scaled(width, height, QtCore.Qt.KeepAspectRatio)
		self.ui.label_5.setPixmap(img)      
		#imagenes redimencionadas a 400x500
		print "La cantidad de modelos para la marca "+ (str(marca['nombre']))+" es: "+(str(marca['cantidad']))
	

	def cantModelos(self):  ##verifica si es optimo borrar una marca o no
		model = self.ui.table_marc.model()
		index = self.ui.table_marc.currentIndex()
		data = self.ui.table_marc.model()
		marca = data.item(index.row(),0).marca  
		cant = str(marca['cantidad'])
		return cant


	def load_data(self):
		marcas = model_db.get_marcas()
		rows = len(marcas)
		data = QtGui.QStandardItemModel(rows, len(self.table_columns))
		self.ui.table_marc.setModel(data)
		self.ui.table_marc.horizontalHeader().setResizeMode(
			
			0, self.ui.table_marc.horizontalHeader().Stretch)

		for col, h in enumerate(self.table_columns):
			data.setHeaderData(col, QtCore.Qt.Horizontal, h[0])
			self.ui.table_marc.setColumnWidth(col, h[1])

		for i, marca in enumerate(marcas):
			#row = [marca["nombre"], marca["pais"]]
			row = [marca["nombre"], marca["pais"], marca["cantidad"]]
			for j, field in enumerate(row):
				index = data.index(i, j, QtCore.QModelIndex())
				data.setData(index, field)
			data.item(i).marca = marca
	

	def borrar(self):
		model = self.ui.table_marc.model()
		index = self.ui.table_marc.currentIndex()

		if (index.row() == -1): #No se ha seleccionado una fila
			QtGui.QMessageBox.information(self, "Aviso", "No ha seleccionado ninguna fila!")
			return False

		else:
			marc_id = model.index(index.row(), 0, QtCore.QModelIndex()).data()
			rutaimg = model_db.buscarI(str(marc_id)) 
			rutaa = str(rutaimg[0])   #obtenemos la ruta del logo de la marca seleccionada
			cm = self.cantModelos()   #cantidad de modelos por marca
			cm1 = cm.strip()		 
			cm2 = int(cm1)

			if(cm2!=0):
				QtGui.QMessageBox.information(self, "Aviso", "Error al eliminar el registro ya que se encuentran modelos registrados para esa marca.")
				return false
			else:
				if (cm2==0):						#si no hay modelos para esa marca lo eliminamos
					
					flags = QtGui.QMessageBox.StandardButton.Yes 
					flags |= QtGui.QMessageBox.StandardButton.No
					question = "Esta a un paso de borrar esta marca de la base de datos. Desea continuar de todas formas? (OBS: Esta marca no contiene modelos asociados) "
					response = QtGui.QMessageBox.question(self, "Consulta",question,flags)

					if response == QtGui.QMessageBox.Yes:     #si quiere continuar con la eliminacion

						if(model_db.delete(marc_id)):   #eliminamos la marca de la base de datos
							self.load_data()			#cargamos nuevamente los datos en la grilla
							img = QtGui.QPixmap('/logos/null.png')   #limpiamos el label que muestra la imagen
							self.ui.label_5.setPixmap(img) 			 #definimos una nueva imagen nula al label  
							os.remove(rutaa)						#eliminamos la imagen de la carpeta de logos
							msgBox = QtGui.QMessageBox()		
							msgBox.setWindowTitle("Estado de la marca")
							msgBox.setText("EL registro de "+marca_eliminada+" fue eliminado satisfactoriamente.")
							print "EL registro de "+marca_eliminada+" fue eliminado."
							msgBox.exec_()
							return True
					elif QtGui.QMessageBox.No:
						print "Cuando este completamente seguro puede intentarlo nuevamente!"

	
if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	main = Widget_marca()
	sys.exit(app.exec_())
