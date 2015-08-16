# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 18:33:45 2014

@author: Argen
"""
import sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QWidget, QSizePolicy, QLabel, QHBoxLayout)
from PyQt4.QtCore import pyqtSignal, pyqtSlot

from aui.gui.robot.internal import ui_wifi


class Wifi(QWidget, ui_wifi.Ui_WifiStatus):
    '''
    Simulation of a Wifi level widget
    '''
    lev = pyqtSignal(str, str, name='wifi_level')
    vis = pyqtSignal(str, str, name='wifi_visible')

    def __init__(self,parent):
        QWidget.__init__(self,parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.wifi.valueChanged[int].connect(self.send_level)
        self.wifiLevel.clicked[bool].connect(self.send_visible)

    @pyqtSlot(int)
    def send_level(self, value):
        if value > 70:
            self.lev.emit('wifi_level', 'Ok')
            # self.change_color('rgb(76, 175, 80)')
        elif 70 >= value > 50:
            self.lev.emit('wifi_level', 'Warn')
            # self.change_color('rgb(255, 193, 7)')
        elif value <= 50:
            self.lev.emit('wifi_level', 'Critical')
            # self.change_color('rgb(244, 67, 54)')

    @pyqtSlot(bool)
    def send_visible(self, checked):
        if checked:
            self.vis.emit('wifi_visible', 'True')
        else:
            self.vis.emit('wifi_visible', 'False')

        

def main():
    app = QtGui.QApplication(sys.argv)
    minSize = QtCore.QSize(100, 100)
    maxSize = QtCore.QSize(300, 300)
    stretch = 3
    main = Wifi(None,minSize,maxSize)
    
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()