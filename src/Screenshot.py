__author__ = 'Argen'

from PyQt4 import QtGui
from PyQt4.QtGui import (QWidget, QSizePolicy, QDragEnterEvent, QDropEvent)
import sys
import ScreenshotUI


class Screenshot(QWidget, ScreenshotUI.Ui_ScreenshotWidget):
    def __init__(self, parent, num):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.num = num
        self.initui()

    def initui(self):
        self.setObjectName("Screenshot%d" % self.num)
        self.screenshot.setText("Screenshot %d" % self.num)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)

