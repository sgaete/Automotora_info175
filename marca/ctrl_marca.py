#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore

from ui_widget_marca import Ui_widget_marca
from ctrl_form import Widget_form
import marca.model_marca as model_db


class Widget_marca(QtGui.QWidget):
    """
    Marca
    """
    
    table_columns = (
		(u"id", 10),
		(u"Marca", 150),
		(u"Pais", 120),
		(u"Cantidad", 75))
        
    def __init__(self, parent=None):
        super(Widget_marca, self).__init__(parent)
        self.ui = Ui_widget_marca()
        self.ui.setupUi(self)
        self.load_data()
        self.signals()
        self.show()


    def signals(self):
        self.ui.table_marc.clicked.connect(self.show_logo)

    
    def show_logo(self, index):
        index = index if index is not None\
            else self.ui.table_marc.currentIndex()
            
        data = self.ui.table_marc.model()
        marca = data.item(index.row(),0).marca
        img = QtGui.QPixmap(str(marca['imagen']))
        self.ui.label_5.setPixmap(img)        
        #imagenes redimencionadas a 400x500
        print "Ha seleccionado la marca: "+(str(marca['nombre']))


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
            row = [marca["id"], marca["nombre"], marca["pais"]]
            for j, field in enumerate(row):
                index = data.index(i, j, QtCore.QModelIndex())
                data.setData(index, field)
            data.item(i).marca = marca
	
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Widget_marca()
    sys.exit(app.exec_())
