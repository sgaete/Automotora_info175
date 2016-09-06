#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from ui_widget_vent import Ui_widget_vent
from ctrl_form import FormVenta
import venta.model_vent as model_db


class Widget_vent(QtGui.QWidget):
    """
    Venta
    """
    def __init__(self, parent=None):
        super(Widget_vent, self).__init__(parent)
        self.ui = Ui_widget_vent()
        self.ui.setupUi(self)

        self.load_data()
        self.connect_signals()

    def connect_signals(self):
    	"""captura la señal de los botones agregar venta y eliminar venta"""
        self.ui.btn_agregar_vent.clicked.connect(self.add)
        self.ui.btn_eliminar_vent.clicked.connect(self.delete)
       


    def add(self):
    	"""Se despliega el formulario de vantas"""
        self.ui.ui_from_vent = FormVenta(self)
        self.ui.ui_from_vent.accepted.connect(self.load_data)
        self.ui.ui_from_vent.exec_()



    def load_data(self):
        """
        Función que carga la información de autos en la grilla
        """
        datos = model_db.obtener_datos()
        #Creamos el modelo asociado a la tabla
        self.data = QtGui.QStandardItemModel(len(datos), 8)
        self.data.setHorizontalHeaderItem(
            0, QtGui.QStandardItem(u"RUT"))
        self.data.setHorizontalHeaderItem(
            1, QtGui.QStandardItem(u"Nombres"))
        self.data.setHorizontalHeaderItem(
            2, QtGui.QStandardItem(u"Apellidos"))
        self.data.setHorizontalHeaderItem(
            3, QtGui.QStandardItem(u"Modelo"))
        self.data.setHorizontalHeaderItem(
            4, QtGui.QStandardItem(u"Marca"))
        self.data.setHorizontalHeaderItem(
            5, QtGui.QStandardItem(u"Patente"))
        self.data.setHorizontalHeaderItem(
            6, QtGui.QStandardItem(u"Color"))
        self.data.setHorizontalHeaderItem(
            7, QtGui.QStandardItem(u"Precio de venta"))

        for r, row in enumerate(datos):

            index = self.data.index(r, 0, QtCore.QModelIndex())
            self.data.setData(index, row['rut'])
            index = self.data.index(r, 1, QtCore.QModelIndex())
            self.data.setData(index, row['nombres'])
            index = self.data.index(r, 2, QtCore.QModelIndex())
            self.data.setData(index, row['apellidos'])
            index = self.data.index(r, 3, QtCore.QModelIndex())
            self.data.setData(index, row['modelo'])
            index = self.data.index(r, 4, QtCore.QModelIndex())
            self.data.setData(index, row['marca'])
            index = self.data.index(r, 5, QtCore.QModelIndex())
            self.data.setData(index, row['patente'])
            index = self.data.index(r, 6, QtCore.QModelIndex())
            self.data.setData(index, row['color'])
            index = self.data.index(r, 7, QtCore.QModelIndex())
            self.data.setData(index, row['precio_venta'])

        self.ui.table_vent.setModel(self.data)

        # Para que las columnas 1 y 2 se estire o contraiga cuando
        # se cambia el tamaño de la pantalla
        self.ui.table_vent.horizontalHeader().setResizeMode(
            1, self.ui.table_vent.horizontalHeader().Stretch)
        self.ui.table_vent.horizontalHeader().setResizeMode(
            2, self.ui.table_vent.horizontalHeader().Stretch)

        self.ui.table_vent.setColumnWidth(0, 100)
        self.ui.table_vent.setColumnWidth(1, 210)
        self.ui.table_vent.setColumnWidth(2, 210)
        self.ui.table_vent.setColumnWidth(3, 100)
        self.ui.table_vent.setColumnWidth(4, 100)
        self.ui.table_vent.setColumnWidth(5, 100)
        self.ui.table_vent.setColumnWidth(6, 100)
        self.ui.table_vent.setColumnWidth(7, 150)




    def delete(self):
        """
        Función que un autos de la base de datos e
        indica el resultado de la operación
        """
        data = self.ui.table_vent.model()
        index = self.ui.table_vent.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage(u"Debe seleccionar una fila")
            return False
        else:
            patente = data.index(index.row(), 5, QtCore.QModelIndex()).data()
            if (model_db.borrar(patente)):
                self.load_data()
                msgBox = QtGui.QMessageBox()
                msgBox.setText(u"EL registro fue eliminado.")
                msgBox.exec_()
                return True
            else:
                self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
                self.ui.errorMessageDialog.showMessage(
                    u"Error al eliminar el registro")
                return False
