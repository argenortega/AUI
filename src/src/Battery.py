# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 18:33:54 2014

@author: Argen
"""

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QSizePolicy, QLabel, QHBoxLayout, QFrame)
import sys

class Battery(QtGui.QWidget):
    '''
    Simulation of a Battery level widget
    '''
    def __init__(self,parent, minSize, maxSize):
        QtGui.QWidget.__init__(self,parent)
        self.minSize = minSize
        self.maxSize = maxSize
        self.initUI()
        
    def initUI(self):
        self.setObjectName("battery_status")
        self.layout = QtGui.QVBoxLayout(self)
        self.layout.setMargin(0)
        self.layout.setObjectName("BatteryLayout")
        self.setLayout(self.layout)
        self.batteryLevel = QtGui.QGroupBox("Battery",self)
        self.batteryLevel.setObjectName("batteryLevel")
        
        self.batteryBoxLevel = QHBoxLayout(self.batteryLevel)
        self.batteryBoxLevel.setObjectName("batteryBoxLevel")
        
        self.battery = QtGui.QProgressBar(self.batteryLevel)
        self.battery.setProperty("value", 100)
        self.battery.setAlignment(QtCore.Qt.AlignCenter)
        self.battery.setInvertedAppearance(False)
        self.battery.setObjectName("battery")
        
        self.batteryBoxLevel.addWidget(self.battery)
        
        self.value = QtGui.QLabel(self.batteryLevel)
        self.value.setText("%d"%self.battery.value())        
        self.batteryBoxLevel.addWidget(self.value)        
        
        self.p = QLabel("%",self.batteryLevel)
        self.batteryBoxLevel.addWidget(self.p)
        
        self.layout.addWidget(self.batteryLevel)
        
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
    main = Battery(None,minSize,maxSize)
    
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()