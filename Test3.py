import sys
from PyQt5.QtWidgets import (QApplication)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import (QPainter, QPen, QBrush)
from PyQt5.QtWidgets import (QWidget, QPushButton, QSlider, QVBoxLayout, QApplication, QWidget, QPushButton, QMessageBox, QLabel)
from PyQt5.QtWidgets import (QDialog, QLineEdit, QSpinBox, QComboBox, QDialogButtonBox, QFormLayout, QVBoxLayout)



class Ui_Frame1(QWidget):
    signal = pyqtSignal(str)

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("窗口1")
        self.resize(300, 100)

        self.editBox = QLineEdit(self)

        btn_to2 = QPushButton(self)
        btn_to2.setText("到窗口2")
        btn_to2.setMaximumSize(100000, 100000)

        layout = QVBoxLayout(self)
        layout.addWidget(self.editBox)
        layout.addWidget(btn_to2)
        self.setLayout(layout)

        btn_to2.clicked.connect(self.OnClick_To2)

    def OnClick_Enter(self, s):
        QMessageBox.about(self, '信息', s)

    def OnClick_To2(self):
        words = self.editBox.text()
        if words is not '':
            self.hide();
            self.next.show()
            self.signal.emit(words)
        else:
            QMessageBox.warning(self, '提示', '请输入内容!')

class Ui_Frame2(QWidget):
    signal = pyqtSignal(str)

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("窗口2")
        self.resize(300, 100)

        self.editBox = QLineEdit(self)

        btn_to1 = QPushButton("到窗口1", self)
        btn_to1.setMaximumSize(100000, 100000)
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.editBox)
        layout.addWidget(btn_to1)
        self.setLayout(layout)

        btn_to1.clicked.connect(self.OnClick_To1)

    def OnClick_Enter(self, s):
        QMessageBox.about(self, '信息', s)

    def OnClick_To1(self):
        words = self.editBox.text()
        if words is not '':
            self.hide();
            self.next.show()
            self.signal.emit(words)
        else:
            QMessageBox.warning(self, '提示', '请输入内容!')

class UI:
    def __init__(self):
        app = QApplication(sys.argv)

        f1 = Ui_Frame1()
        f2 = Ui_Frame2()
        f1.next = f2
        f2.next = f1
        f1.signal.connect(f2.OnClick_Enter)
        f2.signal.connect(f1.OnClick_Enter)
        f1.show()

        sys.exit(app.exec_())


if __name__ == "__main__":
    UI()