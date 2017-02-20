#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QVBoxLayout,
                             QLineEdit)

class StatusWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.lbl_status = QLabel("Running", self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl_status)
        vbox.addStretch()

        self.setLayout(vbox)
        self.setGeometry(100, 100, 800, 480)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    scan_window = StatusWindow()
    sys.exit(app.exec_())
