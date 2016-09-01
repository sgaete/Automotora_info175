#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui
from ui_main import Ui_Main
from modelo.ctrl_modelo import Widget_modelo

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
        self.ui.actionModelos.triggered.connect(self.load_modelo)
        self.ui.actionMarcas.triggered.connect(self.load_marca)
        self.ui.actionClientes.triggered.connect(self.load_cliente)
        self.ui.actionVentas.triggered.connect(self.load_venta)
        
    def load_modelo(self):
        widget = Widget_modelo(self)
        self.setCentralWidget(widget)
    def load_marca(self):
        widget = Widget_marca(self)
        self.setCentralWidget(widget)
    def load_cliente(self):
        widget = Widget_cliente(self)
        self.setCentralWidget(widget)
    def load_venta(self):
        widget = Widget_venta(self)
        self.setCentralWidget(widget)
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
