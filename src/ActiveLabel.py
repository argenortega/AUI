__author__ = 'Argen'

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QWidget, QSizePolicy, QLabel, QVBoxLayout, QFrame,
                         QApplication, QGroupBox, QFont, QGridLayout,
                         QWidget)
from PyQt4.QtCore import (QEvent, QString, QTimer, Qt)
import sys


class ActLabel (QLabel):
    def __init__(self, parent):
        QLabel.__init__(self, parent)
        pass

    def enterEvent(self, QEvent):
        self.setStyleSheet('border: 2px solid rgb(0, 128, 255);; color: rgb(0, 128, 255);')

    def leaveEvent(self, QEvent):
        self.setStyleSheet('color: black')

