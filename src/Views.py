__author__ = 'Argen'


from PyQt4 import QtGui
from PyQt4.QtGui import QWidget
import ViewsUI
import sys

class Views(QWidget, ViewsUI.Ui_viewsWidget):
    def __init__(self,parent):
        QWidget.__init__(self,parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked[bool].connect(self.press)


    def press(self,toggled):
        if toggled:
            self.pushButton.setText("+")
            children = self.findChildren(QtGui.QLabel)
            for child in children:
                child.setVisible(False)
        else:
            self.pushButton.setText("-")
            children = self.findChildren(QtGui.QLabel)
            for child in children:
                child.setVisible(True)


def main():
    app = QtGui.QApplication(sys.argv)

    main = Views(None)

    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()