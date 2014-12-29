# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 18:34:05 2014

@author: Argen
"""

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QSizePolicy, QLabel, QVBoxLayout, QFrame)
import sys

class Joystick(QtGui.QWidget):
    '''
    Simulation of a Battery level widget
    '''
    def __init__(self,parent,minSize,maxSize,stretch):
        QtGui.QWidget.__init__(self,parent)
        self.initUI()
        
    def initUI(self):
        
        self.setObjectName("joystick")
        self.layout = QtGui.QGridLayout(self)
        self.layout.setMargin(0)
        self.layout.setObjectName("layout")
        
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.topleft = QtGui.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.topleft.setFont(font)
        self.topleft.setAlignment(QtCore.Qt.AlignCenter)
        self.topleft.setObjectName("topleft")
        self.gridLayout.addWidget(self.topleft, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.up = QtGui.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.up.setFont(font)
        self.up.setAlignment(QtCore.Qt.AlignCenter)
        self.up.setObjectName("up")
        self.gridLayout.addWidget(self.up, 0, 1, 1, 1)
        self.topright = QtGui.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.topright.setFont(font)
        self.topright.setAlignment(QtCore.Qt.AlignCenter)
        self.topright.setObjectName("topright")
        self.gridLayout.addWidget(self.topright, 0, 2, 1, 1)
        self.left = QtGui.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.left.setFont(font)
        self.left.setAlignment(QtCore.Qt.AlignCenter)
        self.left.setObjectName("left")
        self.gridLayout.addWidget(self.left, 1, 0, 1, 1)
        self.center = QtGui.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.center.setFont(font)
        self.center.setAlignment(QtCore.Qt.AlignCenter)
        self.center.setObjectName("center")
        self.gridLayout.addWidget(self.center, 1, 1, 1, 1)
        self.right = QtGui.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.right.setFont(font)
        self.right.setAlignment(QtCore.Qt.AlignCenter)
        self.right.setObjectName("right")
        self.gridLayout.addWidget(self.right, 1, 2, 1, 1)
        self.downleft = QtGui.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.downleft.setFont(font)
        self.downleft.setAlignment(QtCore.Qt.AlignCenter)
        self.downleft.setObjectName("downleft")
        self.gridLayout.addWidget(self.downleft, 2, 0, 1, 1)
        self.down = QtGui.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.down.setFont(font)
        self.down.setAlignment(QtCore.Qt.AlignCenter)
        self.down.setObjectName("down")
        self.gridLayout.addWidget(self.down, 2, 1, 1, 1)
        self.downright = QtGui.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.downright.setFont(font)
        self.downright.setAlignment(QtCore.Qt.AlignCenter)
        self.downright.setObjectName("downright")
        self.gridLayout.addWidget(self.downright, 2, 2, 1, 1)
        self.layout.addLayout(self.gridLayout, 0, 0, 1, 1)
        
        

def main():
    app = QtGui.QApplication(sys.argv)
    minSize = QtCore.QSize(100, 100)
    maxSize = QtCore.QSize(300, 300)
    stretch = 3
    main = Joystick(None,minSize,maxSize,stretch)
    
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()