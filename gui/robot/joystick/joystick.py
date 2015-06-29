# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 18:34:05 2014

@author: Argen
"""

import sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QSizePolicy, QWidget)

from gui.robot.joystick import ui_joystick


class Joystick(QWidget, ui_joystick.Ui_joystickWidget):
    '''
    Simulation of a Battery level widget
    '''
    def __init__(self,parent):
        QWidget.__init__(self,parent)
        self.setupUi(self)
        #self.minSize = minSize
        #self.maxSize = maxSize
        self.pressUp = False
        self.pressDown = False
        self.pressLeft = False
        self.pressRight = False
        self.initUI()
        
    def initUI(self):
        '''
        self.setObjectName("joystick")
        self.layout = QVBoxLayout(self)
        self.layout.setMargin(1)
        self.layout.setObjectName("layout")
        
        self.joystickControl = QGroupBox("joystick",self)
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
        
        #self.setMinimumSize(self.minSize)
        #self.setMaximumSize(self.maxSize)        
        '''
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)
    '''
    def format_key(self,key):
        font = QFont()
        font.setPointSize(20)
        key.setAlignment(QtCore.Qt.AlignCenter)
        key.setFont(font)
        key.setFrameStyle(QFrame.Sunken | QFrame.StyledPanel)
        
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
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
    '''
        
    def keyPressEvent (self, event):
        key = event.key()
        
        if not self.pressLeft and key == QtCore.Qt.Key_Left:
            self.left.setStyleSheet('border: 2px solid green; color: green')
            self.center.setStyleSheet('color: black')            
            self.pressLeft = True
        elif not self.pressUp and key == QtCore.Qt.Key_Up:
            self.up.setStyleSheet('border: 2px solid green; color: green')
            self.center.setStyleSheet('color: black')
            self.pressUp = True
        elif not self.pressRight and key == QtCore.Qt.Key_Right:    
            self.right.setStyleSheet('border: 2px solid green; color: green')
            self.center.setStyleSheet('color: black')
            self.pressRight = True
        elif not self.pressDown and key == QtCore.Qt.Key_Down:
            self.down.setStyleSheet('border: 2px solid green; color: green')
            self.center.setStyleSheet('color: black')
            self.pressDown = True
        elif self.pressDown and self.pressLeft:
            self.downleft.setStyleSheet('border: 2px solid green; color: green')
            self.center.setStyleSheet('color: black')
            self.down.setStyleSheet('color: black')
            self.left.setStyleSheet('color: black')
        elif self.pressUp and self.pressLeft:
            self.topleft.setStyleSheet('border: 2px solid green; color: green')
            self.center.setStyleSheet('color: black')
            self.up.setStyleSheet('color: black')
            self.left.setStyleSheet('color: black')
        elif self.pressDown and self.pressRight:
            self.downright.setStyleSheet('border: 2px solid green; color: green')
            self.center.setStyleSheet('color: black')
            self.down.setStyleSheet('color: black')
            self.right.setStyleSheet('color: black')
        elif self.pressUp and self.pressRight:
            self.topright.setStyleSheet('border: 2px solid green; color: green')
            self.center.setStyleSheet('color: black')
            self.up.setStyleSheet('color: black')
            self.right.setStyleSheet('color: black')
        #else:
            #self.center.setStyleSheet('border: 2px solid green; color: green')
        
            
        
    def keyReleaseEvent(self, event):
        key = event.key()   
        if key == QtCore.Qt.Key_Left:
            self.left.setStyleSheet('color: black')
            self.topleft.setStyleSheet('color: black')
            self.downleft.setStyleSheet('color: black')
            self.center.setStyleSheet('border: 2px solid green; color: green')
            self.pressLeft = False
        elif key == QtCore.Qt.Key_Up:
            self.up.setStyleSheet('color: black')
            self.topleft.setStyleSheet('color: black')
            self.topright.setStyleSheet('color: black')
            self.center.setStyleSheet('border: 2px solid green; color: green')
            self.pressUp = False
        elif key == QtCore.Qt.Key_Right:
            self.right.setStyleSheet('color: black')
            self.downright.setStyleSheet('color: black')
            self.topright.setStyleSheet('color: black')
            self.center.setStyleSheet('border: 2px solid green; color: green')
            self.pressRight = False
        elif key == QtCore.Qt.Key_Down:
            self.down.setStyleSheet('color: black')
            self.downleft.setStyleSheet('color: black')
            self.downright.setStyleSheet('color: black')
            self.center.setStyleSheet('border: 2px solid green; color: green')
            self.pressDown = False
        else:
            self.center.setStyleSheet('border: 2px solid green; color: green')
        #else: 
         #   QWidget.keyReleaseEvent(self,event)
    

def main():
    app = QtGui.QApplication(sys.argv)
    minSize = QtCore.QSize(250, 250)
    maxSize = QtCore.QSize(300, 300)
    main = Joystick(None)
    
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()