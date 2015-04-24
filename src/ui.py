__author__ = 'Argen'

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.Qt import QWidget, QDesktopWidget, QMainWindow

import AUIUI


class AUI(QMainWindow, AUIUI.Ui_MainWin):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.initui()
        self.showMaximized()

    def initui(self):
        desktop = QDesktopWidget()
        screen_size = QtCore.QRect(desktop.screenGeometry())
        available = QtCore.QRect(desktop.availableGeometry())

        screen_text = 'Screen Geometry\nHeight: %f\tWidth: %f\n'%(screen_size.height(),screen_size.width())
        available_text = 'Available Geometry\nHeight: %f\tWidth: %f'%(available.height(),available.width())

        self.label.setText(screen_text+available_text)




def main():

    app = QtGui.QApplication(sys.argv)
    main = AUI(None)
    main.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()