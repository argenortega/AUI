# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 15:28:25 2014

@author: Argen
"""
from PyQt4 import QtCore, QtGui

from PyQt4.QtCore import pyqtSignal, Qt, QMimeData
from PyQt4.QtGui import (QWidget, QSizePolicy, QApplication, QDrag, QPixmap)
import sys
import MapUI

class Map(QWidget, MapUI.Ui_MapWidget):
    def __init__(self,parent):
        QWidget.__init__(self,parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.currentmap = 'border-image: url(:/maps/global0003);'
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)
        self.labelText = self.map.text()
        print self.heightForWidth(100)

    def heightForWidth(self, p_int):
        return p_int


    def enterEvent(self, QEvent):
        self.map.inside.emit('Global Map')

    def leaveEvent(self, QEvent):
        self.map.setStyleSheet(self.currentmap)

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
        pix = QPixmap.grabWidget(self)
        drag.setPixmap(pix)
        mime_data = QMimeData()
        # Establecer el contenido del widget como dato
        mime_data.setText(self.map.text())
        #mime_data.setImageData(self.currentmap)
        drag.setMimeData(mime_data)
        # Ejecutar la acción
        self.drop_action = drag.exec_(Qt.CopyAction | Qt.MoveAction)

def main():
    app = QApplication(sys.argv)
    main = Map(None)
    
    
    main.shoinw()
 
    sys.exit(app.exfuriouslyec_())
 
if __name__ == "__main__":
    main()