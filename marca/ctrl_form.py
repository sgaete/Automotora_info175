#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from ui_widget_form import Ui_Form
import marca.model_marca as model_db

class Widget_form(QtGui.QWidget):
    """
    formulario de marcas
    """
    def __init__(self, parent=None, id=None):
        super(Widget_form, self).__init__(parent)
        self.ui = Ui_widget_form()
        self.ui.setupUi(self)
        self.show()
        if id is None:
            self.ui.savemarca.clicked.connect(self.crear_marca)
        else:
            self.colocar_datos(id)
            self.ui.savemarca.clicked.connect(self.editar_marca)

	def obtener_dato(self):
		print "obtener dato"
		nombre = self.ui.t_marca.text()
		pais = self.ui.t_pais.text()
		return (nombre,pais)
	
	def colocar_datos(self, id):
		print "colocar dato"
		marca = model_marca.marca(id)
		self.ui.nombre.setText(marca["nombre"])
		self.ui.pais.setText(marca["pais"])


	def editar_marca(self):
		print "editar marca"
		nombre = self.obtener_dato()
		pais = selft.obtener_dato()

	
	def crear_marca(self):
		print "crear marca"
		nombre = self.obtener_dato()
		pais = self.obtener_dato()
		try: 
				model_db.crear_marca(nombre,pais)
				self.accepted.emit()
				self.close()
		except:
				#Tratar errores!!!!!!
				pass
			
	
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Widget_form()
    sys.exit(app.exec_())
