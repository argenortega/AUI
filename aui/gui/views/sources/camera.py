#!/usr/bin/env python
#  -*- coding: utf-8 -*-
"""
Camera widgets
"""

__author__ = "Argentina Ortega Sainz"
__copyright__ = "Copyright (C) 2015 Argentina Ortega Sainz"
__license__ = "MIT"
__version__ = "2.0"

import sys

from PyQt4 import QtGui
from PyQt4.QtCore import QSettings, QVariant, QMimeData, Qt, QSize
from PyQt4.QtGui import (QWidget, QSizePolicy, QApplication, QDrag, QPixmap)

from aui.gui.views.sources import ui_camera


class Camera(QWidget, ui_camera.Ui_Camera):
    """
    Simulation of a camera widget
    """
    def __init__(self, parent, num):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.num = num
        self.initui()

    def initui(self):
        self.setObjectName("C%d" % self.num)
        self.setAccessibleName("C%d" % self.num)

        self.cam.setAccessibleName("C%d" % self.num)

        if self.num == 1:
            self.cam.setText("Front Camera")
        elif self.num == 2:
            self.cam.setText("Back Camera")
        else:
            self.cam.setText("Bird's Eye Camera")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons() and Qt.LeftButton):
            return

        if ((event.pos() - self.drag_start_position).manhattanLength()
            < QApplication.startDragDistance()):
            return

        drag = QDrag(self)
        pix = QPixmap.grabWidget(self)
        drag.setPixmap(pix)
        mime_data = QMimeData()
        mime_data.setText(self.cam.text())
        # mime_data.setImageData(self.currentmap)
        drag.setMimeData(mime_data)

        self.drop_action = drag.exec_(Qt.CopyAction | Qt.MoveAction)


def main():
    app = QtGui.QApplication(sys.argv)
    cam = Camera(None, 1)
    cam.show()
    sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    sizePolicy.setHeightForWidth(True)
    sizePolicy.setHorizontalStretch(10)
    sizePolicy.setVerticalStretch(10)
    cam.cam.setSizePolicy(sizePolicy)
    cam.cam.resize(700, 700)
    cam.cam.updateGeometry()


    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()