# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui


class Ui_widget_modelo(object):

	def setupUi(self, widget_modelo):
		widget_modelo.setObjectName("widget_modelo")
		widget_modelo.resize(860, 710)
		self.gridLayout = QtGui.QGridLayout(widget_modelo)
		self.gridLayout.setObjectName("gridLayout")
		self.widget = QtGui.QWidget(widget_modelo)
		self.widget.setObjectName("widget")
		self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.label = QtGui.QLabel(self.widget)
		self.label.setObjectName("label")
		self.horizontalLayout.addWidget(self.label)
		self.combo_Marcas = QtGui.QComboBox(self.widget)
		self.combo_Marcas.setObjectName("combo_Marcas")
		self.horizontalLayout.addWidget(self.combo_Marcas)
		spacerItem = QtGui.QSpacerItem(
			40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
		self.busca_mod = QtGui.QLineEdit(self.widget)
		self.busca_mod.setObjectName("busca_mod")
		self.horizontalLayout.addWidget(self.busca_mod)
		self.horizontalLayout.setStretch(0, 1)
		self.horizontalLayout.setStretch(1, 1)
		self.horizontalLayout.setStretch(2, 4)
		self.horizontalLayout.setStretch(3, 2)
		self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
		self.line = QtGui.QFrame(widget_modelo)
		self.line.setFrameShape(QtGui.QFrame.VLine)
		self.line.setFrameShadow(QtGui.QFrame.Sunken)
		self.line.setObjectName("line")
		self.gridLayout.addWidget(self.line, 0, 1, 3, 1)
		self.widget_3 = QtGui.QWidget(widget_modelo)
		self.widget_3.setObjectName("widget_3")
		self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_3)
		self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.lbl_imagen = QtGui.QLabel(self.widget_3)
		self.lbl_imagen.setObjectName("lbl_imagen")
		self.lbl_imagen.setAlignment(QtCore.Qt.AlignHCenter)
		self.verticalLayout_2.addWidget(self.lbl_imagen)
		self.label_3 = QtGui.QLabel(self.widget_3)
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setWeight(75)
		font.setBold(True)
		self.label_3.setFont(font)
		self.label_3.setAlignment(
			QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
		self.label_3.setObjectName("label_3")
		self.verticalLayout_2.addWidget(self.label_3)
		self.lbl_detalles = QtGui.QLabel(self.widget_3)
		self.lbl_detalles.setAlignment(
			QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
		self.lbl_detalles.setText("")
		self.lbl_detalles.setObjectName("lbl_detalles")
		self.verticalLayout_2.addWidget(self.lbl_detalles)
		self.label_4 = QtGui.QLabel(self.widget_3)
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setWeight(75)
		font.setBold(True)
		self.label_4.setFont(font)
		self.label_4.setAlignment(
			QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
		self.label_4.setObjectName("label_4")
		self.verticalLayout_2.addWidget(self.label_4)
		self.lbl_descrip = QtGui.QLabel(self.widget_3)
		self.lbl_descrip.setText("")
		self.lbl_descrip.setObjectName("lbl_descrip")
		self.verticalLayout_2.addWidget(self.lbl_descrip)
		self.gridLayout.addWidget(self.widget_3, 0, 2, 3, 1)
		self.table_mod = QtGui.QTableView(widget_modelo)
		self.table_mod.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.table_mod.setAlternatingRowColors(True)
		self.table_mod.setSelectionMode(
			QtGui.QAbstractItemView.SingleSelection)
		self.table_mod.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
		self.table_mod.setSortingEnabled(True)
		self.table_mod.setObjectName("table_mod")
		self.gridLayout.addWidget(self.table_mod, 1, 0, 1, 1)
		self.widget_2 = QtGui.QWidget(widget_modelo)
		self.widget_2.setObjectName("widget_2")
		self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
		self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		spacerItem1 = QtGui.QSpacerItem(
			509, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout_2.addItem(spacerItem1)
		self.btn_agrega_mod = QtGui.QPushButton(self.widget_2)
		self.btn_agrega_mod.setObjectName("btn_agrega_mod")
		self.horizontalLayout_2.addWidget(self.btn_agrega_mod)
		self.btn_edita_mod = QtGui.QPushButton(self.widget_2)
		self.btn_edita_mod.setObjectName("btn_edita_mod")
		self.horizontalLayout_2.addWidget(self.btn_edita_mod)
		self.btn_borra_mod = QtGui.QPushButton(self.widget_2)
		self.btn_borra_mod.setObjectName("btn_borra_mod")
		self.horizontalLayout_2.addWidget(self.btn_borra_mod)
		self.gridLayout.addWidget(self.widget_2, 2, 0, 1, 1)
		self.gridLayout.setColumnStretch(0, 2)
		self.gridLayout.setColumnStretch(2, 1)

		self.retranslateUi(widget_modelo)
		QtCore.QMetaObject.connectSlotsByName(widget_modelo)

	def retranslateUi(self, widget_modelo):
		widget_modelo.setWindowTitle(QtGui.QApplication.translate(
			"widget_modelo", "Form", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate(
			"widget_modelo", "Filtrar marca:", None, QtGui.QApplication.UnicodeUTF8))
		self.busca_mod.setPlaceholderText(QtGui.QApplication.translate(
			"widget_modelo", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
		self.lbl_imagen.setText(QtGui.QApplication.translate(
			"widget_modelo", "Imagen", None, QtGui.QApplication.UnicodeUTF8))
		self.label_3.setText(QtGui.QApplication.translate(
			"widget_modelo", "Detalles:", None, QtGui.QApplication.UnicodeUTF8))
		self.label_4.setText(QtGui.QApplication.translate(
			"widget_modelo", "Descripción:", None, QtGui.QApplication.UnicodeUTF8))
		self.btn_agrega_mod.setText(QtGui.QApplication.translate(
			"widget_modelo", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
		self.btn_edita_mod.setText(QtGui.QApplication.translate(
			"widget_modelo", "Editar", None, QtGui.QApplication.UnicodeUTF8))
		self.btn_borra_mod.setText(QtGui.QApplication.translate(
			"widget_modelo", "Borrar", None, QtGui.QApplication.UnicodeUTF8))
