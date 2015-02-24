# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 15:28:54 2014

@author: Argen
"""

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QSizePolicy, QLabel, QVBoxLayout, QFrame)
import sys

class NewView(QtGui.QWidget):
    '''
    Simulation of an additional view widget
    '''
    def __init__(self,parent,minSize,maxSize,stretch):
        QtGui.QWidget.__init__(self,parent)
        self.minSize = minSize
        self.maxSize = maxSize
        self.stretch = stretch
        self.initUI()
        
    def initUI(self):
        self.setObjectName("NewView")
        self.layout = QVBoxLayout()
        self.layout.setMargin(0)
        #self.layout.setObjectName("view%dLayout"%self.num)
        self.setLayout(self.layout)
        
        self.view = QLabel("Additional View",self)  
        self.view.setAlignment(QtCore.Qt.AlignCenter)
        self.view.setFrameStyle(QFrame.Sunken | QFrame.StyledPanel)
        self.view.setWordWrap(True)
        self.view.setScaledContents(True)
        #view.sizeHint(300,300)        
        font = QtGui.QFont()
        font.setPointSize(14)
        self.view.setFont(font)
        #self.view.setObjectName("view1Label")
        self.layout.addWidget(self.view)
        
        '''
        Size of the widget
        '''
        #self.setMinimumSize(300,300)
        #self.resize(300,300)        
        self.setMinimumSize(self.minSize)
        self.setMaximumSize(self.maxSize)        
        self.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.setMouseTracking(True)

        
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(self.stretch)
        sizePolicy.setVerticalStretch(self.stretch)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)        
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    minSize = QtCore.QSize(100, 100)
    maxSize = QtCore.QSize(300, 300)
    stretch = 3
    main = NewView(None,minSize,maxSize,stretch)
    
    
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()