import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication, QWidget, QApplication, QPushButton, QMessageBox, QLabel)

class SigSlot(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self)
        self.setWindowTitle('XXX')
        self.btn_newGame = QPushButton('新游戏', self)
        self.btn_setting = QPushButton('设置', self)
        self.btn_ending = QPushButton('结束', self)
        self.btn_aboutQt = QPushButton('关于QT', self)
        self.btn_about = QPushButton('关于', self)
        self.lcd = QLCDNumber(self)
        self.slider = QSlider(Qt.Horizontal,self)
         
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.btn_newGame)
        self.vbox.addWidget(self.btn_setting)
        self.vbox.addWidget(self.btn_ending)
        self.vbox.addWidget(self.btn_aboutQt)
        self.vbox.addWidget(self.btn_about)
        self.vbox.addWidget(self.lcd)
        self.vbox.addWidget(self.slider)
         
        self.setLayout(self.vbox)
        self.resize(400,500)
         
        self.slider.valueChanged.connect(self.lcd.display)
