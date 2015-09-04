#!/usr/bin/env python
#  -*- coding: utf-8 -*-
"""
Point Cloud Widget
"""

__author__ = "Argentina Ortega Sainz"
__copyright__ = "Copyright (C) 2015 Argentina Ortega Sainz"
__license__ = "MIT"
__version__ = "2.0"

import sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QMimeData, Qt
from PyQt4.QtGui import (QWidget, QSizePolicy, QDrag, QPixmap, QApplication)

from aui.gui.views.sources import ui_pointcloud


class Pointcloud(QWidget, ui_pointcloud.Ui_PointcloudWidget):
    '''
    Simulation of a 3d pointcloud widget
    '''
    def __init__(self,parent):
        QWidget.__init__(self,parent)
        self.setupUi(self)
        self.initUI()
        
    def initUI(self):
        self.setObjectName("PC")

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
        mime_data.setText(self.pointcloud.text())
        # mime_data.setImageData(self.currentmap)
        drag.setMimeData(mime_data)

        self.drop_action = drag.exec_(Qt.CopyAction | Qt.MoveAction)



def main():
    app = QtGui.QApplication(sys.argv)
    minSize = QtCore.QSize(100, 100)
    maxSize = QtCore.QSize(300, 300)
    stretch = 3
    main = Pointcloud(None,minSize,maxSize,stretch)
    
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()