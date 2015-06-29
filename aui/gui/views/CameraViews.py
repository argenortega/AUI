# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 00:37:22 2014

@author: Argen
"""

from PyQt4 import QtGui, QtCore

class CameraViews(QtGui.QWidget):
     def __init__(self,parent):
        QtGui.QWidget.__init__(self,parent)
        self.initUI()
     def initUI(self):
        self.hbox = QtGui.QHBoxLayout()
        self.setLayout(self.hbox)
        
        self.buttonGroup = QtGui.QButtonGroup()
        self.buttonGroup.setExclusive(True)        
        
        self.a = QtGui.QPushButton("a", self)
        self.a.setCheckable(True)
        self.buttonGroup.addButton(self.a)
        self.hbox.addWidget(self.a)
        self.b = QtGui.QPushButton("b", self)
        self.b.setCheckable(True)        
        self.buttonGroup.addButton(self.b)
        self.hbox.addWidget(self.b)
        self.c = QtGui.QPushButton("c", self)
        self.c.setCheckable(True)
        self.buttonGroup.addButton(self.c)
        self.hbox.addWidget(self.c)
        self.d = QtGui.QPushButton("d", self)
        self.d.setCheckable(True)
        self.buttonGroup.addButton(self.d)
        self.hbox.addWidget(self.d)
        