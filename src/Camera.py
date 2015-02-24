# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 00:48:21 2014

@author: Argen
"""
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QWidget, QSizePolicy, QLabel, QVBoxLayout, QFrame)
import sys
import CameraUI

class Camera(QWidget, CameraUI.Ui_Camera):
    '''
    Simulation of a camera widget
    '''
    def __init__(self,parent,num,stretch):
        QWidget.__init__(self,parent)
        self.setupUi(self)
        self.num = num
        #self.minSize = minSize
        #self.maxSize = maxSize
        self.stretch = stretch
        self.initUI()
        
    def initUI(self):
        self.setObjectName("Camera%d"%self.num)
        #self.layout = QVBoxLayout()
        #self.layout.setMargin(0)
        #self.layout.setObjectName("cam%dLayout"%self.num)
        #self.setLayout(self.layout)
        
        #self.cam = QLabel("Camera %d"%self.num,self)
        self.cam.setText("Camera %d"%self.num)
        #self.cam.setAlignment(QtCore.Qt.AlignCenter)
        #self.cam.setFrameStyle(QFrame.Sunken | QFrame.StyledPanel)
        #cam.sizeHint(300,300)        
        #font = QtGui.QFont()
        #font.setPointSize(28)
        #self.cam.setFont(font)
        #self.cam.setObjectName("Cam1Label")
        #self.layout.addWidget(self.cam)
        
        '''
        Size of the widget
        '''
        #self.setMinimumSize(self.minSize)
        #self.setMaximumSize(self.maxSize)
        #self.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        #self.setMouseTracking(True)

        
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(self.stretch)
        sizePolicy.setVerticalStretch(self.stretch)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)        
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    minSize = QtCore.QSize(100, 100)
    maxSize = QtCore.QSize(300, 300)
    stretch = 3
    main = Camera(None,1,minSize,maxSize,stretch)
    
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()