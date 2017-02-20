from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QVBoxLayout,
                             QLineEdit)


class ScanWorkorderWindow(QWidget):
    # First window
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

        font_scanbox = QtGui.QFont('SanSerif', 10)
        font_scanbox_color = QtGui.QPalette()

        # Setup Title
        lbl_title = QLabel("Loader Controller  -  Press " + press_id, self)
        lbl_title.setFont(font_large)
        lbl_title.setPalette(font_large_color)
        lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        lbl_title.setStyleSheet("QLabel {background-color: blue;}")

        # Setup Work Order Scan box
        lbl_scan_wo = QLabel("Scan Work Order:", self)
        lbl_scan_wo.setFont(font)
        lbl_scan_wo.setPalette(font_color)
        lbl_scan_wo.setAlignment(QtCore.Qt.AlignCenter)

        txt_scan_wo = QLineEdit()
        # txt_scan_wo.setFixedWidth(100)
        txt_scan_wo.setFont(font_scanbox)
        txt_scan_wo.setPalette(font_scanbox_color)
        txt_scan_wo.setAlignment(QtCore.Qt.AlignCenter)
        txt_scan_wo.setStyleSheet("QLineEdit {background-color: black;\
                                              border: 0px}")

        # Setup Layout
        vbox = QVBoxLayout()
        vbox.addWidget(lbl_title)
        vbox.addStretch()
        vbox.addWidget(lbl_scan_wo)
        vbox.addWidget(txt_scan_wo)
        vbox.addStretch()
        vbox.addStretch()

        # Setup GUI
        self.setLayout(vbox)
        self.setPalette(app_color)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.showMaximized()
