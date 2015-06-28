# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 18:33:54 2014

@author: Argen
"""

import sys

from PyQt4 import QtGui
from PyQt4.QtGui import (QWidget)

from GUI.StateSensors.Internal import BatteryUI


class Battery(QWidget, BatteryUI.Ui_batteryStatus):
    '''
    Simulation of a Battery level widget
    '''
    def __init__(self,parent):
        QWidget.__init__(self,parent)
        self.setupUi(self)

    def initUI(self):
        self.setupUi(self)


def main():
    app = QtGui.QApplication(sys.argv)
    main = Battery(None)
    
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()