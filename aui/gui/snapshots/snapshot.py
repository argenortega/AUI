# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 17:21:56 2014

@author: Argen
"""

import sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QSizePolicy, QFrame
from PyQt4.QtCore import QSize, pyqtSignal, pyqtSlot

from aui.gui.snapshots import ui_snapshot
#import ActiveLabel


class Screenshots(QWidget, ui_snapshot.Ui_ScreenshotWidget):
    vis = pyqtSignal(str, str, name='AS_visible')

    def __init__(self,parent):
        QWidget.__init__(self,parent)
        self.setupUi(self)
        self.num = 4
        self.initUI()
        
    def initUI(self):
        # self.newS.clicked.connect(self.add_new)

        # self.showB.clicked[bool].connect(self.press)

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHeightForWidth(False)
        self.scrollArea.setSizePolicy(sizePolicy)
        
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(False)
        self.setSizePolicy(sizePolicy)

        self.extraScreenGroup.clicked[bool].connect(self.send_visible)


    @pyqtSlot(str)
    def setScreenshot(self,s):
        self.currentScreenshot.setText(s)

    @pyqtSlot(bool)
    def send_visible(self, checked):
        if checked:
            self.vis.emit('AS_visible', 'True')
        else:
            self.vis.emit('AS_visible', 'False')
        
        
    
def main():
    app = QtGui.QApplication(sys.argv)
    minSize = QtCore.QSize(350, 350)
    maxSize = QtCore.QSize(400, 400)
    stretch = 1
    main = Screenshots(None)
    
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()