# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 15:04:51 2014

@author: Argentina Ortega Sáinz
@version: 0.0.1
"""
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.uic import loadUi
from Camera import *
from Screenshots import *
from AUIWidgets import *
from ScreenshotImage import *
from CameraViews import *
from Parameters import *
from AUIParam import *

'''
Adaptive User Interface for TRADR project
'''
class AUI(QtGui.QWidget):    
    def __init__(self,parent=None):
        #QtGui.QMainWindow.__init__(self)
        super(AUI, self).__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(100,100 , 1090, 1080)
        self.setWindowTitle("Static GUI")

        self.hbox = QtGui.QHBoxLayout()
        self.setLayout(self.hbox)
        
        self.vbox = QtGui.QVBoxLayout()
        self.hbox.addLayout(self.vbox)

        aui = AUIWidgets(self)
        self.vbox.addWidget(aui)

        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(5)
        self.vbox.addLayout(self.grid)                
        
        vc = QtGui.QVBoxLayout()
        hc = QtGui.QHBoxLayout()
        cv = CameraViews(self)
        vc.addWidget(cv)
        c1 = Camera(self,1)
        c2 = Camera(self,2)  
        hc.addWidget(c1)
        hc.addWidget(c2)
        vc.addLayout(hc)
        self.grid.addLayout(vc,1,0)
        
        v = QtGui.QVBoxLayout()   
        ss = Screenshots(self)
        si = ScreenshotImage(self)
        v.addWidget(ss)
        v.addWidget(si)        
        self.grid.addLayout(v,1,2)
        #self.grid.addWidget(ss,2,2)
        p = loadUi('AUIParam.ui')
        self.hbox.addWidget(p)
        self.show()
        
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    main = AUI()
    
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()
