# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 17:21:56 2014

@author: Argen
"""

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QSizePolicy, QVBoxLayout, QFrame,
                         QHBoxLayout, QPushButton, QLabel,
                         QGroupBox)
from PyQt4.QtCore import QSize
import sys

class Screenshots(QtGui.QWidget):
    def __init__(self,parent,minSize,maxSize,stretch):
        QtGui.QWidget.__init__(self,parent)
        self.minSize = minSize
        self.maxSize = maxSize
        self.stretch = stretch
        self.initUI()
        
    def initUI(self):
        self.setObjectName("CurrentScreenshot")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setMargin(1)
        self.layout.setObjectName("layout")
        
        self.currentScreenshot = QLabel("Image 1", self)
        self.currentScreenshot.setAlignment(QtCore.Qt.AlignCenter)
        self.currentScreenshot.setObjectName("currentScreenshot")        
        self.currentScreenshot.setAlignment(QtCore.Qt.AlignCenter)
        self.currentScreenshot.setFrameStyle(QFrame.Sunken | QFrame.StyledPanel)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.currentScreenshot.setFont(font)
        #self.currentScreenshot.setObjectName("currentScreenshotLabel")
        self.currentScreenshot.setMinimumSize(self.minSize)
        self.currentScreenshot.setMaximumSize(self.maxSize)        
        self.currentScreenshot.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.currentScreenshot.setMouseTracking(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(self.stretch)
        sizePolicy.setVerticalStretch(self.stretch)
        sizePolicy.setHeightForWidth(True)
        self.currentScreenshot.setSizePolicy(sizePolicy)
        self.layout.addWidget(self.currentScreenshot)
        
        self.ExtraScreenshots = QFrame(self)
        self.ExtraScreenshots.setObjectName("ExtraScreenshots")
        self.extraScreenshotLayout = QVBoxLayout(self.ExtraScreenshots)
        self.extraScreenshotLayout.setMargin(1)
        self.extraScreenshotLayout.setObjectName("extraScreenshotLayout")
        
        self.extraScreenGroup = QGroupBox("Screenshots", self.ExtraScreenshots)
        self.extraScreenGroup.setObjectName("extraScreenGroup")
        self.extraScreenshotGroupLayout = QHBoxLayout(self.extraScreenGroup)
        self.extraScreenshotGroupLayout.setObjectName("extraScreenshotGroupLayout")
        
        self.img1 = QtGui.QLabel("Image 1", self.extraScreenGroup)
        self.img1.setObjectName("img1")
        self.format_screenshot(self.img1)
        self.extraScreenshotGroupLayout.addWidget(self.img1)
        
        self.img2 = QtGui.QLabel("Image 2", self.extraScreenGroup)
        self.img2.setObjectName("img2")
        self.format_screenshot(self.img2)
        self.extraScreenshotGroupLayout.addWidget(self.img2)
        
        self.img3 = QtGui.QLabel("Image 3", self.extraScreenGroup)
        self.img3.setObjectName("img3")
        self.format_screenshot(self.img3)
        self.extraScreenshotGroupLayout.addWidget(self.img3)
        
        self.extraScreenshotLayout.addWidget(self.extraScreenGroup)
        self.layout.addWidget(self.ExtraScreenshots)
        
        
        self.setMinimumSize(QSize(self.minSize.width()*1.1,self.minSize.height()*1.7))
        self.setMaximumSize(QSize(self.maxSize.width()*1.3,self.maxSize.height()*2))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(self.stretch)
        sizePolicy.setVerticalStretch(self.stretch)
        sizePolicy.setHeightForWidth(False)
        self.setSizePolicy(sizePolicy)
        
        
    def format_screenshot(self,img):
        img.setAlignment(QtCore.Qt.AlignCenter)
        img.setFrameStyle(QFrame.Sunken | QFrame.StyledPanel)
        img.setMinimumSize(self.minSize/3)
        img.setMaximumSize(self.maxSize/3)        
        img.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(self.stretch)
        sizePolicy.setVerticalStretch(self.stretch)
        sizePolicy.setHeightForWidth(True)
        img.setSizePolicy(sizePolicy)
        
        
    
def main():
    app = QtGui.QApplication(sys.argv)
    minSize = QtCore.QSize(350, 350)
    maxSize = QtCore.QSize(400, 400)
    stretch = 1
    main = Screenshots(None,minSize,maxSize,stretch)
    
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()