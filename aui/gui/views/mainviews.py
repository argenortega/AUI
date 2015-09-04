#!/usr/bin/env python
#  -*- coding: utf-8 -*-
"""
Main Views Widget
"""

__author__ = "Argentina Ortega Sainz"
__copyright__ = "Copyright (C) 2015 Argentina Ortega Sainz"
__license__ = "MIT"
__version__ = "2.0"

import sys

from PyQt4 import QtGui
from PyQt4.QtGui import QWidget, QSizePolicy
from PyQt4.QtCore import  pyqtSignal, pyqtSlot

from aui.gui.views import ui_views
from .sources import camera, gmap, lmap, pointcloud


class MainViews(QWidget, ui_views.Ui_viewsWidget):
    vis = pyqtSignal(str, str, name='AV_visible')

    def __init__(self,parent):
        QWidget.__init__(self,parent)
        self.normal_stretch = 6
        self.priority_stretch = 8
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.hor.clicked[bool].connect(self.horizontalView)
        self.vert.clicked[bool].connect(self.verticalView)
        self.four.clicked[bool].connect(self.fourViews)
        self.horizontalView()
        self.viewsGroup.clicked[bool].connect(self.send_visible)

        self.pointcloud = pointcloud.Pointcloud(self.availableViews)
        self.availableViewsLayout.addWidget(self.pointcloud)

        self.globalmap = gmap.GlobalMap(self.availableViews)
        self.availableViewsLayout.addWidget(self.globalmap)

        self.localmap = lmap.LocalMap(self.availableViews)
        self.availableViewsLayout.addWidget(self.localmap)

        self.camera1 = camera.Camera(self.tleft, 1)
        self.tleftLayout.addWidget(self.camera1)
        self.tleftLabel.setVisible(False)

        self.camera2 = camera.Camera(self.bleft, 2)
        self.bleftLayout.addWidget(self.camera2)
        self.bleftLabel.setVisible(False)

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

    @pyqtSlot(bool)
    def send_visible(self, checked):
        if checked:
            self.vis.emit('AV_visible', 'True')
        else:
            self.vis.emit('AV_visible', 'False')

    @pyqtSlot(str)
    def atomic_decision(self, decision):
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(self.normal_stretch)
        sizePolicy.setVerticalStretch(self.normal_stretch)
        self.setSizePolicy(sizePolicy)

        viewPolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        viewPolicy.setHeightForWidth(True)
        viewPolicy.setHorizontalStretch(self.normal_stretch)
        viewPolicy.setVerticalStretch(self.normal_stretch)
        self.camera1.setSizePolicy(viewPolicy)
        self.camera2.setSizePolicy(viewPolicy)
        self.globalmap.setSizePolicy(viewPolicy)
        self.localmap.setSizePolicy(viewPolicy)
        self.pointcloud.setSizePolicy(viewPolicy)


        if decision == 'hide_AV':
            print 'Atomic action: %s'%decision
            self.viewsGroup.setChecked(False)
            self.availableViews.setVisible(False)
            self.send_visible(False)
        elif decision == 'show_AV':
            print 'Atomic action: %s'%decision
            self.viewsGroup.setChecked(True)
            self.availableViews.setVisible(True)
            self.send_visible(True)
        elif decision == 'content':
            sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            sizePolicy.setHeightForWidth(True)
            sizePolicy.setHorizontalStretch(4)
            sizePolicy.setVerticalStretch(4)
            print 'Suggested content'
            #self.currentScreenshot.setSizePolicy(sizePolicy)
        elif decision == 'priority':
            sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            sizePolicy.setHeightForWidth(True)
            sizePolicy.setHorizontalStretch(4)
            sizePolicy.setVerticalStretch(4)
            style = 'border-color: rgb(51, 94, 242);border-radius: 6px; border-width: 3px; border-style: solid;'
            #self.currentScreenshot.setSizePolicy(sizePolicy)
            print 'Prioritize content'
        elif decision == 'widget_content':
            print 'Atomic action: %s'%decision
        elif decision == 'add_C1':
            self.tleft.add_widget(self.camera1)
        elif decision == 'add_C2':
            self.bleft.add_widget(self.camera2)
        elif decision == 'add_LM':
            self.tleft.add_widget(self.localmap)
        elif decision == 'add_GM':
            self.bleft.add_widget(self.globalmap)
        elif decision == 'add_PC':
            self.bleft.add_widget(self.pointcloud)
        elif decision == 'remove_C2':
            self.availableViews.add_widget(self.camera2)
        elif decision == 'remove_GM':
            self.availableViews.add_widget(self.globalmap)
        elif decision == 'remove_PC':
            self.availableViews.add_widget(self.pointcloud)
        elif decision == 'minimum':
            self.camera1.cam.attention()
            self.localmap.map.attention()
        elif decision == 'mapping':
            sizePolicy.setHorizontalStretch(self.priority_stretch)
            sizePolicy.setVerticalStretch(self.priority_stretch)
            self.setSizePolicy(sizePolicy)

            self.camera1.cam.attention()
            self.localmap.map.attention()
            self.pointcloud.pointcloud.attention()

            viewPolicy.setHorizontalStretch(self.priority_stretch)
            viewPolicy.setVerticalStretch(self.priority_stretch)
            self.pointcloud.setSizePolicy(sizePolicy)
        elif decision == 'exploring':
            sizePolicy.setHorizontalStretch(self.priority_stretch)
            sizePolicy.setVerticalStretch(self.priority_stretch)
            self.setSizePolicy(sizePolicy)

            self.camera1.cam.attention()
            self.localmap.map.attention()
            self.globalmap.map.attention()

            viewPolicy.setHorizontalStretch(self.priority_stretch)
            viewPolicy.setVerticalStretch(self.priority_stretch)
            self.localmap.setSizePolicy(sizePolicy)
        elif decision == 'navigation':
            sizePolicy.setHorizontalStretch(self.priority_stretch)
            sizePolicy.setVerticalStretch(self.priority_stretch)
            self.setSizePolicy(sizePolicy)

            self.camera1.cam.attention()
            self.localmap.map.attention()
            self.camera2.cam.attention()

            viewPolicy.setHorizontalStretch(self.priority_stretch)
            viewPolicy.setVerticalStretch(self.priority_stretch)
            self.camera1.setSizePolicy(sizePolicy)
        elif decision == 'minimum_C2':
            self.camera1.cam.attention()
            self.localmap.map.attention()
            self.camera2.cam.attention()

        elif decision == 'mapping_C2':
            sizePolicy.setHorizontalStretch(self.priority_stretch)
            sizePolicy.setVerticalStretch(self.priority_stretch)
            self.setSizePolicy(sizePolicy)

            self.camera1.cam.attention()
            self.localmap.map.attention()
            self.camera2.cam.attention()
            self.pointcloud.pointcloud.attention()

            viewPolicy.setHorizontalStretch(self.priority_stretch)
            viewPolicy.setVerticalStretch(self.priority_stretch)
            self.pointcloud.setSizePolicy(sizePolicy)
        elif decision == 'exploring_C2':
            sizePolicy.setHorizontalStretch(self.priority_stretch)
            sizePolicy.setVerticalStretch(self.priority_stretch)
            self.setSizePolicy(sizePolicy)

            self.camera1.cam.attention()
            self.localmap.map.attention()
            self.camera2.cam.attention()
            self.globalmap.map.attention()

            viewPolicy.setHorizontalStretch(self.priority_stretch)
            viewPolicy.setVerticalStretch(self.priority_stretch)
            self.localmap.setSizePolicy(sizePolicy)
        elif decision == 'navigation_C2':
            sizePolicy.setHorizontalStretch(self.priority_stretch)
            sizePolicy.setVerticalStretch(self.priority_stretch)
            self.setSizePolicy(sizePolicy)

            self.camera1.cam.attention()
            self.localmap.map.attention()
            self.camera2.cam.attention()

            viewPolicy.setHorizontalStretch(self.priority_stretch)
            viewPolicy.setVerticalStretch(self.priority_stretch)
            self.camera2.setSizePolicy(sizePolicy)
        elif decision == 'navigation_C1C2':
            sizePolicy.setHorizontalStretch(self.priority_stretch)
            sizePolicy.setVerticalStretch(self.priority_stretch)
            self.setSizePolicy(sizePolicy)

            self.camera1.cam.attention()
            self.localmap.map.attention()
            self.camera2.cam.attention()

            viewPolicy.setHorizontalStretch(self.priority_stretch)
            viewPolicy.setVerticalStretch(self.priority_stretch)
            self.camera1.setSizePolicy(sizePolicy)
            self.camera2.setSizePolicy(sizePolicy)


def main():
    app = QtGui.QApplication(sys.argv)

    main = MainViews(None)

    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()