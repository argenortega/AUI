__author__ = 'Argen'

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QPushButton, QSizePolicy, QLabel, QVBoxLayout, QFrame,
                         QApplication, QGroupBox, QFont, QGridLayout,
                         QWidget)
from PyQt4.QtCore import (QEvent, QString, QTimer, Qt)
import sys


class HButton (QPushButton):
    def __init__(self, parent):
        QPushButton.__init__(self, parent)


    def enterEvent(self, QEvent):
        self.setStyleSheet('border: 2px solid rgb(0, 128, 255);')

    def leaveEvent(self, QEvent):
        self.setStyleSheet('color: black')