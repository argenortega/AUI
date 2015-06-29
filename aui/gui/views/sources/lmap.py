# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 15:28:54 2014

@author: Argen
"""

import sys

from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import (QWidget, QSizePolicy, QApplication)

from aui.gui.views.sources import ui_lmap


class LocalMap(QWidget, ui_lmap.Ui_NewView):
    '''
    Simulation of an additional view widget
    '''
    inside = pyqtSignal(str)

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.initUI()
        
    def initUI(self):
        #self.currentmap = 'border-image: url(:/maps/local);'
        self.currentmap = self.map.styleSheet()

        '''
        Size of the widget
        '''
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)

    def enterEvent(self, QEvent):
        self.inside.emit('Local Map')

    def leaveEvent(self, QEvent):
        self.map.setStyleSheet(self.currentmap)


        
        
def main():
    app = QApplication(sys.argv)
    main = LocalMap(None)
    main.show()
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()