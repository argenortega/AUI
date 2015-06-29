from PyQt4.QtCore import pyqtSignal

__author__ = 'Argen'

from PyQt4.QtGui import (QWidget, QSizePolicy)
from aui.gui.snapshots import ui_snapshot


class Screenshot(QWidget, ui_snapshot.Ui_ScreenshotWidget):
    chosen = pyqtSignal(str)
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

    def mousePressEvent(self, QMouseEvent):
        self.chosen.emit(self.screenshot.text())

