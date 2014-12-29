# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 00:19:25 2014

@author: Argen
"""
from PyQt4 import QtGui, QtCore

class ScreenshotImage(QtGui.QWidget):
    def __init__(self,parent):
        QtGui.QWidget.__init__(self,parent)
        self.initUI()
        
    def initUI(self):        
        self.setMinimumSize(300,300)
        self.resize(300,300)        
        self.cam = QtGui.QLabel("Screenshot Image ")  
        self.cam.setAlignment(QtCore.Qt.AlignCenter)
        self.cam.setFrameStyle(QtGui.QFrame.Sunken | QtGui.QFrame.StyledPanel)
        #cam.sizeHint(300,300)
        #self.setCentralWidget(self.cam)
        self.hbox = QtGui.QHBoxLayout()
        self.hbox.addWidget(self.cam)        
        self.setLayout(self.hbox)