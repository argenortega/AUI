# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 18:33:54 2014

@author: Argen
"""

import sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QWidget)
from PyQt4.QtCore import pyqtSignal, pyqtSlot

from aui.gui.robot.internal import ui_battery


class Battery(QWidget, ui_battery.Ui_batteryStatus):
    '''
    Simulation of a Battery level widget
    '''
    lev = pyqtSignal(str, str, name='battery_level')
    vis = pyqtSignal(str, str, name='battery_visible')

    def __init__(self,parent):
        QWidget.__init__(self,parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.battery.valueChanged[int].connect(self.send_level)
        self.batteryLevel.clicked[bool].connect(self.send_visible)

    @pyqtSlot(int)
    def send_level(self, value):
        if value > 70:
            self.lev.emit('battery_level', 'Ok')
            # self.change_color('rgb(76, 175, 80)')
        elif 70 >= value > 50:
            self.lev.emit('battery_level', 'Warn')
            # self.change_color('rgb(255, 193, 7)')
        elif value <= 50:
            self.lev.emit('battery_level', 'Critical')
            # self.change_color('rgb(244, 67, 54)')

    @pyqtSlot(bool)
    def send_visible(self, checked):
        if checked:
            self.vis.emit('battery_visible', 'True')
        else:
            self.vis.emit('battery_visible', 'False')


def main():
    app = QtGui.QApplication(sys.argv)
    main = Battery(None)
    
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()