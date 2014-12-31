# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 17:21:56 2014

@author: Argen
"""

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QSizePolicy, QVBoxLayout, QFrame,
                         QHBoxLayout, QPushButton, QLabel,
                         QGroupBox, QGridLayout)
from PyQt4.QtCore import QSize
import sys

class Screenshots(QtGui.QWidget):
    def __init__(self,parent,minWidth,maxWidth,stretch):
        QtGui.QWidget.__init__(self,parent)
        self.minWidth = minWidth
        self.maxWidth = maxWidth
        self.stretch = stretch
        self.num = 3
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
        self.currentScreenshot.setMinimumSize(QSize(self.minWidth*0.9,self.minWidth*0.9))
        #self.currentScreenshot.setMaximumSize(QSize(self.maxWidth*0.9,self.maxWidth*0.9))        
        self.currentScreenshot.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.currentScreenshot.setMouseTracking(True)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(self.stretch)
        sizePolicy.setVerticalStretch(self.stretch)
        sizePolicy.setHeightForWidth(True)
        self.currentScreenshot.setSizePolicy(sizePolicy)
        self.layout.addWidget(self.currentScreenshot)
                
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addStretch()        

        self.newS = QPushButton("New", self)
        self.buttonLayout.addWidget(self.newS)
        self.newS.clicked.connect(self.add_new)
        
        
        self.layout.addLayout(self.buttonLayout)
        
        
        self.extraScreenGroup = QGroupBox("Screenshots", self)
        self.extraScreenGroup.setObjectName("extraScreenGroup")
        self.extraScreenshotGroupLayout = QVBoxLayout(self.extraScreenGroup)
        self.extraScreenshotGroupLayout.setObjectName("extraScreenshotGroupLayout")

        self.showLayout = QHBoxLayout()
        self.showLayout.addStretch()
        self.showB = QPushButton("Hide",self)
        self.showB.setCheckable(True)
        self.showLayout.addWidget(self.showB)
        self.extraScreenshotGroupLayout.addLayout(self.showLayout)
        
        self.scrollArea = QtGui.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.extraScreenshots = QFrame(self.scrollArea)
        self.extraScreenshots = QFrame(self.extraScreenGroup)
        self.extraScreenshots.setObjectName("extraScreenshots")
        self.scrollArea.setWidget(self.extraScreenshots)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setViewportMargins(1,1,1,1)
        self.extraScreenshotGroupLayout.addWidget(self.scrollArea)

        #self.scrollBar = QtGui.QScrollBar(QtCore.Qt.Horizontal,self.extraScreenshots)
        
        self.extraScreenshotLayout = QHBoxLayout(self.extraScreenshots)
        self.extraScreenshotLayout.setMargin(0)
        self.extraScreenshotLayout.setObjectName("extraScreenshotLayout")
        
        self.showB.clicked[bool].connect(self.press)
        #self.showB.toggled.connect(self.extraScreenshots.setVisible)
        
        self.img1 = self.new_screenshot(1)
        self.extraScreenshotLayout.addWidget(self.img1)
        
        self.img2 = self.new_screenshot(2)
        self.extraScreenshotLayout.addWidget(self.img2)
        
        self.img3 = self.new_screenshot(3)
        self.extraScreenshotLayout.addWidget(self.img3)
        
        self.scrollArea.setMinimumSize(QSize(self.minWidth*9/10,self.minWidth*.4))
        self.scrollArea.setMaximumSize(QSize(self.maxWidth*0.9,self.maxWidth*.4))
        
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(self.stretch)
        sizePolicy.setVerticalStretch(self.stretch)
        sizePolicy.setHeightForWidth(False)
        self.scrollArea.setSizePolicy(sizePolicy)
        
        self.extraScreenshotGroupLayout.addWidget(self.scrollArea)
        #self.extraScreenshotGroupLayout.addWidget(self.extraScreenshots)
        #self.extraScreenshotGroupLayout.addWidget(self.scrollBar)
        self.layout.addWidget(self.extraScreenGroup)
        
        #self.layout.setAlignment(QtCore.Qt.AlignHCenter)
        
        #self.setMinimumSize(QSize())
        #self.setMaximumSize(QSize(self.maxSize.width()*1.3,self.maxSize.height()*2))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(self.stretch)
        sizePolicy.setVerticalStretch(self.stretch)
        sizePolicy.setHeightForWidth(False)
        self.setSizePolicy(sizePolicy)
        
        
    def new_screenshot(self,num):
        img = QtGui.QLabel("Image %d"%num, self.extraScreenGroup)
        img.setObjectName("img%d"%num)
        img.setAlignment(QtCore.Qt.AlignCenter)
        img.setFrameStyle(QFrame.Sunken | QFrame.StyledPanel)
        img.setMinimumSize(QSize(self.minWidth/3,self.minWidth/3))
        img.setMaximumSize(QSize(self.maxWidth/3,self.maxWidth/3))        
        img.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(True)
        img.setSizePolicy(sizePolicy)
        #img.resize(self.minWidth/3,self.minWidth/3)
        return img
    
    def add_new(self):
        self.num = self.num + 1
        ns = self.new_screenshot(self.num)
        self.extraScreenshotLayout.addWidget(ns)
        
    def press(self,toggled):
        if toggled:
            self.showB.setText("Show")
            self.scrollArea.setVisible(False)
        else:
            self.showB.setText("Hide")
            self.scrollArea.setVisible(True)
        
        
    
def main():
    app = QtGui.QApplication(sys.argv)
    minSize = QtCore.QSize(350, 350)
    maxSize = QtCore.QSize(400, 400)
    stretch = 1
    main = Screenshots(None,350,400,stretch)
    
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()