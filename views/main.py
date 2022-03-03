# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Colores(object):
    def setupUi(self, Colores):
        if not Colores.objectName():
            Colores.setObjectName(u"Colores")
        Colores.resize(470, 387)
        font = QFont()
        font.setPointSize(33)
        Colores.setFont(font)
        self.label = QLabel(Colores)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, -20, 451, 121))
        font1 = QFont()
        font1.setFamily(u"Arial Black")
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setFrameShape(QFrame.NoFrame)
        self.label_2 = QLabel(Colores)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(145, 80, 21, 41))
        font2 = QFont()
        font2.setFamily(u"Arial Black")
        font2.setPointSize(25)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_2.setFont(font2)
        self.lbl = QLineEdit(Colores)
        self.lbl.setObjectName(u"lbl")
        self.lbl.setGeometry(QRect(170, 80, 131, 41))
        font3 = QFont()
        font3.setPointSize(25)
        self.lbl.setFont(font3)
        self.lbl.setLayoutDirection(Qt.LeftToRight)
        self.lbl.setMaxLength(6)
        self.lbl.setAlignment(Qt.AlignCenter)
        self.btn = QPushButton(Colores)
        self.btn.setObjectName(u"btn")
        self.btn.setGeometry(QRect(190, 140, 81, 31))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(12)
        self.btn.setFont(font4)
        self.color = QFrame(Colores)
        self.color.setObjectName(u"color")
        self.color.setGeometry(QRect(160, 230, 151, 111))
        self.color.setFrameShape(QFrame.StyledPanel)
        self.color.setFrameShadow(QFrame.Raised)
        self.correcto = QLabel(Colores)
        self.correcto.setObjectName(u"correcto")
        self.correcto.setEnabled(False)
        self.correcto.setGeometry(QRect(120, 180, 231, 41))
        font5 = QFont()
        font5.setPointSize(16)
        self.correcto.setFont(font5)
        self.nombre = QLabel(Colores)
        self.nombre.setObjectName(u"nombre")
        self.nombre.setGeometry(QRect(110, 340, 251, 41))
        font6 = QFont()
        font6.setPointSize(14)
        self.nombre.setFont(font6)
        self.nombre.setAlignment(Qt.AlignCenter)
        self.incorrecto = QLabel(Colores)
        self.incorrecto.setObjectName(u"incorrecto")
        self.incorrecto.setEnabled(False)
        self.incorrecto.setGeometry(QRect(80, 200, 331, 41))
        font7 = QFont()
        font7.setPointSize(19)
        self.incorrecto.setFont(font7)

        self.retranslateUi(Colores)

        QMetaObject.connectSlotsByName(Colores)
    # setupUi

    def retranslateUi(self, Colores):
        Colores.setWindowTitle(QCoreApplication.translate("Colores", u"Form", None))
        self.label.setText(QCoreApplication.translate("Colores", u"Digite el codigo del color en hexadecimal", None))
        self.label_2.setText(QCoreApplication.translate("Colores", u"#", None))
        self.lbl.setText("")
        self.btn.setText(QCoreApplication.translate("Colores", u"Verificar", None))
        self.correcto.setText("")
        self.nombre.setText("")
        self.incorrecto.setText("")
    # retranslateUi

