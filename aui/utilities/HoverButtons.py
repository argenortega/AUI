#!/usr/bin/env python
#  -*- coding: utf-8 -*-
"""
Hover Buttons. Deprecated and replaced by use of stylesheets
"""

__author__ = "Argentina Ortega Sainz"
__copyright__ = "Copyright (C) 2015 Argentina Ortega Sainz"
__license__ = "MIT"
__version__ = "2.0"

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QPushButton, QSizePolicy, QLabel, QVBoxLayout, QFrame,
                         QApplication, QGroupBox, QFont, QGridLayout,
                         QWidget)
from PyQt4.QtCore import (QEvent, QString, QTimer, Qt)
import sys


class HButton (QPushButton):
    def __init__(self, parent):
        QPushButton.__init__(self, parent)


    def enterEvent(self, QEvent):
        self.setStyleSheet('border: 2px solid rgb(0, 128, 255);')

    def leaveEvent(self, QEvent):
        self.setStyleSheet('color: black')