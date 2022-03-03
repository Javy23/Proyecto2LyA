from unittest import result
from PySide2.QtWidgets import QWidget
from views.main import Colores
import re
import js2py
class Hexadecimal(QWidget, Colores):

    origin = '^#[{a-f}{A-F}{0-9}][{a-f}{A-F}{0-9}][{a-f}{A-F}{0-9}][{a-f}{A-F}{0-9}][{a-f}{A-F}{0-9}][{a-f}{A-F}{0-9}]'
    eInicial = '#'
    reg_exp = "[{a-f}{A-F}{0-9}]"
    result,jsFile = js2py.run_file("controllers\\ntc.js")

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.start)
    
    def start(self):

        self.reset()
        codigo = self.eInicial+ self.lbl.text()

        i = 0
        bandera = self.verificar(self.eInicial, codigo[i])

        if bandera:
            for i in range(1, 7):
                try:
                    bandera = self.verificar(self.reg_exp, codigo[i])
                except IndexError:
                    bandera = False
                    break
                if bandera is False:
                    break
        else:
            self.invalido()

        if bandera:
            self.valido(codigo)
        else:
            self.invalido()

    def verificar(self, exp, num):
        if re.match(exp, num) is not None:
            return True
        return False
    
    def valido(self, codigo):
        self.correcto.setEnabled(True)
        self.correcto.setText('Codigo de color valido :)')
        self.color.setEnabled(True)
        self.color.setStyleSheet("QWidget {background-color: %s}" %codigo)
        self.result = self.jsFile.color(codigo)
        self.nombre.setEnabled(True)
        self.nombre.setText(self.result[1])

    def invalido(self):
        self.incorrecto.setEnabled(True)
        self.incorrecto.setText('Codigo de color invalido :(')
    
    def reset(self):
        self.correcto.setEnabled(False)
        self.correcto.setText('')
        self.incorrecto.setEnabled(False)
        self.incorrecto.setText('')
        self.color.setEnabled(False)
        self.color.setStyleSheet("QWidget {background-color: }")
        self.nombre.setEnabled(False)
        self.nombre.setText('')