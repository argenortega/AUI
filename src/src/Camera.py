# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 00:48:21 2014

@author: Argen
"""
from PyQt4 import QtGui, QtCore

class Camera(QtGui.QWidget):
    '''
    Simulation of a camera widget
    '''
    def __init__(self,parent,num):
        QtGui.QWidget.__init__(self,parent)
        self.num = num
        self.initUI()
        
    def initUI(self):        
        self.setMinimumSize(300,300)
        self.resize(300,300)        
        self.cam = QtGui.QLabel("Camera %d"%self.num)  
        self.cam.setAlignment(QtCore.Qt.AlignCenter)
        self.cam.setFrameStyle(QtGui.QFrame.Sunken | QtGui.QFrame.StyledPanel)
        #cam.sizeHint(300,300)
        #self.setCentralWidget(self.cam)
        self.hbox = QtGui.QHBoxLayout()
        self.hbox.addWidget(self.cam)        
        self.setLayout(self.hbox)