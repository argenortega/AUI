# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 15:28:25 2014

@author: Argen
"""

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QWidget, QSizePolicy, QLabel, QVBoxLayout, QFrame)
import sys
import MapUI

class Map(QWidget, MapUI.Ui_MapWidget):
    '''
    Simulation of an additional view widget
    '''
    def __init__(self,parent):
        QtGui.QWidget.__init__(self,parent)
        self.setupUi(self)
        #self.minSize = minSize
        #self.maxSize = maxSize
        #self.stretch = stretch
        self.initUI()
        
    def initUI(self):
        '''
        self.setObjectName("Map")
        self.layout = QVBoxLayout()
        self.layout.setMargin(0)
        #self.layout.setObjectName("view%dLayout"%self.num)
        self.setLayout(self.layout)
        
        self.map = QLabel(self)  
        self.map.setAlignment(QtCore.Qt.AlignCenter)
        self.map.setFrameStyle(QFrame.Sunken | QFrame.StyledPanel)
        #map.sizeHint(300,300)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.map.setFont(font)
        self.map.setScaledContents(True)
        #self.map.setObjectName("map1Label")
        self.layout.addWidget(self.map)
        '''
        '''
        Size of the widget
        '''
        #self.setMinimumSize(300,300)
        #self.resize(300,300)
        #self.map.clear()
        #self.map.setPixmap(QtGui.QPixmap(':/maps/02.png'))
        #self.setMinimumSize(self.minSize)
        #self.setMaximumSize(self.maxSize)
        #self.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        #self.setMouseTracking(True)

        
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        #sizePolicy.setHorizontalStretch(self.stretch)
        #sizePolicy.setVerticalStretch(self.stretch)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)

    def enterEvent(self, QEvent):
        self.setStyleSheet('border: 2px solid rgb(0, 128, 255);; color: rgb(0, 128, 255);')

    def leaveEvent(self, QEvent):
        self.setStyleSheet('color: black')

        
        
def main():
    app = QtGui.QApplication(sys.argv)
    main = Map(None)
    
    
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()