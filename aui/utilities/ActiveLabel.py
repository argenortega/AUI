__author__ = 'Argen'

from PyQt4.QtGui import (QLabel)
from PyQt4.QtCore import (pyqtSignal, QObject)


class ActLabel (QLabel, QObject):
    inside = pyqtSignal(str, str, name= 'inside')

    def __init__(self, parent):
        QLabel.__init__(self, parent)
        self.outside = pyqtSignal(str)
        self.default_style = self.styleSheet()

    def enterEvent(self, QEvent):
        self.setStyleSheet('border: 2px solid rgb(0, 0, 0);'+self.default_style)
        self.inside.emit('Focus', str(self.accessibleName()))

    def leaveEvent(self, QEvent):
        self.setStyleSheet(self.default_style)
        pass


