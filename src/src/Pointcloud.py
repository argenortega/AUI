# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 15:28:42 2014

@author: Argen
"""

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QSizePolicy, QLabel, QVBoxLayout, QFrame)
import sys

class Pointcloud(QtGui.QWidget):
    '''
    Simulation of a 3d pointcloud widget
    '''
    def __init__(self,parent,minSize,maxSize,stretch):
        QtGui.QWidget.__init__(self,parent)
        self.minSize = minSize
        self.maxSize = maxSize
        self.stretch = stretch
        self.initUI()
        
    def initUI(self):
        self.setObjectName("Pointcloud")
        self.layout = QVBoxLayout()
        self.layout.setMargin(0)
        self.setLayout(self.layout)
        
        self.pointcloud = QLabel("3D pointcloud",self)  
        self.pointcloud.setAlignment(QtCore.Qt.AlignCenter)
        self.pointcloud.setFrameStyle(QFrame.Sunken | QFrame.StyledPanel)
        self.pointcloud.setWordWrap(True)
        self.pointcloud.setScaledContents(True)
        #pointcloud.sizeHint(300,300)        
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pointcloud.setFont(font)
        #self.pointcloud.setObjectName("pointcloud1Label")
        self.layout.addWidget(self.pointcloud)
        
        '''
        Size of the widget
        '''
        #self.setMinimumSize(300,300)
        #self.resize(300,300)        
        self.setMinimumSize(self.minSize)
        self.setMaximumSize(self.maxSize)        
        self.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.setMouseTracking(True)

        
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(self.stretch)
        sizePolicy.setVerticalStretch(self.stretch)
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