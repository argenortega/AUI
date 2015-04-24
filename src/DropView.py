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
        self.label = event.source()
        self.label.setParent(self)
        self.label.setGeometry(pos.x(), pos.y(), 150, 20)
        self.label.show()
        event.acceptProposedAction()