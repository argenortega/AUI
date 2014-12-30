# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 18:33:45 2014

@author: Argen
"""
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QSizePolicy, QLabel, QHBoxLayout, QFrame)
import sys

class Wifi(QtGui.QWidget):
    '''
    Simulation of a Wifi level widget
    '''
    def __init__(self,parent, minSize, maxSize):
        QtGui.QWidget.__init__(self,parent)
        self.minSize = minSize
        self.maxSize = maxSize
        self.initUI()
        
    def initUI(self):
        self.setObjectName("wifi_status")
        self.layout = QtGui.QVBoxLayout(self)
        self.layout.setMargin(0)
        self.layout.setObjectName("WifiLayout")
        self.setLayout(self.layout)
        self.wifiLevel = QtGui.QGroupBox("Wifi",self)
        self.wifiLevel.setObjectName("wifiLevel")
        
        self.wifiBoxLevel = QHBoxLayout(self.wifiLevel)
        self.wifiBoxLevel.setObjectName("wifiBoxLevel")
        
        self.wifi = QtGui.QProgressBar(self.wifiLevel)
        self.wifi.setProperty("value", 100)
        self.wifi.setAlignment(QtCore.Qt.AlignCenter)
        self.wifi.setInvertedAppearance(False)
        self.wifi.setObjectName("wifi")
        
        self.wifiBoxLevel.addWidget(self.wifi)
        
        self.value = QtGui.QLabel(self.wifiLevel)
        self.value.setText("%d"%self.wifi.value())        
        self.wifiBoxLevel.addWidget(self.value)
        
        self.layout.addWidget(self.wifiLevel)
        
        
        self.setMinimumSize(self.minSize)
        #self.setMaximumSize(self.maxSize)        
        
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(False)
        self.setSizePolicy(sizePolicy)
        

def main():
    app = QtGui.QApplication(sys.argv)
    minSize = QtCore.QSize(100, 100)
    maxSize = QtCore.QSize(300, 300)
    stretch = 3
    main = Wifi(None,minSize,maxSize)
    
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()