__author__ = 'Argen'


from PyQt4 import QtGui, QtCore
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
        self.hor.clicked[bool].connect(self.horizontalView)
        self.vert.clicked[bool].connect(self.verticalView)
        self.four.clicked[bool].connect(self.fourViews)
        self.horizontalView()


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

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('application/x-Map'):
            if event.source() in self.children():
                event.setDropAction(QtCore.Qt.MoveAction)
                event.accept()
            else:
                event.acceptProposedAction()
        elif event.mimeData().hasText():
            event.acceptProposedAction()
        else:
            event.ignore()

    dragMoveEvent = dragEnterEvent


def main():
    app = QtGui.QApplication(sys.argv)

    main = Views(None)

    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()