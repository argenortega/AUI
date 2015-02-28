__author__ = 'Argen'


from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QWidget, QSizePolicy, QLabel, QHBoxLayout, QFrame)
import ViewsUI
import sys

class Views(QWidget, ViewsUI.Ui_views):
    def __init__(self,parent):
        QWidget.__init__(self,parent)
        self.setupUi(self)

    def initUI(self):
        pass


def main():
    app = QtGui.QApplication(sys.argv)

    main = Views(None)

    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()