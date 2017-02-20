#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QVBoxLayout,
                             QLineEdit)

# from iqapi import get_wo_id_from_press_api
import iqapi as api


# Variables
PRESS_ID = "113"

# wo_id = "10292565"
# itemno = "1012324546"
# desc = "RANDOM THINGY COVER"
# rm_itemno = "PK-458645-BLACK"


class ScanWorkorderWindow(QWidget):
    # First window
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set Application Background color
        app_color = QtGui.QPalette()
        app_color.setColor(QtGui.QPalette.Background, QtCore.Qt.black)

        # Set Fonts
        self.font_large = QtGui.QFont('SanSerif', 36, QtGui.QFont.Bold)
        self.font_large_color = QtGui.QPalette()
        self.font_large_color.setColor(QtGui.QPalette.Foreground,
                                       QtCore.Qt.white)
        self.font = QtGui.QFont('SanSerif', 28, QtGui.QFont.Bold)
        self.font_color = QtGui.QPalette()
        self.font_color.setColor(QtGui.QPalette.Foreground,
                                 QtCore.Qt.white)
        self.font_scanbox = QtGui.QFont('SanSerif', 10)
        self.font_scanbox_color = QtGui.QPalette()

        # Setup Title
        self.lbl_title = QLabel("Loader Controller  -  Press " +
                                PRESS_ID, self)
        self.lbl_title.setFont(self.font_large)
        self.lbl_title.setPalette(self.font_large_color)
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setStyleSheet("QLabel {background-color: blue;}")

        # Setup Work Order Scan box
        self.lbl_scan_wo = QLabel("Scan Work Order:", self)
        self.lbl_scan_wo.setFont(self.font)
        self.lbl_scan_wo.setPalette(self.font_color)
        self.lbl_scan_wo.setAlignment(QtCore.Qt.AlignCenter)

        self.txt_scan_wo = QLineEdit()
        self.txt_scan_wo.setFont(self.font_scanbox)
        self.txt_scan_wo.setPalette(self.font_scanbox_color)
        self.txt_scan_wo.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_scan_wo.setStyleSheet("QLineEdit {background-color: black;\
                                                   border: 0px}")

        # Handlers
        self.txt_scan_wo.returnPressed.connect(self.check_wo_id_against_api)

        # Setup Layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl_title)
        vbox.addStretch()
        vbox.addWidget(self.lbl_scan_wo)
        vbox.addWidget(self.txt_scan_wo)
        vbox.addStretch()
        vbox.addStretch()

        # Setup GUI
        self.setLayout(vbox)
        self.setPalette(app_color)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.showMaximized()

    def get_press_api_request(self, PRESS_ID):
        press_id, wo_id, itemno, descrip, itemno_mat,descrip_mat = api.press_api_request(PRESS_ID)
        return press_id, wo_id, itemno_mat

    def check_wo_id_against_api(self):
        wo_id_from_scan = self.txt_scan_wo.text()
        press_id_api, wo_id_api, itemno_mat_api = self.get_press_api_request(PRESS_ID)
        print(press_id_api)
        # Verify Press ID
        if not press_id_api == PRESS_ID:
            # If the Press IDs do not match, 'reset' the Window
            print("Press IDs do not match")
            self.txt_scan_wo.clear()
            return
        # Verify Work order
        if not wo_id_from_scan == wo_id_api:
            # If work orders do not match, 'reset' the Window
            print("Incorrect work order")
            self.txt_scan_wo.clear()
            return
        # If the Press ID and Work order match, return the RM Item number
        print("Press ID and Work order match")
        return itemno_mat_api


class ScanSerialWindow(QWidget):
    # Second window
    def __init__(self, itemno_mat_from_api):
        super().__init__()
        self.initUI()

    def initUI(self):
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

        font_scanbox = QtGui.QFont('SanSerif', 10)
        font_scanbox_color = QtGui.QPalette()

        # Setup Title
        lbl_title = QLabel("Loader Controller  -  Press " + PRESS_ID, self)
        lbl_title.setFont(font_large)
        lbl_title.setPalette(font_large_color)
        lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        lbl_title.setStyleSheet("QLabel {background-color: blue;}")

        # Setup Serial Number Scan box
        lbl_scan_serial = QLabel("Scan Raw Material Serial Number:", self)
        lbl_scan_serial.setFont(font)
        lbl_scan_serial.setPalette(font_color)
        lbl_scan_serial.setAlignment(QtCore.Qt.AlignCenter)

        txt_scan_serial = QLineEdit()
        txt_scan_serial.setFont(font_scanbox)
        txt_scan_serial.setPalette(font_scanbox_color)
        txt_scan_serial.setAlignment(QtCore.Qt.AlignCenter)
        txt_scan_serial.setStyleSheet("QLineEdit {background-color: black;\
                                              border: 0px}")

        # Setup Layout
        vbox = QVBoxLayout()
        vbox.addWidget(lbl_title)
        vbox.addStretch()
        vbox.addWidget(lbl_scan_serial)
        vbox.addWidget(txt_scan_serial)
        vbox.addStretch()
        vbox.addStretch()

        # Setup GUI
        self.setLayout(vbox)
        self.setPalette(app_color)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.showMaximized()


class RunWindow(QWidget):
    # Qt GUI class
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
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

        # Setup Text Labels
        lbl_title = QLabel("Loader Controller  -  Press " + PRESS_ID, self)
        lbl_title.setFont(font_large)
        lbl_title.setPalette(font_large_color)
        lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        lbl_title.setStyleSheet("QLabel {background-color: blue;}")

        lbl_itemno = QLabel(itemno + "\n" + desc, self)
        lbl_itemno.setFont(font)
        lbl_itemno.setPalette(font_color)
        lbl_itemno.setAlignment(QtCore.Qt.AlignCenter)

        lbl_wo = QLabel("Work Order:\n " + wo_id, self)
        lbl_wo.setFont(font)
        lbl_wo.setPalette(font_color)
        lbl_wo.setAlignment(QtCore.Qt.AlignCenter)
        lbl_wo.setStyleSheet("QLabel {background-color: green;}")

        lbl_rm_itemno = QLabel("Raw Material Item Number:\n" + rm_itemno, self)
        lbl_rm_itemno.setFont(font)
        lbl_rm_itemno.setPalette(font_color)
        lbl_rm_itemno.setAlignment(QtCore.Qt.AlignCenter)
        lbl_rm_itemno.setStyleSheet("QLabel {background-color: green;}")

        # Setup Layout
        vbox = QVBoxLayout()
        vbox.addWidget(lbl_title)
        vbox.addStretch()
        vbox.addWidget(lbl_wo)
        vbox.addStretch()
        vbox.addWidget(lbl_itemno)
        vbox.addStretch()
        vbox.addWidget(lbl_rm_itemno)

        # Setup GUI
        self.setLayout(vbox)
        self.setPalette(app_color)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.showMaximized()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    scan_wo_window = ScanWorkorderWindow()
    # scan_serial_window = ScanSerialWindow()
    # run_window = RunWindow()
    sys.exit(app.exec_())
