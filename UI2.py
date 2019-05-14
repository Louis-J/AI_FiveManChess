import json
import os
import sys
from enum import Enum, IntEnum, unique
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication, QWidget, QApplication, QPushButton, QMessageBox, QLabel)
# from Frame import frame

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

@unique
class MAN(Enum):
    N = 0
    B = 1
    R = 2

class Setting:
    def SettingSave(self):
        try:
            with open('setting.json', 'w', encoding = 'utf8') as file:
                setting = dict()
                # setting['V'] = self.V
                # setting['H'] = self.H
                setting['Difficult'] = self.Difficult
                setting['WhoFirst'] = self.WhoFirst
                json.dump(setting, file)
        except Exception as identifier:
            self.paintStatusBar(identifier)
        
    def SettingLoad(self):
        settingDefault = {'V' : 16, 'H' : 16, 'Difficult' : 3, 'WhoFirst' : 'random'}
        settingMinMax  = {'V' : [5, 50], 'H' : [5, 50], 'Difficult' : [1, 5], 'WhoFirst' : ['player', 'AI', 'random']}
        try:
            with open('setting.json', 'r', encoding = 'utf8') as file:
                setting = json.loads(file.read())
                # if 'V' not in setting or type(setting['V']) != int or setting['V'] < settingMinMax['V'][0] or setting['V'] > settingMinMax['V'][1]:
                #     self.V = settingDefault['V']
                # else:
                #     self.V = setting['V']
                # if 'H' not in setting or type(setting['H']) != int or setting['H'] < settingMinMax['H'][0] or setting['H'] > settingMinMax['H'][1]:
                #     self.H = settingDefault['H']
                # else:
                #     self.H = setting['H']
                if 'Difficult' not in setting or type(setting['Difficult']) != type(settingDefault['Difficult']) or setting['Difficult'] < settingMinMax['Difficult'][0] or setting['Difficult'] > settingMinMax['Difficult'][1]:
                    self.Difficult = settingDefault['Difficult']
                else:
                    self.Difficult = setting['Difficult']
                if 'WhoFirst' not in setting or type(setting['WhoFirst']) != type(settingDefault['WhoFirst']) or setting['WhoFirst'] not in settingMinMax['WhoFirst']:
                    self.WhoFirst = settingDefault['WhoFirst']
                else:
                    self.WhoFirst = setting['WhoFirst']
        except Exception as identifier:
            # self.V = settingDefault['V']
            # self.H = settingDefault['H']
            self.Difficult = settingDefault['Difficult']
            self.WhoFirst = settingDefault['WhoFirst']
            self.paintStatusBar(identifier)
        
    def SettingDialog(self):
        from PyQt5.QtWidgets import (QDialog, QSpinBox, QComboBox, QDialogButtonBox, QFormLayout)
        dialog = QDialog(self.qb)
        boxDifficult = QSpinBox(dialog)
        boxDifficult.setRange(1, 5)
        boxDifficult.setValue(self.Difficult)

        boxWhoFirst = QComboBox(dialog)
        boxWhoFirst.addItems(['player', 'AI', 'random'])
        boxWhoFirst.setCurrentIndex(boxWhoFirst.findText(self.WhoFirst))

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, dialog);

        form = QFormLayout(dialog)
        form.addRow(QLabel("设置:"))
        form.addRow("难度(1-5):", boxDifficult)
        form.addRow("先手:", boxWhoFirst)
        form.addRow(buttonBox)

        buttonBox.accepted.connect(dialog.accept)
        buttonBox.rejected.connect(dialog.reject)
        if dialog.exec() == QDialog.Accepted:
            self.Difficult = boxDifficult.value()
            self.WhoFirst = boxWhoFirst.currentText()

class UI(Setting):
    playing = False
    V = 16
    H = 16
    def __init__(self, AI):
        self.AI = AI
        self.SettingLoad()
        self.board = [MAN.N] * (self.V * self.H)
        self.step = []
        
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

    def __del__(self):
        self.SettingSave()

    def Paint(self):
        pass

    def PaintStatusBar(self, info):
        print('StatusBar:')
        print(info)
        pass

    def OnClick_NewGame(self):
        if self.playing == True:
            reply = QMessageBox.question(self.qb, '询问', '正在对局中，是否重新开始游戏？', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
            if reply != QMessageBox.Yes:
                return
        self.playing = True
        # TODO:init & paint


    def OnClick_Setting(self):
        if self.playing == True:
            QMessageBox.critical(self.qb, '错误', '请结束游戏后重新设置', QMessageBox.Yes, QMessageBox.Yes)
            return
        self.SettingDialog()

    def OnClick_Ending(self):
        self.playing = False
        # TODO:init & paint

    def OnClick_About(self):
        QMessageBox.about(self.qb, '关于', '作者：zcy/dcy<br><a href="http://github.com">homepage</a>')

    def OnClick_AboutQt(self):
        QMessageBox.aboutQt(self.qb, '关于Qt')

    def OnClick_LastStep(self):
        pass

    def OnClick_Chess(self):
        pass
        
    def ChessSave(self):
        pass
        
    def ChessLoad(self):
        pass

if __name__ == "__main__":
    UI('AI')