#!/usr/bin/env python
#  -*- coding: utf-8 -*-
"""
Battery Widget
"""

__author__ = "Argentina Ortega Sainz"
__copyright__ = "Copyright (C) 2015 Argentina Ortega Sainz"
__license__ = "MIT"
__version__ = "2.0"

import sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QWidget, QDialog, QMessageBox)
from PyQt4.QtCore import pyqtSignal, pyqtSlot

from aui.gui.robot.internal import ui_battery, ui_dialog


class Dialog(QMessageBox, ui_dialog.Ui_Dialog):
    def __init__(self):
        QMessageBox.__init__(self)
        self.setupUi(self)


class Battery(QWidget, ui_battery.Ui_batteryStatus):
    '''
    Simulation of a Battery level widget
    '''
    lev = pyqtSignal(str, str, name='battery_level')
    vis = pyqtSignal(str, str, name='battery_visible')
    recharge_signal = pyqtSignal(int, name='recharge')

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.initUI()
        self.charge.clicked.connect(self.recharge)
        self.recharge_signal.connect(self.battery.setValue)
        #self.battery.setValue(30)

    def initUI(self):
        self.battery.valueChanged[int].connect(self.send_level)
        self.batteryLevel.clicked[bool].connect(self.send_visible)

    @pyqtSlot(int)
    def send_level(self, value):
        if value > 70:
            self.lev.emit('battery_level', 'Ok')
        elif 70 >= value > 50:
            self.lev.emit('battery_level', 'Warn')
            if value == 70:
                self.alert('Warn')
        elif value <= 50:
            self.lev.emit('battery_level', 'Critical')
            if value == 50:
                self.alert('Critical')

    def alert(self, alert_type='Warn'):
        diag = Dialog()
        diag.setInformativeText('Return to command center to recharge?')
        diag.setStandardButtons(QMessageBox.Yes|QMessageBox.No)

        if alert_type == 'Critical':
            diag.setText('Critical Battery Level')
            diag.setIcon(QMessageBox.Critical)
            diag.setDefaultButton(QMessageBox.Yes)
        elif alert_type == 'Warn':
            diag.setText('Battery level under 70%')
            diag.setIcon(QMessageBox.Warning)
            diag.setDefaultButton(QMessageBox.No)


        if diag.exec_() == QMessageBox.Yes:
            self.recharge()
        elif diag.exec_() == QMessageBox.No:
            pass

    def recharge(self):
        self.recharge_signal.emit(100)
        self.lev.emit('battery_level', 'Ok')

    @pyqtSlot(bool)
    def send_visible(self, checked):
        if checked:
            self.vis.emit('battery_visible', 'True')
        else:
            self.vis.emit('battery_visible', 'False')

    @pyqtSlot(str)
    def atomic_decision(self, decision):
        if decision == 'hide_battery':
            print 'Battery atomic decision'
            self.batteryLevel.setChecked(False)
            self.frame.setVisible(False)
            self.send_visible(False)
        elif decision == 'show_battery':
            print 'Battery atomic decision'
            self.batteryLevel.setChecked(True)
            self.frame.setVisible(True)
            self.send_visible(True)

    def get_level(self):
        if self.battery.value() > 70:
            return 'Ok'
        elif 70 >= self.battery.value() > 50:
            return 'Warn'
        elif self.battery.value() <= 50:
            return 'Critical'


def main():
    app = QtGui.QApplication(sys.argv)
    main = Battery(None)

    main.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
