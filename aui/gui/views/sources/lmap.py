# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 15:28:54 2014

@author: Argen
"""

import sys

from PyQt4.QtCore import pyqtSignal, Qt, QMimeData
from PyQt4.QtGui import (QWidget, QSizePolicy, QApplication, QDrag, QPixmap)

from aui.gui.views.sources import ui_lmap
#from aui.utilities.DragWidget import DView

class LocalMap(QWidget, ui_lmap.Ui_NewView):
    '''
    Simulation of an additional view widget
    '''
    inside = pyqtSignal(str)

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setObjectName("LM")
        self.currentmap = 'border-image: url(:/maps/local/local1);'
        self.map.setStyleSheet(self.currentmap)

        '''
        Size of the widget
        '''
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons() and Qt.LeftButton):
            return

        if ((event.pos() - self.drag_start_position).manhattanLength()
                < QApplication.startDragDistance()):
            return

        drag = QDrag(self)
        pix = QPixmap.grabWidget(self)
        drag.setPixmap(pix)
        mime_data = QMimeData()
        mime_data.setText(self.map.text())
        #mime_data.setImageData(self.currentmap)
        drag.setMimeData(mime_data)

        self.drop_action = drag.exec_(Qt.CopyAction | Qt.MoveAction)


def main():
    app = QApplication(sys.argv)
    main = LocalMap(None)
    main.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
