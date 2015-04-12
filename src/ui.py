__author__ = 'Argen'

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.Qt import QWidget, QDesktopWidget, QRect

import AUIUI


class AUI(QWidget, AUIUI.Ui_UI):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.initui()

    def initui(self):
        desktop = QDesktopWidget()
        screen_size = QtCore.QRectF(desktop.screenGeometry())
        available = QtCore.QRectF(desktop.availableGeometry())
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