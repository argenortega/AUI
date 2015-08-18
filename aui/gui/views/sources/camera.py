# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 00:48:21 2014

@author: Argen
"""
import sys

from PyQt4 import QtGui
from PyQt4.QtCore import QSettings, QVariant, QMimeData, Qt, QSize
from PyQt4.QtGui import (QWidget, QSizePolicy, QApplication, QDrag, QPixmap)

from aui.gui.views.sources import ui_camera


class Camera(QWidget, ui_camera.Ui_Camera):
    """
    Simulation of a camera widget
    """
    def __init__(self, parent, num):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.num = num
        self.initui()
        settings = QSettings()
        settings.setValue("MainWindow/Size",QVariant(self.size()))
        
    def initui(self):
        self.setObjectName("C%d" % self.num)
        self.setAccessibleName("C%d" % self.num)

        self.cam.setAccessibleName("C%d" % self.num)

        if self.num == 1:
            self.cam.setText("Front Camera")
        elif self.num == 2:
            self.cam.setText("Back Camera")
        else:
            self.cam.setText("Bird's Eye Camera")


        '''
        Size of the widget
        '''
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)

    def sizeHint(self):
        return QSize(300,300)

    def heightForWidth(self, width):
        return width * 1

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
        mime_data.setText(self.cam.text())
        # mime_data.setImageData(self.currentmap)
        drag.setMimeData(mime_data)

        self.drop_action = drag.exec_(Qt.CopyAction | Qt.MoveAction)


def main():
    app = QtGui.QApplication(sys.argv)
    app.setOrganizationName("TRADR")
    #app.setOrganizationDomain("UGV OCU")
    app.setApplicationName("UGV OCU")
    cam = Camera(None, 1)
    
    cam.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()