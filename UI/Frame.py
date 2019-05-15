import os
import sys
from .Setting import Setting
from .ColorDefine import Color
from .ChessBoard import ChessBoard
from .Ui_Frame import Ui_Frame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QPainter, QPen, QBrush)
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication, QWidget, QPushButton, QMessageBox, QLabel)


class Frame(QWidget, Setting):
    playing = False
    V = 16
    H = 16

    def __init__(self, AI, parent=None):
        QWidget.__init__(self)
        
        self.AI = AI
        self.SettingLoad()
        self.board = ChessBoard(self.V, self.H, self.WhoFirst)

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        
        self.ui.btn_newGame.clicked.connect(self.OnClick_NewGame)
        self.ui.btn_setting.clicked.connect(self.OnClick_Setting)
        self.ui.btn_ending .clicked.connect(self.OnClick_Ending)
        self.ui.btn_repant .clicked.connect(self.OnClick_Repant)
        self.ui.btn_save   .clicked.connect(self.OnClick_Save)
        self.ui.btn_load   .clicked.connect(self.OnClick_Load)
        self.ui.btn_about  .clicked.connect(self.OnClick_About)
        self.ui.btn_aboutQt.clicked.connect(self.OnClick_AboutQt)

    def __del__(self):
        self.SettingSave()
        del self.ui

    def PaintBoarder(self):
        pen = QPen()
        pen.setWidth(4)
        pen.setColor(Qt.blue)

        painter = QPainter(self)
        painter.setPen(pen)

        painter.drawLine(18,18,622,18)
        painter.drawLine(18,622,622,622)
        painter.drawLine(18,18,18,622)
        painter.drawLine(622,18,622,622)

    def PaintLines(self):
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(Qt.black)

        painter = QPainter(self)
        painter.setPen(pen)

        for x in range(60, 620, 40):
            painter.drawLine(x,20,x,620)
        for y in range(60, 620, 40):
            painter.drawLine(20,y,620,y)

    def PaintMans(self):
        print('A')
        board = self.board.board
        brush = QBrush(Qt.black)
        painter = QPainter(self)
        painter.setBrush(brush)
        for x in range(0, self.H):
            for y in range(0, self.V):
                if board[y * self.H + x] == Color.B:
                    painter.save()
                    painter.drawEllipse(x * 40, y * 40, 40, 40)
                    painter.restore()
        print('B')

        brush = QBrush(Qt.red)
        painter.setBrush(brush)
        for x in range(0, self.H):
            for y in range(0, self.V):
                if board[y * self.H + x] == Color.R:
                    painter.save()
                    painter.drawEllipse(x * 40, y * 40, 40, 40)
                    painter.restore()
        print('C')

    def paintEvent(self, event):
        self.PaintBoarder()
        self.PaintLines()
        self.PaintMans()

    def PaintStatusBar(self, info):
        print('StatusBar:')
        print(info)
        pass
        # TODO:

    def OnClick_NewGame(self):
        if self.playing == True:
            reply = QMessageBox.question(self, '询问', '正在对局中，是否重新开始游戏？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply != QMessageBox.Yes:
                return
        self.playing = True
        self.board.NewGame()

    def OnClick_Setting(self):
        if self.playing == True:
            QMessageBox.critical(self, '错误', '请结束游戏后重新设置', QMessageBox.Ok, QMessageBox.Ok)
            return
        self.SettingDialog(self)

    def OnClick_Ending(self):
        self.playing = False

    def OnClick_Repant(self):
        if self.playing != True:
            QMessageBox.critical(self, '错误', '未在游戏中，请先开始游戏', QMessageBox.Ok, QMessageBox.Ok)
            return
        if not self.board.Repent():
            QMessageBox.critical(self, '错误', '无法再回退', QMessageBox.Ok, QMessageBox.Ok)

    def OnClick_About(self):
        QMessageBox.about(self, '关于', '作者：zcy/dcy<br><a href="http://github.com">homepage</a>')

    def OnClick_Save(self):
        pass
    def OnClick_Load(self):
        pass

    def OnClick_AboutQt(self):
        QMessageBox.aboutQt(self.ui, '关于Qt')

    def OnClick_ChessRepent(self):
        if self.playing != True:
            QMessageBox.critical(self.ui, '错误', '还未开始游戏', QMessageBox.Ok, QMessageBox.Ok)
            return
        if not self.board.Repent():
            QMessageBox.critical(self.ui, '错误', '无法再悔棋', QMessageBox.Ok, QMessageBox.Ok)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            x = event.x()
            y = event.y()
            if x < 641 and y < 641:
                if self.board.Put(int(x / 40), int(y / 40)):
                    print(int(x / 40), int(y / 40))
                    self.update()
                if self.board.CheckWin():
                    QMessageBox.about(self.ui, '胜负已分！', '胜负已分！')
                    self.playing = False
                elif self.board.CheckFull():
                    QMessageBox.about(self.ui, '和棋！', '和棋！')
                    self.playing = False
