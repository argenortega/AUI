#!/usr/bin/env python
#  -*- coding: utf-8 -*-
"""
Joystick Widget
"""

__author__ = "Argentina Ortega Sainz"
__copyright__ = "Copyright (C) 2015 Argentina Ortega Sainz"
__license__ = "MIT"
__version__ = "2.0"

import sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import (QSizePolicy, QWidget)

from aui.gui.robot.joystick import ui_joystick


class Joystick(QWidget, ui_joystick.Ui_joystickWidget):
    '''
    Simulation of a Joystick widget
    '''
    joystick_direction = pyqtSignal(str, str, name='joystick_direction')
    joystick_input = pyqtSignal(str, str, name='joystick_input')

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.pressUp = False
        self.pressDown = False
        self.pressLeft = False
        self.pressRight = False
        self.initUI()

    def initUI(self):
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)


        #self.sustained.setEnabled(False)
        #self.sustained.blockSignals(True)


    def keyPressEvent(self, event):
        key = event.key()


        if self.stackedWidget.currentIndex() == 0:

            if key == QtCore.Qt.Key_Left:
                if self.u.isChecked():
                    self.tl.toggle()
                    self.joystick_direction.emit('joystick_direction', 'Forward')
                elif self.d.isChecked():
                    self.dl.toggle()
                    self.joystick_direction.emit('joystick_direction', 'Backwards')
                elif self.tl.isChecked():
                    self.u.toggle()
                    self.joystick_direction.emit('joystick_direction', 'Forward')
                elif self.dl.isChecked():
                    self.d.toggle()
                    self.joystick_direction.emit('joystick_direction', 'Backwards')
                elif self.l.isChecked():
                    self.c.toggle()
                    self.joystick_direction.emit('joystick_direction', 'False')
                else:
                    self.l.toggle()
                    self.joystick_direction.emit('joystick_direction', 'LeftRight')
            elif key == QtCore.Qt.Key_Right:
                if self.u.isChecked():
                    self.tr.toggle()
                    self.joystick_direction.emit('joystick_direction', 'Forward')
                elif self.d.isChecked():
                    self.dr.toggle()
                    self.joystick_direction.emit('joystick_direction', 'Backwards')
                elif self.tr.isChecked():
                    self.u.toggle()
                    self.joystick_direction.emit('joystick_direction', 'Forward')
                elif self.dr.isChecked():
                    self.d.toggle()
                    self.joystick_direction.emit('joystick_direction', 'Backwards')
                elif self.r.isChecked():
                    self.c.toggle()
                    self.joystick_direction.emit('joystick_direction', 'False')
                else:
                    self.r.toggle()
                    self.joystick_direction.emit('joystick_direction', 'LeftRight')
            elif key == QtCore.Qt.Key_Up:
                if self.l.isChecked():
                    self.tl.toggle()
                    self.joystick_direction.emit('joystick_direction', 'Forward')
                elif self.r.isChecked():
                    self.tr.toggle()
                    self.joystick_direction.emit('joystick_direction', 'Forward')
                elif self.tl.isChecked():
                    self.l.toggle()
                    self.joystick_direction.emit('joystick_direction', 'LeftRight')
                elif self.tr.isChecked():
                    self.r.toggle()
                    self.joystick_direction.emit('joystick_direction', 'LeftRight')
                elif self.u.isChecked():
                    self.c.toggle()
                    self.joystick_direction.emit('joystick_direction', 'False')
                else:
                    self.u.toggle()
                    self.joystick_direction.emit('joystick_direction', 'Forward')
            elif key == QtCore.Qt.Key_Down:
                if self.l.isChecked():
                    self.dl.toggle()
                    self.joystick_direction.emit('joystick_direction', 'Backwards')
                elif self.r.isChecked():
                    self.dr.toggle()
                    self.joystick_direction.emit('joystick_direction', 'Backwards')
                elif self.dl.isChecked():
                    self.l.toggle()
                    self.joystick_direction.emit('joystick_direction', 'LeftRight')
                elif self.dr.isChecked():
                    self.r.toggle()
                    self.joystick_direction.emit('joystick_direction', 'LeftRight')
                elif self.d.isChecked():
                    self.c.toggle()
                    self.joystick_direction.emit('joystick_direction', 'False')
                else:
                    self.d.toggle()
                    self.joystick_direction.emit('joystick_direction', 'Backwards')
        else:

            if not self.pressLeft and key == QtCore.Qt.Key_Left:
                self.left.setStyleSheet('border: 2px solid green; color: green')
                self.center.setStyleSheet('color: black')
                self.pressLeft = True
                self.joystick_direction.emit('joystick_direction', 'LeftRight')
            elif not self.pressUp and key == QtCore.Qt.Key_Up:
                self.up.setStyleSheet('border: 2px solid green; color: green')
                self.center.setStyleSheet('color: black')
                self.pressUp = True
                self.joystick_direction.emit('joystick_direction', 'Forward')
            elif not self.pressRight and key == QtCore.Qt.Key_Right:
                self.right.setStyleSheet('border: 2px solid green; color: green')
                self.center.setStyleSheet('color: black')
                self.pressRight = True
                self.joystick_direction.emit('joystick_direction', 'LeftRight')
            elif not self.pressDown and key == QtCore.Qt.Key_Down:
                self.down.setStyleSheet('border: 2px solid green; color: green')
                self.center.setStyleSheet('color: black')
                self.pressDown = True
                self.joystick_direction.emit('joystick_direction', 'Backwards')
            elif self.pressDown and self.pressLeft:
                self.downleft.setStyleSheet('border: 2px solid green; color: green')
                self.center.setStyleSheet('color: black')
                self.down.setStyleSheet('color: black')
                self.left.setStyleSheet('color: black')
                self.joystick_direction.emit('joystick_direction', 'Backwards')
            elif self.pressUp and self.pressLeft:
                self.topleft.setStyleSheet('border: 2px solid green; color: green')
                self.center.setStyleSheet('color: black')
                self.up.setStyleSheet('color: black')
                self.left.setStyleSheet('color: black')
                self.joystick_direction.emit('joystick_direction', 'Forward')
            elif self.pressDown and self.pressRight:
                self.downright.setStyleSheet('border: 2px solid green; color: green')
                self.center.setStyleSheet('color: black')
                self.down.setStyleSheet('color: black')
                self.right.setStyleSheet('color: black')
                self.joystick_direction.emit('joystick_direction', 'Backwards')
            elif self.pressUp and self.pressRight:
                self.topright.setStyleSheet('border: 2px solid green; color: green')
                self.center.setStyleSheet('color: black')
                self.up.setStyleSheet('color: black')
                self.right.setStyleSheet('color: black')
                self.joystick_direction.emit('joystick_direction', 'Forward')
                # else:
                # self.center.setStyleSheet('border: 2px solid green; color: green')

    def keyReleaseEvent(self, event):
        if self.stackedWidget.currentIndex() == 1:
            key = event.key()
            if key == QtCore.Qt.Key_Left:
                self.left.setStyleSheet('color: black')
                self.topleft.setStyleSheet('color: black')
                self.downleft.setStyleSheet('color: black')
                self.center.setStyleSheet('border: 2px solid green; color: green')
                self.pressLeft = False
            elif key == QtCore.Qt.Key_Up:
                self.up.setStyleSheet('color: black')
                self.topleft.setStyleSheet('color: black')
                self.topright.setStyleSheet('color: black')
                self.center.setStyleSheet('border: 2px solid green; color: green')
                self.pressUp = False
            elif key == QtCore.Qt.Key_Right:
                self.right.setStyleSheet('color: black')
                self.downright.setStyleSheet('color: black')
                self.topright.setStyleSheet('color: black')
                self.center.setStyleSheet('border: 2px solid green; color: green')
                self.pressRight = False
            elif key == QtCore.Qt.Key_Down:
                self.down.setStyleSheet('color: black')
                self.downleft.setStyleSheet('color: black')
                self.downright.setStyleSheet('color: black')
                self.center.setStyleSheet('border: 2px solid green; color: green')
                self.pressDown = False
            else:
                self.joystick_direction.emit('joystick_direction', 'False')
                self.center.setStyleSheet('border: 2px solid green; color: green')
                # else:
                #   QWidget.keyReleaseEvent(self,event)


def main():
    app = QtGui.QApplication(sys.argv)
    minSize = QtCore.QSize(250, 250)
    maxSize = QtCore.QSize(300, 300)
    main = Joystick(None)

    main.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
