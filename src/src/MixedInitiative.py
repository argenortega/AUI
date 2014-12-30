# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 04:42:13 2014

@author: Argen
"""

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QSizePolicy, QVBoxLayout, QFrame,
                         QHBoxLayout, QPushButton, QTextEdit, QTextCursor)
import sys

class MixedInitiative(QtGui.QWidget):
    def __init__(self,parent):
        QtGui.QWidget.__init__(self,parent)
        self.initUI()
        
    def initUI(self):
        self.mixedInitiativeLayout = QVBoxLayout()
        self.AUIStatusLayout = QHBoxLayout()
        self.AUIMsgsLayout = QHBoxLayout()
        #self.mixedInitiativeLayout.addLayout(self.AUIStatusLayout)        
        #self.mixedInitiativeLayout.addLayout(self.AUIMsgsLayout)
        self.setLayout(self.mixedInitiativeLayout)
        self.setMaximumSize(QtCore.QSize(16777215, 100))
        self.setObjectName("mixedInitiative")
        #self.mixedInitiativeLayout = QtGui.QVBoxLayout(self.mixedInitiative)
        self.mixedInitiativeLayout.setMargin(1)
        self.mixedInitiativeLayout.setObjectName("mixedInitiativeLayout")
        
        self.AUIStatusLayout.setMargin(0)
        self.AUIStatusLayout.setObjectName("AUIStatusLayout")
        self.AUIStatusLabel = QtGui.QLabel("AUI Status", self)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.AUIStatusLabel.sizePolicy().hasHeightForWidth())
        self.AUIStatusLabel.setSizePolicy(sizePolicy)
        self.AUIStatusLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.AUIStatusLabel.setMaximumSize(QtCore.QSize(100, 20))
        self.AUIStatusLabel.setScaledContents(False)
        self.AUIStatusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AUIStatusLabel.setWordWrap(False)
        self.AUIStatusLabel.setObjectName("AUIStatusLabel")
        self.AUIStatusLayout.addWidget(self.AUIStatusLabel)
        
        self.AUItoggleButton = QPushButton("Off", self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.AUItoggleButton.sizePolicy().hasHeightForWidth())
        self.AUItoggleButton.setSizePolicy(sizePolicy)
        self.AUItoggleButton.setMinimumSize(QtCore.QSize(60, 30))
        self.AUItoggleButton.setMaximumSize(QtCore.QSize(60, 30))
        self.AUItoggleButton.setMouseTracking(True)
        self.AUItoggleButton.setCheckable(True)
        #self.AUItoggleButton.setChecked(True)
        self.AUItoggleButton.setObjectName("AUItoggleButton")
        self.AUItoggleButton.clicked[bool].connect(self.press)
        self.AUIStatusLayout.addWidget(self.AUItoggleButton)
        self.AUIStatusLayout.addStretch()
        
        self.mixedInitiativeLayout.addLayout(self.AUIStatusLayout)
        
        self.AUIMsgs = QFrame(self)
        self.AUIMsgs.setObjectName("AUIMsgs")
        self.AUIMsgs.setFrameStyle(QFrame.StyledPanel|QFrame.Sunken)
        
        
        self.AUIMsgsLayout = QtGui.QHBoxLayout(self.AUIMsgs)
        self.AUIMsgsLayout.setMargin(2)
        self.AUIMsgsLayout.setObjectName("AUIMsgsLayout")
        
        self.AUIMsgs.setLayout(self.AUIMsgsLayout)        
        
        self.textBrowserAUIMix = QTextEdit(self.AUIMsgs)
        self.textBrowserAUIMix.setReadOnly(True)
        self.textBrowserAUIMix.moveCursor(QTextCursor.End)
        sb = self.textBrowserAUIMix.verticalScrollBar()
        sb.setValue(sb.maximum())
        self.textBrowserAUIMix.setMinimumSize(QtCore.QSize(700, 30))
        self.textBrowserAUIMix.setMaximumSize(QtCore.QSize(1200, 60))
        self.textBrowserAUIMix.setObjectName("textBrowserAUIMix")
        sizePolicy = QtGui.QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(True)
        self.textBrowserAUIMix.setSizePolicy(sizePolicy)

        self.horizontalLayout = QtGui.QHBoxLayout(self.textBrowserAUIMix)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AUIMsgsLayout.addWidget(self.textBrowserAUIMix)

        self.buttonBoxAUIMix = QtGui.QDialogButtonBox(self.AUIMsgs)
        self.buttonBoxAUIMix.setOrientation(QtCore.Qt.Vertical)
        self.buttonBoxAUIMix.setStandardButtons(QtGui.QDialogButtonBox.Discard|QtGui.QDialogButtonBox.Apply)
        self.buttonBoxAUIMix.setObjectName("buttonBoxAUIMix")
        self.buttonBoxAUIMix.setFocus(False)
        self.AUIMsgsLayout.addWidget(self.buttonBoxAUIMix)
        self.AUIMsgsLayout.addStretch()
        
        sizePolicy = QtGui.QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.AUIMsgs.setSizePolicy(sizePolicy)        
        
        self.AUItoggleButton.toggled.connect(self.AUIMsgs.setVisible)

        self.AUIMsgs.hide()
        self.mixedInitiativeLayout.addWidget(self.AUIMsgs)
        
        self.sizePolicy = QtGui.QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(True)
        
        self.setSizePolicy(self.sizePolicy)
        
    def press(self,toggled):
        source = self.sender()
        if toggled:
            self.AUItoggleButton.setText("On")
            #self.AUItoggleButton.setChecked(False)
            #self.AUIMsgs.setVisible(True)
            self.setSizePolicy(self.sizePolicy)

        else:
            self.AUItoggleButton.setText("Off")
            #self.AUItoggleButton.setChecked(True)
            #self.AUIMsgs.setVisible(False)
            self.setSizePolicy(self.sizePolicy)
    
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    main = MixedInitiative(None)
    
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()