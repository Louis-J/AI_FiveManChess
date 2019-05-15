# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Works\FiveManChess\UI\Frame.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(1000, 650)
        self.lineEdit = QtWidgets.QLineEdit(Frame)
        self.lineEdit.setGeometry(QtCore.QRect(630, 20, 341, 391))
        self.lineEdit.setObjectName("lineEdit")
        self.btn_repant = QtWidgets.QPushButton(Frame)
        self.btn_repant.setGeometry(QtCore.QRect(740, 430, 111, 51))
        self.btn_repant.setObjectName("btn_repant")
        self.btn_newGame = QtWidgets.QPushButton(Frame)
        self.btn_newGame.setGeometry(QtCore.QRect(630, 430, 101, 51))
        self.btn_newGame.setObjectName("btn_newGame")
        self.btn_ending = QtWidgets.QPushButton(Frame)
        self.btn_ending.setGeometry(QtCore.QRect(860, 430, 111, 51))
        self.btn_ending.setObjectName("btn_ending")
        self.btn_save = QtWidgets.QPushButton(Frame)
        self.btn_save.setGeometry(QtCore.QRect(740, 500, 111, 51))
        self.btn_save.setObjectName("btn_save")
        self.btn_load = QtWidgets.QPushButton(Frame)
        self.btn_load.setGeometry(QtCore.QRect(860, 500, 111, 51))
        self.btn_load.setObjectName("btn_load")
        self.btn_setting = QtWidgets.QPushButton(Frame)
        self.btn_setting.setGeometry(QtCore.QRect(630, 500, 101, 51))
        self.btn_setting.setObjectName("btn_setting")
        self.btn_about = QtWidgets.QPushButton(Frame)
        self.btn_about.setGeometry(QtCore.QRect(630, 570, 161, 51))
        self.btn_about.setObjectName("btn_about")
        self.btn_aboutQt = QtWidgets.QPushButton(Frame)
        self.btn_aboutQt.setGeometry(QtCore.QRect(810, 570, 161, 51))
        self.btn_aboutQt.setObjectName("btn_aboutQt")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Form"))
        self.btn_repant.setText(_translate("Frame", "悔棋"))
        self.btn_newGame.setText(_translate("Frame", "新游戏"))
        self.btn_ending.setText(_translate("Frame", "结束游戏"))
        self.btn_save.setText(_translate("Frame", "保存游戏"))
        self.btn_load.setText(_translate("Frame", "加载游戏"))
        self.btn_setting.setText(_translate("Frame", "设置"))
        self.btn_about.setText(_translate("Frame", "关于"))
        self.btn_aboutQt.setText(_translate("Frame", "关于QT"))

