import sys
from PyQt5.QtWidgets import (QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QPainter, QPen, QBrush)
from PyQt5.QtWidgets import (QWidget, QPushButton, QSlider, QVBoxLayout, QApplication, QWidget, QPushButton, QMessageBox, QLabel)
from PyQt5.QtWidgets import (QDialog, QSpinBox, QComboBox, QDialogButtonBox, QFormLayout, QVBoxLayout)



class Ui_Frame1(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("窗口1")
        self.resize(300, 200)

        btn_to2 = QPushButton(self)
        btn_to2.setText("到窗口2")
        btn_to2.setMaximumSize(100000, 100000)

        btn_about = QPushButton(self)
        btn_about.setText("关于")
        btn_about.setMaximumSize(100000, 100000)

        layout = QVBoxLayout(self)
        layout.addWidget(btn_to2)
        layout.addWidget(btn_about)
        self.setLayout(layout)

        btn_to2.clicked.connect(self.OnClick_To2)
        btn_about.clicked.connect(self.OnClick_About)

    def OnClick_About(self):
        QMessageBox.about(self, '关于', '窗口1')

    def OnClick_To2(self):
        self.hide();
        self.next.show()

class Ui_Frame2(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("窗口2")
        self.resize(300, 200)

        btn_to1 = QPushButton(self)
        btn_to1.setText("到窗口1")
        btn_to1.setMaximumSize(100000, 100000)

        btn_about = QPushButton(self)
        btn_about.setText("关于")
        btn_about.setMaximumSize(100000, 100000)

        layout = QVBoxLayout(self)
        layout.addWidget(btn_to1)
        layout.addWidget(btn_about)
        self.setLayout(layout)

        btn_to1.clicked.connect(self.OnClick_To1)
        btn_about.clicked.connect(self.OnClick_About)

    def OnClick_About(self):
        QMessageBox.about(self, '关于', '窗口2')

    def OnClick_To1(self):
        self.hide();
        self.next.show()

class UI:
    def __init__(self):
        app = QApplication(sys.argv)

        f1 = Ui_Frame1()
        f2 = Ui_Frame2()
        f1.next = f2
        f2.next = f1
        f1.show()

        sys.exit(app.exec_())


if __name__ == "__main__":
    UI()