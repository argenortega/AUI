__author__ = 'Argen'

from PyQt4 import QtGui
from PyQt4.QtGui import QWidget
import StatusBarUI
import sys

class StatusBar(QWidget, StatusBarUI.Ui_statusBarWidget):
    def __init__(self, parent):
        #print "Started"
        QWidget.__init__(self, parent)
        self.setupUi(self)



def main():
    app = QtGui.QApplication(sys.argv)
    main = StatusBar(None)
    main.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()