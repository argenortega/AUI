#!/usr/bin/env python
#  -*- coding: utf-8 -*-
"""
Global Map Widget
"""

__author__ = "Argentina Ortega Sainz"
__copyright__ = "Copyright (C) 2015 Argentina Ortega Sainz"
__license__ = "MIT"
__version__ = "2.0"

import sys

from PyQt4.QtCore import Qt, QMimeData
from PyQt4.QtGui import (QWidget, QSizePolicy, QApplication, QDrag, QPixmap)

from aui.gui.views.sources import ui_gmap


class GlobalMap(QWidget, ui_gmap.Ui_MapWidget):
    def __init__(self,parent):
        QWidget.__init__(self,parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setObjectName("GM")
        self.currentmap = 'border-image: url(:/maps/global/global2);'
        #self.map.setStyleSheet(self.currentmap)

    def heightForWidth(self, p_int):
        return p_int

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
    main = GlobalMap(None)
    
    
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()