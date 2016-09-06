#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: 850 -*-

import sys
from PySide import QtGui, QtCore
from ui_widget_form import Ui_Form
import marca.model_marca as model_db
import shutil, os

class Widget_form(QtGui.QDialog):
	"""
	Formulario de marca
	"""
	def __init__(self, parent=None, marc_id=None):
		super(Widget_form, self).__init__(parent)
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.signals()
		#buscar_img_bloqueado=True
		if marc_id is None:
			self.ui.savemarca.clicked.connect(self.crear_marca)
			self.ui.buscar_img.clicked.connect(self.abririmg)
		else:
			self.colocar_datos(marc_id)
			self.ui.savemarca.clicked.connect(
				lambda: self.editar_marca(marc_id))  
			self.ui.buscar_img.clicked.connect(self.abririmg)

		self.ui.cancel.clicked.connect(self.close)

	def signals(self):
		pass

	def colocar_datos(self, marc_id):
		print " --- Colocando datos... ---"
		marca = model_db.marca(marc_id)
		print "Datos puestos en la ventana de editar: "
		i=str(marca[0]).strip()
		n=str(marca[1]).strip()
		p=str(marca[2]).strip()
		print "- Marca: "+str(marca[0])
		print "- Pais: "+str(marca[1])
		print "- Ruta logo: "+str(marca[2])
		self.ui.t_marca.setText(i)
		self.ui.t_pais.setText(n)
		self.ui.t_img.setText(p)
	
	#si se presiona aceptar se ejecuta...
	def crear_marca(self):
		imagen, nombre, pais = self.obtener_dato()
		ii=imagen.strip()
		nn=nombre.strip()
		pp=pais.strip()

		b=False
		uno=""
		dos=""
		print nn
		m = model_db.marca(nn)

		if(m is None):
			print "es nulo"
			b=True
		else:
			print m[0]
			uno = str(m[0]).strip()
			uno = uno.lower()
			print uno
			dos = nn.lower()
			print dos

			print "uno="+uno+" dos="+dos

		if(uno!=dos or b):
			if(ii=="" or nn=="" or pp==""):
				if(nn==""):
					QtGui.QMessageBox.information(self, "Campo incompleto", "No ha ingresado ningun nombre para la marca")
				if(pp==""):
					QtGui.QMessageBox.information(self, "Campo incompleto", "No ha ingresado ningun pais")
				if(ii==""):
					QtGui.QMessageBox.information(self, "Campo incompleto", "No ha ingresado ningun logo para su marca")
			else:
				i = imagen
				n = nombre.upper()
				p = pais.title()

				ruta = os.getcwd() + os.sep
				origen = imagen
				destino = "marca/logos/"+nombre+".png"
				#print origen
				#print destino
				try:
				    shutil.copyfile(origen, destino)
				    print("Logotipo copiado satisfactoriamente")
				except:
				    print("Se ha producido un error en el copiado del logo")
			
				model_db.crear_marca(destino,n,p)
				self.accepted.emit()
				print "Creacion de nueva marca finalizada!"
				print " - Nueva marca: "+n
				print " - Del pais: "+p
				print " - Ruta del logo: "+destino
				self.close()
		else:
			if(uno==dos):
				QtGui.QMessageBox.information(self, "Aviso","La marca que esta ingresando ya se encuentra en la base de datos de la automotora.")
				self.close()

	def editar_marca(self,marc_id):
		imagen,nombre,pais = self.obtener_dato()
		ii=imagen.strip()
		nn=nombre.strip()
		pp=pais.strip()
		if(ii=="" or nn=="" or pp==""):
			if(nn==""):
				QtGui.QMessageBox.information(self, "Campo incompleto", "No ha ingresado ningun nombre para la marca")
			if(pp==""):
				QtGui.QMessageBox.information(self, "Campo incompleto", "No ha ingresado ningun pais")
			if(ii==""):
				QtGui.QMessageBox.information(self, "Campo incompleto", "No ha ingresado ningun logo para su marca")
		else:
			i = imagen
			n = nombre.upper()
			p = pais.title()

		print "Datos obtenidos:"
		print "- Marca: "+nombre
		print "- Pais: "+pais
		print "- Direccion de la img: "+imagen    #################tratar la imagen y copiarla

		ruta = os.getcwd() + os.sep
		origen = imagen
		destino = "marca/logos/"+nombre+".png"
		#print origen
		#print destino
		try:
		    shutil.copyfile(origen, destino)
		    print("Logotipo copiado satisfactoriamente")
		except:
		    print("Se ha producido un error en el copiado del logo")
		os.remove(ii)
		model_db.edit_marca(imagen,nombre,pais,marc_id)
		self.accepted.emit()
		print "Edicion de la marca ha finalizado!"
		print " - Marca: "+n
		print " - Pais: "+p
		print " - Ruta del logo: "+destino
		self.close()

	def abririmg(self):
		n=self.obtenerNombre()
		if(n!=""):
			ruta_logo = QtGui.QFileDialog.getOpenFileName(self, "Abrir imagen","/home/","Image Files (*.png *.jpg *.bmp)")
			print ruta_logo[0]
			self.ui.t_img.setText(str(ruta_logo[0]))
		else:
			QtGui.QMessageBox.information(self, "Aviso", "Antes de seleccionar un logo debe ingresar el nombre de la marca a registrar")

	def obtenerNombre(self):       #para validar el metodo abririmg()
		nombre = self.ui.t_marca.text()
		return nombre

	def obtener_dato(self):
		print " --- Obteniendo datos... ---"
		imagen = self.ui.t_img.text()
		nombre = self.ui.t_marca.text()
		pais = self.ui.t_pais.text()
		return (imagen,nombre,pais)

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	main = Widget_form()
	sys.exit(app.exec_())