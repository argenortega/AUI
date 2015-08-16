from PyQt4.QtCore import pyqtSignal

__author__ = 'Argen'

from PyQt4.QtGui import (QWidget, QSizePolicy)
from aui.gui.snapshots import ui_image


class Screenshot(QWidget, ui_image.Ui_ScreenshotWidget):
    chosen = pyqtSignal(str)

    def __init__(self, parent, num):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.num = num
        self.initui()

    def initui(self):
        self.setObjectName("Snapshot%d" % self.num)
        self.screenshot.setText("Snapshot %d" % self.num)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)

    def mousePressEvent(self, QMouseEvent):
        self.chosen.emit(self.screenshot.text())

