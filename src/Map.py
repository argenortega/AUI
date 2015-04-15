# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 15:28:25 2014

@author: Argen
"""

from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import (QWidget, QSizePolicy, QApplication)
import sys
import MapUI

class Map(QWidget, MapUI.Ui_MapWidget):
    def __init__(self,parent):
        QWidget.__init__(self,parent)
        self.setupUi(self)
        self.initUI()
        self.txt = 'Global Map'
        
    def initUI(self):
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)

def main():
    app = QApplication(sys.argv)
    main = Map(None)
    
    
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()