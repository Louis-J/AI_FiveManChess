import sys
from .Frame import Frame
from PyQt5.QtWidgets import (QApplication)


class UI:
    def __init__(self, AI):
        app = QApplication(sys.argv)

        self.frame = Frame(AI)
        self.frame.show()

        sys.exit(app.exec_())


if __name__ == "__main__":
    UI('AI')