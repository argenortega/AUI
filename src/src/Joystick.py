# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 18:34:05 2014

@author: Argen
"""

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QSizePolicy, QLabel, QVBoxLayout, QFrame, 
                         QApplication, QGroupBox, QFont, QGridLayout)
import sys

class Joystick(QtGui.QWidget):
    '''
    Simulation of a Battery level widget
    '''
    def __init__(self,parent,minSize,maxSize):
        QtGui.QWidget.__init__(self,parent)
        self.minSize = minSize
        self.maxSize = maxSize
        self.initUI()
        
    def initUI(self):
        
        self.setObjectName("joystick")
        self.layout = QVBoxLayout(self)
        self.layout.setMargin(1)
        self.layout.setObjectName("layout")
        
        self.joystickControl = QGroupBox("Joystick",self)
        self.joystickControl.setObjectName("joystickControl")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.joystickControl.setLayout(self.gridLayout)
        
        self.topleft = QLabel(self)
        self.format_key(self.topleft)
        self.topleft.setObjectName("topleft")
        self.gridLayout.addWidget(self.topleft, 0, 0)
        
        self.up = QLabel(self)
        self.format_key(self.up)
        self.up.setObjectName("up")
        self.gridLayout.addWidget(self.up, 0, 1)
        
        self.topright = QLabel(self)
        self.format_key(self.topright)
        self.topright.setObjectName("topright")
        self.gridLayout.addWidget(self.topright, 0, 2)
        
        self.left = QLabel(self)
        self.format_key(self.left)
        self.left.setObjectName("left")
        self.gridLayout.addWidget(self.left, 1, 0)
        
        self.center = QLabel(self)
        self.format_key(self.center)
        self.center.setObjectName("center")
        self.gridLayout.addWidget(self.center, 1, 1)
        
        self.right = QLabel(self)
        self.format_key(self.right)
        self.right.setObjectName("right")
        self.gridLayout.addWidget(self.right, 1, 2)
        
        self.downleft = QLabel(self)
        self.format_key(self.downleft)
        self.downleft.setObjectName("downleft")
        self.gridLayout.addWidget(self.downleft, 2, 0)
        
        self.down = QLabel(self)
        self.format_key(self.down)        
        self.down.setObjectName("down")
        self.gridLayout.addWidget(self.down, 2, 1)
        
        self.downright = QLabel(self)
        self.format_key(self.downright)
        self.downright.setObjectName("downright")
        self.gridLayout.addWidget(self.downright, 2, 2)
        
        self.retranslateUi(self)        
        
        self.layout.addWidget(self.joystickControl)
        
        self.setMinimumSize(self.minSize)
        #self.setMaximumSize(self.maxSize)        
        
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)
        
    def format_key(self,key):
        font = QFont()
        font.setPointSize(20)
        key.setAlignment(QtCore.Qt.AlignCenter)
        key.setFont(font)
        key.setFrameStyle(QFrame.Sunken | QFrame.StyledPanel)
        
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)
        
    def retranslateUi(self, AUI):        
        self.topleft.setText(QApplication.translate("joystick", "↖︎", None,QApplication.UnicodeUTF8))
        self.up.setText(QApplication.translate("joystick", "↑", None,QApplication.UnicodeUTF8))
        self.topright.setText(QApplication.translate("joystick", "↗︎", None,QApplication.UnicodeUTF8))
        self.left.setText(QApplication.translate("joystick", "←", None,QApplication.UnicodeUTF8))
        self.center.setText(QApplication.translate("joystick", "•", None,QApplication.UnicodeUTF8))
        self.right.setText(QApplication.translate("joystick", "→", None,QApplication.UnicodeUTF8))
        self.downleft.setText(QApplication.translate("joystick", "↙︎", None,QApplication.UnicodeUTF8))
        self.down.setText(QApplication.translate("joystick", "↓", None,QApplication.UnicodeUTF8))
        self.downright.setText(QApplication.translate("joystick", "↘︎", None,QApplication.UnicodeUTF8))
        
        
        

def main():
    app = QtGui.QApplication(sys.argv)
    minSize = QtCore.QSize(250, 250)
    maxSize = QtCore.QSize(300, 300)
    main = Joystick(None,minSize,maxSize)
    
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()