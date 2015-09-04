#!/usr/bin/env python
#  -*- coding: utf-8 -*-
"""
Local Map Widget
"""

__author__ = "Argentina Ortega Sainz"
__copyright__ = "Copyright (C) 2015 Argentina Ortega Sainz"
__license__ = "MIT"
__version__ = "2.0"

import sys

from PyQt4.QtCore import pyqtSignal, Qt, QMimeData
from PyQt4.QtGui import (QWidget, QSizePolicy, QApplication, QDrag, QPixmap)

from aui.gui.views.sources import ui_lmap

class LocalMap(QWidget, ui_lmap.Ui_NewView):
    '''
    Simulation of an additional view widget
    '''
    inside = pyqtSignal(str)

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setObjectName("LM")
        self.currentmap = 'border-image: url(:/maps/local/local1);'
        #self.map.setStyleSheet(self.currentmap)


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
        mime_data.setText(self.map.text())
        #mime_data.setImageData(self.currentmap)
        drag.setMimeData(mime_data)

        self.drop_action = drag.exec_(Qt.CopyAction | Qt.MoveAction)


def main():
    app = QApplication(sys.argv)
    main = LocalMap(None)
    main.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
