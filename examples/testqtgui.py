#!/user/bin/env python3
# -*- coding: utf-8 -*-

import sys
from time import sleep
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QVBoxLayout


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        lbl_counter = QLabel(str(0), self)
        self.setGeometry(300, 300, 300, 220)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())

