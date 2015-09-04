#!/usr/bin/env python
#  -*- coding: utf-8 -*-
"""
Snapshots Widget
"""

__author__ = "Argentina Ortega Sainz"
__copyright__ = "Copyright (C) 2015 Argentina Ortega Sainz"
__license__ = "MIT"
__version__ = "2.0"

import sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QSizePolicy, QFrame
from PyQt4.QtCore import QSize, pyqtSignal, pyqtSlot

from aui.gui.snapshots import ui_snapshot


class Screenshots(QWidget, ui_snapshot.Ui_ScreenshotWidget):
    vis = pyqtSignal(str, str, name='AS_visible')

    def __init__(self,parent):
        QWidget.__init__(self,parent)
        self.normal_stretch = 4
        self.priority_stretch = 8

        self.setupUi(self)
        self.num = 4
        self.initUI()
        
    def initUI(self):
        # self.newS.clicked.connect(self.add_new)

        # self.showB.clicked[bool].connect(self.press)
        self.extraScreenGroup.clicked[bool].connect(self.send_visible)


    @pyqtSlot(str)
    def setScreenshot(self,s):
        self.currentScreenshot.setText(s)

    @pyqtSlot(bool)
    def send_visible(self, checked):
        if checked:
            self.vis.emit('AS_visible', 'True')
        else:
            self.vis.emit('AS_visible', 'False')

    @pyqtSlot(str)
    def atomic_decision(self, decision):
        if decision == 'hide_AS':
            print 'Atomic decision: %s' % decision
            self.extraScreenGroup.setChecked(False)
            self.scrollArea.setVisible(False)
            self.send_visible(False)
        elif decision == 'show_AS':
            print 'Atomic decision: %s' % decision
            self.extraScreenGroup.setChecked(True)
            self.scrollArea.setVisible(True)
            self.send_visible(True)
        elif decision == 'increase':
            print 'Atomic decision: %s' % decision
            sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            sizePolicy.setHeightForWidth(True)
            sizePolicy.setHorizontalStretch(self.priority_stretch)
            sizePolicy.setVerticalStretch(self.priority_stretch)
            self.setSizePolicy(sizePolicy)
            #self.currentScreenshot.resize(16777215, 16777215)
            self.updateGeometry()
            print 'Expanding'
        elif decision == 'decrease':
            print 'Atomic decision: %s' % decision
            sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            sizePolicy.setHeightForWidth(True)
            sizePolicy.setHorizontalStretch(self.normal_stretch)
            sizePolicy.setVerticalStretch(self.normal_stretch)
            self.setSizePolicy(sizePolicy)
            #self.currentScreenshot.resize(0,0)
            self.updateGeometry()
        elif decision in ['minimum', 'mapping', 'navigation', 'exploring', 'minimum_C2', 'navigation_C2',
                          'mapping_C2', 'exploring_C2', 'minimum_C2', 'navigation_C1C2' ]:
            sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            sizePolicy.setHeightForWidth(True)
            sizePolicy.setHorizontalStretch(self.normal_stretch)
            sizePolicy.setVerticalStretch(self.normal_stretch)
            self.setSizePolicy(sizePolicy)
            self.updateGeometry()

    
def main():
    app = QtGui.QApplication(sys.argv)
    minSize = QtCore.QSize(350, 350)
    maxSize = QtCore.QSize(400, 400)
    stretch = 1
    main = Screenshots(None)
    
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()