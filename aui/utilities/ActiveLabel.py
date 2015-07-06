__author__ = 'Argen'

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QSizePolicy, QLabel, QVBoxLayout, QFrame,
                         QApplication, QGroupBox, QFont, QGridLayout,
                         QWidget)
from PyQt4.QtCore import (pyqtSignal, QObject, QString, QTimer, Qt)
import sys


class ActLabel (QLabel, QObject):
    inside = pyqtSignal(str, name= 'inside')
    def __init__(self, parent):
        QLabel.__init__(self, parent)
        self.outside = pyqtSignal(str)
        self.default_style = self.styleSheet()


    def enterEvent(self, QEvent):
        self.setStyleSheet('border: 2px solid rgb(0, 0, 0);'+self.default_style)
        self.inside.emit(self.text())

    def leaveEvent(self, QEvent):
        self.setStyleSheet(self.default_style)
        pass


