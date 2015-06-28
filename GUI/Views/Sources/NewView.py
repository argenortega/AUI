# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 15:28:54 2014

@author: Argen
"""

import sys

from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import (QWidget, QSizePolicy, QApplication)

from GUI.Views.Sources import ExtraViewUI


class NewView(QWidget, ExtraViewUI.Ui_NewView):
    '''
    Simulation of an additional view widget
    '''
    inside = pyqtSignal(str)

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.initUI()
        
    def initUI(self):
        self.currentmap = 'border-image: url(:/maps/local0003);'

        '''
        Size of the widget
        '''
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)

    def enterEvent(self, QEvent):
        self.inside.emit('Local Map')

    def leaveEvent(self, QEvent):
        self.view.setStyleSheet(self.currentmap)


        
        
def main():
    app = QApplication(sys.argv)
    main = NewView(None)
    main.show()
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()