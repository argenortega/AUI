# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 04:42:13 2014

@author: Argen
"""

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QWidget, QSizePolicy, QVBoxLayout, QFrame,
                         QHBoxLayout, QPushButton, QTextEdit, QTextCursor)
import MixedInitiativeUI as MixInitUI
import sys

class MixedInitiative(QWidget,MixInitUI.Ui_mixedInitiative):
    def __init__(self,parent):
        QWidget.__init__(self,parent)
        self.setupUi(self)
        self.initUI()
        
    def initUI(self):
        self.AUItoggleButton.clicked[bool].connect(self.press)
        self.AUItoggleButton.toggled.connect(self.AUIMsgs.setVisible)

        self.AUIMsgs.hide()

        self.sizePolicy = QtGui.QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)

        self.setSizePolicy(self.sizePolicy)

        self.textBrowserAUIMix.setText('[9:00]: Adaptive capabilities turned on.')

        
    def press(self,toggled):
        #source = self.sender()
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