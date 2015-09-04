#!/usr/bin/env python
#  -*- coding: utf-8 -*-
"""
Wifi Widget
"""

__author__ = "Argentina Ortega Sainz"
__copyright__ = "Copyright (C) 2015 Argentina Ortega Sainz"
__license__ = "MIT"
__version__ = "2.0"

import sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QWidget, QSizePolicy, QLabel, QHBoxLayout, QMessageBox)
from PyQt4.QtCore import pyqtSignal, pyqtSlot

from aui.gui.robot.internal import ui_wifi, ui_dialog


class Dialog(QMessageBox, ui_dialog.Ui_Dialog):
    def __init__(self):
        QMessageBox.__init__(self)
        self.setupUi(self)


class Wifi(QWidget, ui_wifi.Ui_WifiStatus):
    '''
    Simulation of a Wifi level widget
    '''
    lev = pyqtSignal(str, str, name='wifi_level')
    vis = pyqtSignal(str, str, name='wifi_visible')
    repair_signal = pyqtSignal(int, name='repair')

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.repair_signal.connect(self.wifi.setValue)
        self.repair.clicked.connect(self.repair_wifi)
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
            if value == 70:
                self.alert('Warn')
            # self.change_color('rgb(255, 193, 7)')
        elif value <= 50:
            self.lev.emit('wifi_level', 'Critical')
            if value == 50:
                self.alert('Critical')
            # self.change_color('rgb(244, 67, 54)')

    def alert(self, alert_type='Warn'):
        diag = Dialog()
        diag.setInformativeText('Return to command center to recharge?')
        diag.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        if alert_type == 'Critical':
            diag.setText('Critical Battery Level')
            diag.setIcon(QMessageBox.Critical)
            diag.setDefaultButton(QMessageBox.Yes)
        elif alert_type == 'Warn':
            diag.setText('Battery level under 70%')
            diag.setIcon(QMessageBox.Warning)
            diag.setDefaultButton(QMessageBox.No)

        if diag.exec_() == QMessageBox.Yes:
            self.repair_wifi()
        elif diag.exec_() == QMessageBox.No:
            pass

    def repair_wifi(self):
        self.repair_signal.emit(100)
        self.lev.emit('battery_level', 'Ok')

    @pyqtSlot(bool)
    def send_visible(self, checked):
        if checked:
            self.vis.emit('wifi_visible', 'True')
        else:
            self.vis.emit('wifi_visible', 'False')

    @pyqtSlot(str)
    def atomic_decision(self, decision):
        if decision == 'hide_wifi':
            print 'Wifi atomic decision'
            self.wifiLevel.setChecked(False)
            self.frame.setVisible(False)
            self.send_visible(False)
        elif decision == 'show_wifi':
            print 'Wifi atomic decision'
            self.wifiLevel.setChecked(True)
            self.frame.setVisible(True)
            self.send_visible(True)

    def get_level(self):
        if self.wifi.value() > 70:
            return 'Ok'
        elif 70 >= self.wifi.value() > 50:
            return 'Warn'
        elif self.wifi.value() <= 50:
            return 'Critical'

def main():
    app = QtGui.QApplication(sys.argv)
    minSize = QtCore.QSize(100, 100)
    maxSize = QtCore.QSize(300, 300)
    stretch = 3
    main = Wifi(None, minSize, maxSize)

    main.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
