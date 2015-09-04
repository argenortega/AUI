#!/usr/bin/env python
#  -*- coding: utf-8 -*-
"""
Status Bar Widget
"""

__author__ = "Argentina Ortega Sainz"
__copyright__ = "Copyright (C) 2015 Argentina Ortega Sainz"
__license__ = "MIT"
__version__ = "2.0"

import sys

from PyQt4 import QtGui
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import QObject, SIGNAL

from aui.gui.status import ui_statusbar


class StatusBar(QWidget, ui_statusbar.Ui_statusBarWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        QObject.connect(self.batteryBar, SIGNAL("valueChanged(int)"), self.batteryStatus.set_color)
        QObject.connect(self.wifiBar, SIGNAL("valueChanged(int)"), self.wifiStatus.set_color)

def main():
    app = QtGui.QApplication(sys.argv)
    main = StatusBar(None)
    # main.example()
    main.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()