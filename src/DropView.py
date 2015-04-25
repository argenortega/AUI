__author__ = 'Argen'

from PyQt4 import QtCore, QtGui

from PyQt4.QtCore import pyqtSignal, Qt, QMimeData
from PyQt4.QtGui import (QFrame, QSizePolicy, QApplication, QDrag)
import sys
import MapUI


class DView(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self, parent)
        self.setAcceptDrops(True)  # Aceptar objetos
        self.setStyleSheet("background-color: #E6E6E6;")
    def dragEnterEvent(self, event):
        # Ignorar objetos arrastrados sin informacion
        if event.mimeData().hasText():
            event.acceptProposedAction()
    def dropEvent(self, event):
        # Establecer el widget en una nueva posicion
        pos = event.pos()
        self.wid = event.source()
        self.wid.setParent(self)
        #self.wid.setGeometry(pos.x(), pos.y(), 150, 20)
        #self.wid.setGeometry()
        self.layout().addWidget(self.wid)
        event.acceptProposedAction()

        if self.parent().objectName() == 'currentViews':
            print 'Current Views'
            minSize = QtCore.QSize(100, 100)
            maxSize = QtCore.QSize(16777215, 16777215)
            #stretch = 1

            self.wid.setMaximumSize(maxSize)
            self.wid.setMinimumSize(minSize)
            #self.wid.maximize()
            self.wid.resize(16777215, 16777215)
        elif self.parent().objectName() == 'viewsGroup':
            print 'Available Views'
            minSize = QtCore.QSize(50, 50)
            maxSize = QtCore.QSize(70, 70)
            self.wid.setMaximumSize(maxSize)
            self.wid.setMinimumSize(minSize)
            self.wid.resize(70, 70)

        self.wid.show()

        print self.objectName()
        print self.children()
