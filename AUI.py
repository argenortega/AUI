# -*- coding: utf-8 -*-
"""
Created on Sat Dec 27 02:57:21 2014

@author: Argentina Ortega Sáinz
@version: 0.0.2
"""
import sys
import os

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import (QMainWindow, QHBoxLayout, QVBoxLayout)

from aui.gui.views.sources import camera, lmap, gmap, pointcloud
from aui.gui.robot.internal import battery, wifi
from aui.gui.robot.joystick import joystick
from aui.gui.snapshots import snapshot, image
from aui.gui.views import mainviews
from aui.gui.status import statusbar
from aui.mi import mixed_initative
from aui.mi import parameters

import ui_aui

# from PyQt4.uic import loadUi

class AUI(QMainWindow, ui_aui.Ui_MainWin):
    """
    Adaptive User Interface for TRADR project
    """
    closing = pyqtSignal()

    def __init__(self, parent=None):
        super(AUI, self).__init__()
        self.sc_num = 0
        self.evidence = {}
        self.setupUi(self)
        self.initUI()
        self.closing.connect(self.mixedInitiative.close)

    def initUI(self):
        # self.setGeometry(0, 0, 1280, 800)
        self.setWindowTitle("Adaptive TRADR OCU")
        self.setMouseTracking(True)

        self.label.setVisible(False)

        '''
        Layout Definitions for the complete AUI
        '''
        # Global Layout for AUI Parameters + TRADR gui
        self.MainLayout = QVBoxLayout()
        self.MainLayout.setObjectName("MainLayout")
        self.globalLayout.addLayout(self.MainLayout)

        self.GUILayout = QHBoxLayout()
        self.GUILayout.setObjectName("GUILayout")
        self.GUILayout.setMargin(3)

        self.ViewsLayout = QVBoxLayout()
        self.ViewsLayout.setObjectName("ViewsLayout")

        self.ScreenshotLayout = QVBoxLayout()
        self.ScreenshotLayout.setObjectName("ScreenshotLayout")

        self.StatusLayout = QVBoxLayout()
        self.StatusLayout.setObjectName("StatusLayout")

        '''
        Widgets
        '''
        self.statusBar = statusbar.StatusBar(self)
        self.MainLayout.addWidget(self.statusBar)

        self.mixedInitiative = mixed_initative.MixedInitiative(self)
        self.MainLayout.addWidget(self.mixedInitiative)

        self.MainLayout.addLayout(self.GUILayout)

        self.views = mainviews.MainViews(self)
        self.pointcloud = pointcloud.Pointcloud(self)
        self.pointcloud.setParent(self.views)
        self.views.availableViewsLayout.addWidget(self.pointcloud)

        self.map = gmap.GlobalMap(self)
        self.map.setParent(self.views)
        self.views.availableViewsLayout.addWidget(self.map)

        self.extra = lmap.LocalMap(self)
        self.extra.setParent(self.views)
        self.views.availableViewsLayout.addWidget(self.extra)

        self.Camera1 = camera.Camera(self, 1)
        self.views.tleftLayout.addWidget(self.Camera1)
        self.views.tleftLabel.setVisible(False)

        self.Camera2 = camera.Camera(self, 2)
        self.Camera2.setMinimumSize(QtCore.QSize(80, 80))
        self.views.bleftLayout.addWidget(self.Camera2)
        self.views.bleftLabel.setVisible(False)

        self.GUILayout.addWidget(self.views)

        self.Screenshots = snapshot.Screenshots(self)
        self.GUILayout.addWidget(self.Screenshots)

        self.battery = battery.Battery(self)
        self.wifi = wifi.Wifi(self)
        self.joystick = joystick.Joystick(self)

        self.StatusLayout.addWidget(self.battery)
        self.StatusLayout.addWidget(self.wifi)
        self.StatusLayout.addStretch()
        self.StatusLayout.addWidget(self.joystick)

        self.GUILayout.addLayout(self.StatusLayout)

        self.parameters = parameters.AUIParameters(self)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.parameters)

        for i in xrange(4):
            self.new_screenshot()

        '''
        Connect internal widgets
        '''
        self.mixedInitiative.AUItoggleButton.clicked[bool].connect(self.AUIupdate)
        self.statusBar.adaptiveStatus.clicked[bool].connect(self.AUIupdate)
        self.AUIupdate()
        # QtCore.QObject.connect(self.parameters.wifiSlider, QtCore.SIGNAL("valueChanged(int)"), self.wifi.value.setNum)
        # QtCore.QObject.connect(self.parameters.batterySlider, QtCore.SIGNAL("valueChanged(int)"),
                               #self.battery.value.setNum)
        QtCore.QObject.connect(self.parameters.batterySlider, QtCore.SIGNAL("valueChanged(int)"),
                               self.battery.battery.setValue)
        QtCore.QObject.connect(self.parameters.wifiSlider, QtCore.SIGNAL("valueChanged(int)"), self.wifi.wifi.setValue)

        self.Screenshots.newS.clicked.connect(self.new_screenshot)

        self.battery.charge.clicked.connect(self.chargeBattery)
        self.wifi.repair.clicked.connect(self.repairWifi)
        QtCore.QObject.connect(self.parameters.wifiSlider, QtCore.SIGNAL("valueChanged(int)"),
                               self.statusBar.wifiBar.setValue)
        QtCore.QObject.connect(self.parameters.batterySlider, QtCore.SIGNAL("valueChanged(int)"),
                               self.statusBar.batteryBar.setValue)
        self.Camera1.cam.inside.connect(self.parameters.insideWidget)
        self.Camera2.cam.inside.connect(self.parameters.insideWidget)
        self.map.map.inside.connect(self.parameters.insideWidget)
        self.pointcloud.pointcloud.inside.connect(self.parameters.insideWidget)
        self.extra.map.inside.connect(self.parameters.insideWidget)
        self.Screenshots.currentScreenshot.inside.connect(self.parameters.insideWidget)
        self.joystick.joystick_direction.connect(self.parameters.jdirection)
        QtCore.QObject.connect(self.parameters.joystickButtonGroup, QtCore.SIGNAL('buttonClicked(int)'),self.joystick.stackedWidget.setCurrentIndex )
        # self.parameters.joystickButtonGroup.connect(self.joystick.stackedWidget.setCurrentIndex, QtCore.SIGNAL('buttonPressed(int)'))
        self.mixedInitiative.AUItoggleButton.clicked.connect(self.statusBar.adaptiveStatus.setChecked)
        self.statusBar.adaptiveStatus.clicked.connect(self.mixedInitiative.AUItoggleButton.setChecked)
        self.statusBar.adaptiveStatus.clicked.connect(self.mixedInitiative.adaptive)

        QtCore.QMetaObject.connectSlotsByName(self)

        # Evidence connections
        self.Camera1.cam.inside.connect(self.mixedInitiative.update_evidence)
        self.Camera2.cam.inside.connect(self.mixedInitiative.update_evidence)
        self.map.map.inside.connect(self.mixedInitiative.update_evidence)
        self.pointcloud.pointcloud.inside.connect(self.mixedInitiative.update_evidence)
        self.extra.map.inside.connect(self.mixedInitiative.update_evidence)
        self.Screenshots.currentScreenshot.inside.connect(self.mixedInitiative.update_evidence)

        self.joystick.joystick_direction.connect(self.mixedInitiative.update_evidence)
        self.joystick.joystick_input.connect(self.mixedInitiative.update_evidence)
        self.battery.lev.connect(self.mixedInitiative.update_evidence)
        self.battery.vis.connect(self.mixedInitiative.update_evidence)
        self.wifi.lev.connect(self.mixedInitiative.update_evidence)
        self.wifi.vis.connect(self.mixedInitiative.update_evidence)
        self.views.vis.connect(self.mixedInitiative.update_evidence)
        self.Screenshots.vis.connect(self.mixedInitiative.update_evidence)
        self.views.bleft.content.connect(self.mixedInitiative.update_evidence)
        self.views.bright.content.connect(self.mixedInitiative.update_evidence)
        self.views.tleft.content.connect(self.mixedInitiative.update_evidence)
        self.views.tright.content.connect(self.mixedInitiative.update_evidence)
        self.views.availableViews.av_wid.connect(self.mixedInitiative.update_evidence)

        # Evidence initialization (manual)
        # TODO find a way to initialize evidence automatically
        self.evidence.update({'C1':'MV', 'C2':'AV', 'PC':'AV','LM':'AV','GM':'AV'})
        self.evidence.update({'battery_level': 'Ok', 'battery_visible':str(self.battery.batteryLevel.isChecked())})
        self.evidence.update({'wifi_level': 'Ok', 'wifi_visible':str(self.wifi.wifiLevel.isChecked())})
        self.evidence.update({'AV_visible':str(self.views.viewsGroup.isChecked())})
        self.evidence.update({'AS_visible':str(self.Screenshots.extraScreenGroup.isChecked())})
        self.evidence.update({'joystick_direction':'False'})
        self.evidence.update({'focus':'C1'})

        self.mixedInitiative.initial_evidence(self.evidence)

        # Atomic action connections
        self.mixedInitiative.decision.connect(self.battery.atomic_decision)
        self.mixedInitiative.decision.connect(self.wifi.atomic_decision)
        self.mixedInitiative.decision.connect(self.Screenshots.atomic_decision)
        self.mixedInitiative.decision.connect(self.views.atomic_decision)

        '''
        State machine.
        '''
        machine = QtCore.QStateMachine()
        state1 = QtCore.QState(machine)
        state2 = QtCore.QState(machine)
        state3 = QtCore.QState(machine)
        machine.setInitialState(state1)
        # State1
        # state1 =

        self.showMaximized()

    def get_evidence(self):
        return self.evidence

    def chargeBattery(self):
        self.parameters.batterySlider.setValue(100)
        self.battery.battery.setValue(100)

    def repairWifi(self):
        self.parameters.wifiSlider.setValue(100)
        self.wifi.wifi.setValue(100)

    def keyPressEvent(self, e):
        self.joystick.setFocus(True)

    def AUIupdate(self):
        enable = self.mixedInitiative.AUItoggleButton.isChecked()
        self.parameters.contents.setEnabled(enable)

    def mouseMoveEvent(self, e):
        # hoveredWidget = QApplication.widgetAt(e.globalPos())
        hoveredWidget = self.childAt(e.pos())
        if hoveredWidget == None:
            self.parameters.currentWidget.setText("")

    def mouseReleaseEvent(self, e):
        # print "Mouse entered"
        if self.Camera1.underMouse():
            # print "Camera 1"
            # self.parameters.currentWidget.clear()
            # self.parameters.currentWidget.setText("Camera 1")
            pass

    def new_screenshot(self):
        self.sc_num = self.sc_num + 1
        ns = image.Screenshot(self.Screenshots.extraScreenGroup, self.sc_num)
        ns.screenshot.inside.connect(self.parameters.insideWidget)
        self.Screenshots.extraScreenshotLayout.addWidget(ns)
        ns.chosen.connect(self.Screenshots.setScreenshot)
        ns.screenshot.inside.connect(self.mixedInitiative.update_evidence)

    def closeEvent(self, event):
        self.closing.emit()


def main():
    app = QtGui.QApplication(sys.argv)
    adaptive_interface = AUI()
    adaptive_interface.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
