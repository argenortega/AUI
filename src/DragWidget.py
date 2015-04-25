__author__ = 'Argen'


from PyQt4 import QtCore, QtGui

from PyQt4.QtCore import pyqtSignal, Qt, QMimeData
from PyQt4.QtGui import (QWidget, QSizePolicy, QApplication, QDrag)
import sys
import MapUI


class DView(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        # Chequear que se esté presionando el botón derecho
        if not (event.buttons() and Qt.LeftButton):
            return
        # Verificar que sea una posición válida
        if ((event.pos() - self.drag_start_position).manhattanLength()
            < QApplication.startDragDistance()):
            return
        drag = QDrag(self)
        mime_data = QMimeData()
        # Establecer el contenido del widget como dato
        mime_data.setText(self.map.text())
        #mime_data.setImageData(self.currentmap)
        drag.setMimeData(mime_data)
        # Ejecutar la acción
        self.drop_action = drag.exec_(Qt.CopyAction | Qt.MoveAction)
