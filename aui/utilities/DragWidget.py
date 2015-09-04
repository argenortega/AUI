#!/usr/bin/env python
#  -*- coding: utf-8 -*-
"""
Drag widget behavior
"""

__author__ = "Argentina Ortega Sainz"
__copyright__ = "Copyright (C) 2015 Argentina Ortega Sainz"
__license__ = "MIT"
__version__ = "2.0"


from PyQt4 import QtGui
from PyQt4.QtCore import Qt, QMimeData
from PyQt4.QtGui import (QWidget, QApplication, QDrag, QPixmap)
from PyQt4 import QtCore

class DView(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)

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
        # mime_data.setImageData(self.currentmap)
        drag.setMimeData(mime_data)

        self.drop_action = drag.exec_(Qt.CopyAction | Qt.MoveAction)




class DragButton(QtGui.QPushButton):
    def mousePressEvent(self, event):
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == QtCore.Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()

        super(DragButton, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            # adjust offset from clicked point to origin of widget
            currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()
            diff = globalPos - self.__mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)

            self.__mouseMovePos = globalPos

        super(DragButton, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos
            if moved.manhattanLength() > 3:
                event.ignore()
                return

        super(DragButton, self).mouseReleaseEvent(event)


def clicked():
    print "click as normal!"


if __name__ == "__main__":
    app = QtGui.QApplication([])
    w = QtGui.QWidget()
    w.resize(800, 600)

    button = DragButton("Drag", w)
    button.clicked.connect(clicked)

    w.show()
    app.exec_()
