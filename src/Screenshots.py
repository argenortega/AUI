# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 17:21:56 2014

@author: Argen
"""

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QSizePolicy, QFrame
from PyQt4.QtCore import QSize
import sys
import ScreenshotsUI
import Screenshot
import ActiveLabel

class Screenshots(QWidget, ScreenshotsUI.Ui_ScreenshotWidget):
    def __init__(self,parent):
        QWidget.__init__(self,parent)
        self.setupUi(self)
        self.num = 4
        self.initUI()
        
    def initUI(self):
        #self.newS.clicked.connect(self.add_new)

        self.showB.clicked[bool].connect(self.press)

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHeightForWidth(False)
        self.scrollArea.setSizePolicy(sizePolicy)
        
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(False)
        self.setSizePolicy(sizePolicy)
        
        
    def new_screenshot(self,num):
        #img = QtGui.QLabel("Image %d"%num, self.extraScreenGroup)
        img = ActiveLabel.ActLabel(self.extraScreenGroup)
        img.setText("Screenshot %d"%num)
        img.setObjectName("img%d"%num)
        img.setAlignment(QtCore.Qt.AlignCenter)
        img.setFrameStyle(QFrame.Sunken | QFrame.StyledPanel)
        img.setMinimumSize(QSize(85,85))
        img.setMaximumSize(QSize(100,100))
        img.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        img.setMouseTracking(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(True)
        img.setSizePolicy(sizePolicy)
        # img.resize(self.minWidth/3,self.minWidth/3)
        return img
    
    def add_new(self):
        self.num = self.num + 1
        ns = self.new_screenshot(self.num)
        self.extraScreenshotLayout.addWidget(ns)
        
    def press(self,toggled):
        if toggled:
            self.showB.setText("+")
            self.scrollArea.setVisible(False)
        else:
            self.showB.setText("-")
            self.scrollArea.setVisible(True)
    
    def select_screenshot(self):
        pass
        
        
    
def main():
    app = QtGui.QApplication(sys.argv)
    minSize = QtCore.QSize(350, 350)
    maxSize = QtCore.QSize(400, 400)
    stretch = 1
    main = Screenshots(None)
    
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()