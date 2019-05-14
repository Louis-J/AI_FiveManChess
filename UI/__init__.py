import json
import os
import sys
from .Setting import Setting
from .SigSlot import SigSlot
from .ChessBoard import ChessBoard
from .ColorDefine import Color
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication, QWidget, QApplication, QPushButton, QMessageBox, QLabel)
# from Frame import frame


class UI(Setting):
    playing = False
    V = 16
    H = 16
    def __init__(self, AI):
        self.AI = AI
        self.SettingLoad()
        self.board = ChessBoard(self.V, self.H, self.WhoFirst)
        
        app = QApplication(sys.argv)
        self.qb = SigSlot()
        self.qb.btn_newGame.clicked.connect(self.OnClick_NewGame)
        self.qb.btn_setting.clicked.connect(self.OnClick_Setting)
        self.qb.btn_ending .clicked.connect(self.OnClick_Ending)
        self.qb.btn_aboutQt.clicked.connect(self.OnClick_AboutQt)
        self.qb.btn_about  .clicked.connect(self.OnClick_About)
        self.qb.show()
        sys.exit(app.exec_())
        # self.frame = frame()
        # TODO:

    def __del__(self):
        self.SettingSave()

    def Paint(self):
        pass
        # TODO:

    def PaintStatusBar(self, info):
        print('StatusBar:')
        print(info)
        pass
        # TODO:

    def OnClick_NewGame(self):
        if self.playing == True:
            reply = QMessageBox.question(self.qb, '询问', '正在对局中，是否重新开始游戏？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply != QMessageBox.Yes:
                return
        self.playing = True
        self.board.NewGame()

    def OnClick_Setting(self):
        if self.playing == True:
            QMessageBox.critical(self.qb, '错误', '请结束游戏后重新设置', QMessageBox.Ok, QMessageBox.Ok)
            return
        self.SettingDialog()

    def OnClick_Ending(self):
        self.playing = False

    def OnClick_About(self):
        QMessageBox.about(self.qb, '关于', '作者：zcy/dcy<br><a href="http://github.com">homepage</a>')

    def OnClick_AboutQt(self):
        QMessageBox.aboutQt(self.qb, '关于Qt')

    def OnClick_ChessPut(self):
        if self.playing != True:
            return
        # TODO:

    def OnClick_ChessRepent(self):
        if self.playing != True:
            QMessageBox.critical(self.qb, '错误', '还未开始游戏', QMessageBox.Ok, QMessageBox.Ok)
            return
        if not self.board.Repent():
            QMessageBox.critical(self.qb, '错误', '无法再悔棋', QMessageBox.Ok, QMessageBox.Ok)

if __name__ == "__main__":
    UI('AI')