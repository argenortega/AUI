# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 23:02:54 2014

@author: Argen
"""

from PyQt4 import QtGui, QtCore

class AUIWidgets(QtGui.QWidget):
    '''
    Simulation of a camera widget
    '''
    def __init__(self,parent):
        QtGui.QWidget.__init__(self,parent)
        self.initUI()
        
    def initUI(self):        
        self.setMinimumSize(30,90)
        self.setMaximumSize(900,100)
        self.resize(10,90)        
        self.hbox = QtGui.QHBoxLayout()
        self.setLayout(self.hbox)
        
        self.togBtn = QtGui.QPushButton("On", self)
        self.togBtn.setChecked(True)        
        self.togBtn.setCheckable(True) 
        self.togBtn.setMinimumSize(QtCore.QSize(50,20))          
        #self.togBtn.setFixedSize(70,70)
        self.togBtn.clicked[bool].connect(self.press)        
        self.hbox.addWidget(self.togBtn)        

        
        self.msgs = QtGui.QLabel("Messages")  
        self.msgs.setAlignment(QtCore.Qt.AlignCenter)
        self.msgs.setMinimumSize(700,70)
        self.msgs.setMaximumSize(QtCore.QSize(900,90))
        self.msgs.resize(QtCore.QSize(800,70))
        self.msgs.setFrameStyle(QtGui.QFrame.Sunken | QtGui.QFrame.StyledPanel)        
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(True)
        self.msgs.setSizePolicy(sizePolicy)
        self.hbox.addWidget(self.msgs)
        
        self.acc = QtGui.QPushButton("Accept",self)
        self.hbox.addWidget(self.acc)
    
    def press(self,toggled):
        source = self.sender()
        if toggled:
            self.togBtn.setText("Off")
        else:
            self.togBtn.setText("On")