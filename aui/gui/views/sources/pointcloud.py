# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 15:28:42 2014

@author: Argen
"""

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
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)


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