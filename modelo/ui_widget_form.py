# -*- coding: utf-8 -*-


from PySide import QtCore, QtGui
import time


class Ui_Form(object):

	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(450, 464)
		Form.setMinimumSize(QtCore.QSize(450, 400))
		self.gridLayout = QtGui.QGridLayout(Form)
		self.gridLayout.setObjectName("gridLayout")
		self.label_6 = QtGui.QLabel(Form)
		font = QtGui.QFont()
		font.setFamily("Noto Sans [unknown]")
		font.setWeight(75)
		font.setBold(True)
		self.label_6.setFont(font)
		self.label_6.setObjectName("label_6")
		self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
		self.label_8 = QtGui.QLabel(Form)
		font = QtGui.QFont()
		font.setFamily("Noto Sans [unknown]")
		font.setWeight(75)
		font.setBold(True)
		self.label_8.setFont(font)
		self.label_8.setObjectName("label_8")
		self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
		self.label_9 = QtGui.QLabel(Form)
		font = QtGui.QFont()
		font.setFamily("Noto Sans [unknown]")
		font.setWeight(75)
		font.setBold(True)
		self.label_9.setFont(font)
		self.label_9.setObjectName("label_9")
		self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
		self.label_2 = QtGui.QLabel(Form)
		font = QtGui.QFont()
		font.setFamily("Noto Sans [unknown]")
		font.setWeight(75)
		font.setBold(True)
		self.label_2.setFont(font)
		self.label_2.setObjectName("label_2")
		self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
		self.label_5 = QtGui.QLabel(Form)
		font = QtGui.QFont()
		font.setFamily("Noto Sans [unknown]")
		font.setWeight(75)
		font.setBold(True)
		self.label_5.setFont(font)
		self.label_5.setObjectName("label_5")
		self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
		self.label = QtGui.QLabel(Form)
		font = QtGui.QFont()
		font.setFamily("Noto Sans [unknown]")
		font.setWeight(75)
		font.setBold(True)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
		self.label_4 = QtGui.QLabel(Form)
		font = QtGui.QFont()
		font.setFamily("Noto Sans [unknown]")
		font.setWeight(75)
		font.setBold(True)
		self.label_4.setFont(font)
		self.label_4.setObjectName("label_4")
		self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
		self.label_3 = QtGui.QLabel(Form)
		font = QtGui.QFont()
		font.setFamily("Noto Sans [unknown]")
		font.setWeight(75)
		font.setBold(True)
		self.label_3.setFont(font)
		self.label_3.setObjectName("label_3")
		self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)
		self.n_img = QtGui.QLineEdit(Form)
		self.n_img.setReadOnly(True)
		self.n_img.setObjectName("n_img")
		self.gridLayout.addWidget(self.n_img, 7, 1, 1, 1)
		self.open_qfile = QtGui.QPushButton(Form)
		self.open_qfile.setObjectName("open_qfile")
		self.gridLayout.addWidget(self.open_qfile, 7, 2, 1, 1)
		self.label_7 = QtGui.QLabel(Form)
		font = QtGui.QFont()
		font.setFamily("Noto Sans [unknown]")
		font.setWeight(75)
		font.setBold(True)
		self.label_7.setFont(font)
		self.label_7.setObjectName("label_7")
		self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)
		self.n_descrip = QtGui.QTextEdit(Form)
		self.n_descrip.setObjectName("n_descrip")
		self.gridLayout.addWidget(self.n_descrip, 8, 1, 1, 2)
		self.n_modelo = QtGui.QLineEdit(Form)
		self.n_modelo.setMaxLength(250)
		self.n_modelo.setObjectName("n_modelo")
		self.gridLayout.addWidget(self.n_modelo, 0, 1, 1, 2)
		self.n_marca = QtGui.QComboBox(Form)
		self.n_marca.setObjectName("n_marca")
		self.gridLayout.addWidget(self.n_marca, 1, 1, 1, 2)
		self.n_motor = QtGui.QLineEdit(Form)
		self.n_motor.setMaxLength(100)
		self.n_motor.setObjectName("n_motor")
		self.gridLayout.addWidget(self.n_motor, 2, 1, 1, 2)
		self.n_rend = QtGui.QSpinBox(Form)
		self.n_rend.setAlignment(
			QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
		self.n_rend.setMinimum(5)
		self.n_rend.setMaximum(80)
		self.n_rend.setObjectName("n_rend")
		self.gridLayout.addWidget(self.n_rend, 3, 1, 1, 2)
		self.n_precio = QtGui.QSpinBox(Form)
		self.n_precio.setAlignment(
			QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
		self.n_precio.setMinimum(3000000)
		self.n_precio.setMaximum(499999999)
		self.n_precio.setObjectName("n_precio")
		self.gridLayout.addWidget(self.n_precio, 4, 1, 1, 2)
		self.n_peso = QtGui.QDoubleSpinBox(Form)
		self.n_peso.setAlignment(
			QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
		self.n_peso.setPrefix("")
		self.n_peso.setMinimum(500.0)
		self.n_peso.setMaximum(9999.0)
		self.n_peso.setObjectName("n_peso")
		self.gridLayout.addWidget(self.n_peso, 5, 1, 1, 2)
		self.n_fecha = QtGui.QDateEdit(Form)
		self.n_fecha.setAlignment(
			QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
		self.n_fecha.setDate(QtCore.QDate(int(time.strftime("%Y")), int(
			time.strftime("%m")), int(time.strftime("%d"))))
		self.n_fecha.setCalendarPopup(True)
		self.n_fecha.setObjectName("n_fecha")
		self.gridLayout.addWidget(self.n_fecha, 6, 1, 1, 2)
		self.widget = QtGui.QWidget(Form)
		self.widget.setObjectName("widget")
		self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.acepta_mod = QtGui.QPushButton(self.widget)
		self.acepta_mod.setObjectName("acepta_mod")
		self.horizontalLayout.addWidget(self.acepta_mod)
		self.cancel = QtGui.QPushButton(self.widget)
		self.cancel.setObjectName("cancel")
		self.horizontalLayout.addWidget(self.cancel)
		self.gridLayout.addWidget(self.widget, 9, 0, 1, 3)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		Form.setWindowTitle(QtGui.QApplication.translate(
			"Form", "Modelo", None, QtGui.QApplication.UnicodeUTF8))
		self.label_6.setText(QtGui.QApplication.translate(
			"Form", "Modelo:", None, QtGui.QApplication.UnicodeUTF8))
		self.label_8.setText(QtGui.QApplication.translate(
			"Form", "Marca:", None, QtGui.QApplication.UnicodeUTF8))
		self.label_9.setText(QtGui.QApplication.translate(
			"Form", "Motor:", None, QtGui.QApplication.UnicodeUTF8))
		self.label_2.setText(QtGui.QApplication.translate(
			"Form", "Rendimiento:", None, QtGui.QApplication.UnicodeUTF8))
		self.label_5.setText(QtGui.QApplication.translate(
			"Form", "Precio:", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate(
			"Form", "Peso:", None, QtGui.QApplication.UnicodeUTF8))
		self.label_4.setText(QtGui.QApplication.translate(
			"Form", "Fecha de Creación: ", None, QtGui.QApplication.UnicodeUTF8))
		self.label_3.setText(QtGui.QApplication.translate(
			"Form", "Imagen:", None, QtGui.QApplication.UnicodeUTF8))
		self.open_qfile.setText(QtGui.QApplication.translate(
			"Form", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
		self.label_7.setText(QtGui.QApplication.translate(
			"Form", "Descripción:", None, QtGui.QApplication.UnicodeUTF8))
		self.n_rend.setSuffix(QtGui.QApplication.translate(
			"Form", "Km/L", None, QtGui.QApplication.UnicodeUTF8))
		self.n_precio.setSuffix(QtGui.QApplication.translate(
			"Form", "$", None, QtGui.QApplication.UnicodeUTF8))
		self.n_peso.setSuffix(QtGui.QApplication.translate(
			"Form", "Kg", None, QtGui.QApplication.UnicodeUTF8))
		self.n_fecha.setDisplayFormat(QtGui.QApplication.translate(
			"Form", "yyyy-MM-dd", None, QtGui.QApplication.UnicodeUTF8))
		self.acepta_mod.setText(QtGui.QApplication.translate(
			"Form", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
		self.cancel.setText(QtGui.QApplication.translate(
			"Form", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
