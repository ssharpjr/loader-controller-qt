#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication,
                             QGridLayout, QFormLayout, QHBoxLayout,
                             QVBoxLayout)


class Example(QWidget):


    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        PRESS_ID = "113"
        wo_id = "9001234"
        itemno = "1012324546"
        desc = "RANDOM THINGY COVER"
        rm_itemno = "PK-458645-BLACK"

        # Set Application Background color
        app_color = QtGui.QPalette()
        app_color.setColor(QtGui.QPalette.Background, QtCore.Qt.black)

        # Set Font
        font_large = QtGui.QFont('SanSerif', 36, QtGui.QFont.Bold)
        font_large_color = QtGui.QPalette()
        font_large_color.setColor(QtGui.QPalette.Foreground, QtCore.Qt.white)

        font = QtGui.QFont('SanSerif', 28, QtGui.QFont.Bold)
        font_color = QtGui.QPalette()
        font_color.setColor(QtGui.QPalette.Foreground, QtCore.Qt.white)

        lbl_title = QLabel("Loader Controller  -  Press " + PRESS_ID, self)
        lbl_title.setFont(font_large)
        lbl_title.setPalette(font_large_color)
        lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        lbl_title.setStyleSheet("QLabel {background-color: blue;}")

        lbl_wo = QLabel("Work Order:" + wo_id, self)
        lbl_wo.setFont(font)
        lbl_wo.setPalette(font_color)
        lbl_wo.setAlignment(QtCore.Qt.AlignCenter)

        lbl_itemno = QLabel(itemno + "\n" + desc, self)
        lbl_itemno.setFont(font)
        lbl_itemno.setPalette(font_color)
        lbl_itemno.setAlignment(QtCore.Qt.AlignCenter)

        lbl_rm_itemno = QLabel("Raw Material Item Number:\n" + rm_itemno, self)
        lbl_rm_itemno.setFont(font)
        lbl_rm_itemno.setPalette(font_color)
        lbl_rm_itemno.setAlignment(QtCore.Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_title)
        vbox.addStretch()
        vbox.addWidget(lbl_wo)
        vbox.addStretch()
        vbox.addWidget(lbl_itemno)
        vbox.addStretch()
        vbox.addWidget(lbl_rm_itemno)

        # grid = QGridLayout()
        # grid.setSpacing(10)
        # grid.setColumnStretch(0, 1)
        # grid.setColumnStretch(4, 1)
        # grid.setRowStretch(0, 1)
        # grid.setRowStretch(4, 1)

        # grid.addWidget(lbl_title, 1, 1)
        # grid.addWidget(lbl_press, 2, 1)
        # grid.addWidget(lbl_wo, 3, 1)

        # self.setLayout(grid)

        # fbox = QFormLayout()
        # fbox.addRow(lbl_title)
        # fbox.addRow(lbl0)
        # fbox.addRow(lbl_press)
        # fbox.addRow(lbl_wo)

        self.setLayout(vbox)
        self.setPalette(app_color)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.showMaximized()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
