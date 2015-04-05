__author__ = 'Argen'

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QSizePolicy, QLabel, QHBoxLayout, QFrame, QWidget)
import BatteryUI
import sys

class StatusBar(QWidget):
    def __init__(self, parent):
        print "Started"


if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    main = StatusBar(None)
    main.main()
    sys.exit(app.exec_())