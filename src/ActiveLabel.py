__author__ = 'Argen'

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QSizePolicy, QLabel, QVBoxLayout, QFrame,
                         QApplication, QGroupBox, QFont, QGridLayout,
                         QWidget)
from PyQt4.QtCore import (pyqtSignal, QObject, QString, QTimer, Qt)
import sys


class ActLabel (QLabel, QObject):
    inside = pyqtSignal(str)
    def __init__(self, parent):
        QLabel.__init__(self, parent)
        self.outside = pyqtSignal(str)
        self.txt = self.text()

    def enterEvent(self, QEvent):
        self.setStyleSheet('border: 2px solid rgb(0, 128, 255);; color: rgb(0, 128, 255);')
        self.inside.emit(self.txt)

    def leaveEvent(self, QEvent):
        self.setStyleSheet('color: black')


