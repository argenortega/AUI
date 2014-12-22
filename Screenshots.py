# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 00:48:21 2014

@author: Argen
"""
from PyQt4 import QtGui, QtCore

class Screenshots(QtGui.QWidget):
    '''
    Simulation of a camera widget
    '''
    def __init__(self,parent):
        QtGui.QWidget.__init__(self,parent)
        self.initUI()
        
    def initUI(self):        
        self.setMinimumSize(90,30)
        self.setMaximumSize(400,100)
        self.resize(200,60)        
        self.ss = QtGui.QLabel("Screenshots")  
        self.ss.setAlignment(QtCore.Qt.AlignCenter)
        self.ss.setFrameStyle(QtGui.QFrame.Sunken | QtGui.QFrame.StyledPanel)
        #cam.sizeHint(300,300)
        #self.setCentralWidget(self.cam)
        self.hbox = QtGui.QHBoxLayout()
        self.hbox.addWidget(self.ss)        
        self.setLayout(self.hbox)