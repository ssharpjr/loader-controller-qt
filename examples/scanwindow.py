#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QVBoxLayout,
                             QLineEdit)

from statuswindow import StatusWindow


class ScanWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.lbl_wo = QLabel("Scan the Work Order", self)
        self.txt_scan_wo = QLineEdit()
        self.lbl_output = QLabel("", self)

        self.txt_scan_wo.returnPressed.connect(self.update_output)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl_wo)
        vbox.addWidget(self.txt_scan_wo)
        vbox.addWidget(self.lbl_output)
        vbox.addStretch()

        self.setLayout(vbox)
        self.setGeometry(100, 100, 800, 480)
        self.show()

    def update_output(self):
        # self.lbl_output.setText(self.txt_scan_wo.text())
        if self.txt_scan_wo.text() == "run":
            self.statuswindow = StatusWindow()
            self.hide()
            self.statuswindow.show()
        else:
            self.lbl_output.setText(self.txt_scan_wo.text())
            print(self.txt_scan_wo.text())


def main():
    app = QApplication(sys.argv)
    scan_window = ScanWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

