__author__ = 'Argen'

import sys

from PyQt4 import QtGui
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import  pyqtSignal, pyqtSlot

from aui.gui.views import ui_views


class MainViews(QWidget, ui_views.Ui_viewsWidget):
    vis = pyqtSignal(str, str, name='AV_visible')

    def __init__(self,parent):
        QWidget.__init__(self,parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        #self.pushButton.clicked[bool].connect(self.press)
        self.hor.clicked[bool].connect(self.horizontalView)
        self.vert.clicked[bool].connect(self.verticalView)
        self.four.clicked[bool].connect(self.fourViews)
        self.horizontalView()
        self.viewsGroup.clicked[bool].connect(self.send_visible)


    def horizontalView(self):
        self.bright.setVisible(False)
        self.tright.setVisible(False)
        self.bleft.setVisible(True)
        self.tleft.setVisible(True)

    def verticalView(self):
        self.bright.setVisible(False)
        self.bleft.setVisible(False)
        self.tright.setVisible(True)
        self.tleft.setVisible(True)

    def fourViews(self):
        self.bright.setVisible(True)
        self.tright.setVisible(True)
        self.tleft.setVisible(True)
        self.bleft.setVisible(True)

    def press(self,toggled):
        if toggled:
            self.pushButton.setText("+")
            self.availableViews.setVisible(False)
            #children = self.findChildren(QtGui.QLabel)
            #for child in children:
                #child.setVisible(False)
        else:
            self.pushButton.setText("-")
            self.availableViews.setVisible(True)
            #children = self.findChildren(QtGui.QLabel)
            #for child in children:
                #child.setVisible(True)

    @pyqtSlot(bool)
    def send_visible(self, checked):
        if checked:
            self.vis.emit('AV_visible', 'True')
        else:
            self.vis.emit('AV_visible', 'False')



def main():
    app = QtGui.QApplication(sys.argv)

    main = MainViews(None)

    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()