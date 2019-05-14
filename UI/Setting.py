import json
import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication, QWidget, QApplication, QPushButton, QMessageBox, QLabel)

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
            self.PaintStatusBar(identifier)
        
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
            self.PaintStatusBar(identifier)
        
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
