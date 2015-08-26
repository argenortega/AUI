__author__ = 'Argen'

from PyQt4.QtGui import (QLabel)
from PyQt4.QtCore import (pyqtSignal, QObject, QTimer)


class ActLabel(QLabel, QObject):
    inside = pyqtSignal(str, str, name='inside')

    def __init__(self, parent):
        QLabel.__init__(self, parent)
        self.outside = pyqtSignal(str)
        #self.default_style = self.styleSheet()
        self.default_style = 'border-color: rgb(154, 154, 154); border-style: solid; border-width: 2px; border-radius: 6px;'
        self.setStyleSheet(self.default_style)

    def enterEvent(self, QEvent):
        self.setStyleSheet(
            'border-color: rgb(164, 205, 255); border-radius: 6px; border-width: 3px; border-style: solid;')  # + self.default_style)
        QTimer.singleShot(5000,self.focusing)

    def leaveEvent(self, QEvent):
        self.setStyleSheet(self.default_style)

    def focusing(self):
        if self.underMouse():
            #print 'Focus ', self.accessibleName()
            self.inside.emit('focus', str(self.accessibleName()))

