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
			self.ui.savemarca.clicked.connect(self.crear_marca)  #al precionar aceptar se crea la nueva marca con todos los datos 
			self.ui.buscar_img.clicked.connect(self.abririmg)	#accion del boton buscar logo dentro del formulario
		else:
			self.colocar_datos(marc_id)			#al abrir la ventana de edicion, se cargan los datos automaticamente
			self.ui.savemarca.clicked.connect(		#se presiona al finalizar la edicion, se guardan los cambios
				lambda: self.editar_marca(marc_id))  
			self.ui.buscar_img.clicked.connect(self.abririmg)	#busca un logo en sus archivos

		self.ui.cancel.clicked.connect(self.close)		#boton que cierra los formularios

	def signals(self):		#no se ocupa
		pass

	def colocar_datos(self, marc_id):		#seteamos los datos de la marca en la ventana de edicion automaticamente
		print " --- Colocando datos... ---"
		marca = model_db.marca(marc_id)
		print "Datos puestos en la ventana de editar: "
		i=str(marca[0]).strip()			#obtenemos los 3 datos necesarios (nombre,pais,imagen)
		n=str(marca[1]).strip()
		p=str(marca[2]).strip()
		print "- Marca: "+str(marca[0])
		print "- Pais: "+str(marca[1])
		print "- Ruta logo: "+str(marca[2])
		self.ui.t_marca.setText(i)			#aqui seteamos para que el usuario los vea al abrir el formulario
		self.ui.t_pais.setText(n)
		self.ui.t_img.setText(p)
	
	#si se presiona aceptar se ejecuta...
	def crear_marca(self):			#cuando se quiere crear una nueva marca se ejecuta lo siguiente
		imagen, nombre, pais = self.obtener_dato()
		ii=imagen.strip()			#obtenemos los datos segun la marca 
		nn=nombre.strip()			#le quitamos los espacios (si es que tienen)
		pp=pais.strip()

		b=False
		uno=""
		dos=""
		#print nn
		m = model_db.marca(nn)

		if(m is None):					#si es nulo se puede crear una marca (no existe una igual)
			print "Es nulo (no se encuentran similitudes con otras marcas)"
			b=True
		else:		
			#print m[0]
			uno = str(m[0]).strip()
			uno = uno.lower()
			#print uno
			dos = nn.lower()
			#print dos

			#print "uno="+uno+" dos="+dos

		if(uno!=dos or b):		#si son distintos se puede continuar con la creacion (son los datos obtenidos del line edit con los de la base de datos)
			if(ii=="" or nn=="" or pp==""):	#aqui nos aseguramos que los campos no sean vacios, muestra sus respectivos mensajes segun corresponda
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
				#a continuacion se ve el tema de copiar un logo en el directorio del programa
				ruta = os.getcwd() + os.sep
				origen = imagen
				destino = "marca/logos/"+nombre+".png"  #definimos la ruta y archivo del logo de la marca
				#print origen
				#print destino
				try:	#tratamos los errores de la copia de los archivos (logos)
				    shutil.copyfile(origen, destino)
				    print("Logotipo copiado satisfactoriamente")
				except:
				    print("Se ha producido un error en el copiado del logo")
			
				model_db.crear_marca(destino,n,p)   #creamos la nueva marca, se hace un insert
				self.accepted.emit()
				print "Creacion de nueva marca finalizada!"
				print " - Nueva marca: "+n
				print " - Del pais: "+p
				print " - Ruta del logo: "+destino
				self.close()
		else:				#no se puede crear porque se encuentra la marca en el registro
			if(uno==dos):  #en la BD se encuentra lo que señala el lineedit
				QtGui.QMessageBox.information(self, "Aviso","La marca que esta ingresando ya se encuentra en la base de datos de la automotora.")
				self.close()

	def editar_marca(self,marc_id):	#metodo que edita la marca
		imagen,nombre,pais = self.obtener_dato()
		ii=imagen.strip()		#obtenemos los datos necesarios para la edicion de una marca
		ii2=ii
		nn=nombre.strip()
		pp=pais.strip()
		if(ii=="" or nn=="" or pp==""):		#se verifica que los campos esten completos
			if(nn==""):
				QtGui.QMessageBox.information(self, "Campo incompleto", "No ha ingresado ningun nombre para la marca")
			if(pp==""):
				QtGui.QMessageBox.information(self, "Campo incompleto", "No ha ingresado ningun pais")
			if(ii==""):
				QtGui.QMessageBox.information(self, "Campo incompleto", "No ha ingresado ningun logo para su marca")
		else:
			i = imagen
			n = nombre.upper()		#definimos un tipo de letra para la BD
			p = pais.title()
			print "Datos obtenidos:"
			print "- Marca: "+nombre
			print "- Pais: "+pais
			print "- Direccion de la img: "+imagen    
			ruta = os.getcwd() + os.sep
			origen = imagen
			destino = "marca/logos/"+nombre+".png"   #copiamos la imagen en la carpeta del programa
			#print origen
			#print destino
			try:
			    shutil.copyfile(origen, destino)	#si se pudo copiar el logo
			    print("Logotipo copiado satisfactoriamente")
			except:
			    print("Se ha producido un error en el copiado del logo")  # el logo no se pudo copiar
			model_db.edit_marca(ii,nn,pp,marc_id)			#insertamos los datos en la base de datos
			self.accepted.emit()
			print "Edicion de la marca ha finalizado!"
			print " - Marca: "+nn
			print " - Pais: "+pp
			print " - Ruta del logo: "+destino
		#os.remove(ii2)
		self.close()

	def abririmg(self):		#se llama cuando queremos buscar un logo en el ordenador
		n=self.obtenerNombre()	#primero necesitamos el nombre de la marca, ya que se le definira en la ruta del logo
		if(n!=""):			#ejecutamos el dialogo que busca la img
			ruta_logo = QtGui.QFileDialog.getOpenFileName(self, "Abrir imagen","/home/","Image Files (*.png *.jpg *.bmp)")
			print ruta_logo[0]	#obtenemos la ruta
			self.ui.t_img.setText(str(ruta_logo[0]))		#la seteamos al label
		else:
			QtGui.QMessageBox.information(self, "Aviso", "Antes de seleccionar un logo debe ingresar el nombre de la marca a registrar")

	def obtenerNombre(self):       #para validar el metodo abririmg()
		nombre = self.ui.t_marca.text()	#obtenemos el nombre de la marca 
		return nombre

	def obtener_dato(self):			#cuando se necesiten datos, se llama este metodo que busca esa info
		print " --- Obteniendo datos... ---"
		imagen = self.ui.t_img.text()
		nombre = self.ui.t_marca.text()
		pais = self.ui.t_pais.text()
		return (imagen,nombre,pais)

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	main = Widget_form()
	sys.exit(app.exec_())
