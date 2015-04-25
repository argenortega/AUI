# -*- coding: utf-8 -*-
"""
Created on Sat Dec 27 02:57:21 2014

@author: Argentina Ortega Sáinz
@version: 0.0.2
"""
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QMainWindow, QHBoxLayout, QVBoxLayout, QApplication, QDesktopWidget)
# from PyQt4.uic import loadUi

import Camera
import MixedInitiative
import NewView
import Map
import Pointcloud
import Screenshot
import Screenshots
import Wifi
import Battery
import Joystick
import Parameters
import StatusBar
import Toolbar
import Views
import AUIUI
import ActiveLabel


class AUI(QMainWindow,AUIUI.Ui_MainWin):
    """
    Adaptive User Interface for TRADR project
    """

    def __init__(self, parent=None):
        super(AUI, self).__init__()
        self.sc_num = 0
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        #self.setGeometry(0, 0, 1280, 800)
        self.setWindowTitle("Adaptive TRADR OCU")
        self.setMouseTracking(True)

        self.label.setVisible(False)


        '''
        Layout Definitions for the complete AUI
        '''
        # Global Layout for AUI Parameters + TRADR GUI
        #self.globalLayout = QHBoxLayout()
        #self.setLayout(self.globalLayout)
        #self.globalLayout.setMargin(0)

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
        self.statusBar = StatusBar.StatusBar(self)
        self.MainLayout.addWidget(self.statusBar)

        self.mixedInitiative = MixedInitiative.MixedInitiative(self)
        self.MainLayout.addWidget(self.mixedInitiative)

        self.MainLayout.addLayout(self.GUILayout)

        #self.views = QtGui.QGroupBox("Available Views", self)
        #self.views.setMinimumSize(QtCore.QSize(550, 70))
        #self.views.setMaximumSize(QtCore.QSize(5000, 150))
        #self.views.setObjectName("views")
        #self.viewsGroupLayout = QtGui.QHBoxLayout(self.views)
        #self.viewsGroupLayout.setObjectName("viewsGroupLayout")

        self.views = Views.Views(self)
        # minSize = QtCore.QSize(50, 50)
        # maxSize = QtCore.QSize(70, 70)
        # stretch = 0
        self.pointcloud = Pointcloud.Pointcloud(self)
        self.pointcloud.setParent(self.views)
        self.views.availableViewsLayout.addWidget(self.pointcloud)

        # minSize = QtCore.QSize(50, 50)
        # maxSize = QtCore.QSize(70, 70)
        # stretch = 0
        self.map = Map.Map(self)
        self.map.setParent(self.views)
        self.views.availableViewsLayout.addWidget(self.map)

        # minSize = QtCore.QSize(50, 50)
        # maxSize = QtCore.QSize(70, 70)
        # stretch = 0
        self.extra = NewView.NewView(self)
        self.extra.setParent(self.views)
        self.views.availableViewsLayout.addWidget(self.extra)

        #self.MainViews = QtGui.QGridLayout()
        #self.MainViews.setObjectName("MainViews")


        # minSize = QtCore.QSize(100, 100)
        # maxSize = QtCore.QSize(300, 300)
        # stretch = 3
        self.Camera1 = Camera.Camera(self, 1)
        self.views.tleftLayout.addWidget(self.Camera1)
        self.views.tleftLabel.setVisible(False)


        # minSize = QtCore.QSize(100, 100)
        # maxSize = QtCore.QSize(300, 300)
        # stretch = 1
        self.Camera2 = Camera.Camera(self, 2)
        self.Camera2.setMinimumSize(QtCore.QSize(80,80))
        self.views.bleftLayout.addWidget(self.Camera2)
        self.views.bleftLabel.setVisible(False)


        #self.ViewsLayout.addLayout(self.MainViews)
        #self.ViewsLayout.addWidget(self.views)

        self.GUILayout.addWidget(self.views)

        # minSize = QtCore.QSize(150, 150)
        # maxSize = QtCore.QSize(200, 200)
        # stretch = 1
        self.Screenshots = Screenshots.Screenshots(self)
        self.scr2 = Screenshot.Screenshot(self.Screenshots.extraScreenGroup,2)
        self.scr3 = Screenshot.Screenshot(self.Screenshots.extraScreenGroup,3)
        self.scr4 = Screenshot.Screenshot(self.Screenshots.extraScreenGroup,4)
        self.Screenshots.extraScreenshotLayout.addWidget(self.scr2)
        self.Screenshots.extraScreenshotLayout.addWidget(self.scr3)
        self.Screenshots.extraScreenshotLayout.addWidget(self.scr4)

        self.GUILayout.addWidget(self.Screenshots)

        # minSize = QtCore.QSize(80, 80)
        # maxSize = QtCore.QSize(120, 120)
        self.battery = Battery.Battery(self)
        self.wifi = Wifi.Wifi(self)

        self.joystick = Joystick.Joystick(self)

        self.StatusLayout.addWidget(self.battery)
        self.StatusLayout.addWidget(self.wifi)
        self.StatusLayout.addStretch()
        self.StatusLayout.addWidget(self.joystick)

        self.GUILayout.addLayout(self.StatusLayout)

        self.parameters = Parameters.AUIParameters(self)
        #self.globalLayout.addWidget(self.parameters)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.parameters)

        '''
        Connect internal widgets
        '''
        self.mixedInitiative.AUItoggleButton.clicked[bool].connect(self.AUIupdate)
        self.AUIupdate()
        QtCore.QObject.connect(self.parameters.wifiSlider, QtCore.SIGNAL("valueChanged(int)"), self.wifi.value.setNum)
        QtCore.QObject.connect(self.parameters.batterySlider, QtCore.SIGNAL("valueChanged(int)"),
                               self.battery.value.setNum)
        QtCore.QObject.connect(self.parameters.batterySlider, QtCore.SIGNAL("valueChanged(int)"),
                               self.battery.battery.setValue)
        QtCore.QObject.connect(self.parameters.wifiSlider, QtCore.SIGNAL("valueChanged(int)"), self.wifi.wifi.setValue)

        self.battery.charge.clicked.connect(self.chargeBattery)
        self.wifi.repair.clicked.connect(self.repairWifi)
        QtCore.QObject.connect(self.parameters.wifiSlider, QtCore.SIGNAL("valueChanged(int)"), self.statusBar.wifiBar.setValue)
        QtCore.QObject.connect(self.parameters.batterySlider, QtCore.SIGNAL("valueChanged(int)"),
                               self.statusBar.batteryBar.setValue)
        #QtCore.QObject.connect(self.Camera1.cam.inside,QtCore.pyqtSignal(),self.parameters.insideWidget)
        self.Camera1.cam.inside.connect(self.parameters.insideWidget)
        self.Camera2.cam.inside.connect(self.parameters.insideWidget)
        self.map.map.inside.connect(self.parameters.insideWidget)
        self.pointcloud.pointcloud.inside.connect(self.parameters.insideWidget)
        self.extra.view.inside.connect(self.parameters.insideWidget)
        self.Screenshots.currentScreenshot.inside.connect(self.parameters.insideWidget)
        #self.scr2.screenshot.inside.connect(self.parameters.insideWidget)
        #self.scr3.screenshot.inside.connect(self.parameters.insideWidget)
        #self.scr4.screenshot.inside.connect(self.parameters.insideWidget)


        QtCore.QMetaObject.connectSlotsByName(self)

        '''
        State machine.
        '''
        machine = QtCore.QStateMachine()
        state1 = QtCore.QState(machine)
        state2 = QtCore.QState(machine)
        state3 = QtCore.QState(machine)
        machine.setInitialState(state1)

        #State1
        #state1 =


        self.showMaximized()



    def chargeBattery(self):
        self.parameters.batterySlider.setValue(100)
        self.battery.battery.setValue(100)
        self.battery.value.setText('100')

    def repairWifi(self):
        self.parameters.wifiSlider.setValue(100)
        self.wifi.wifi.setValue(100)
        self.battery.value.setText('100')

    def keyPressEvent(self, e):
        self.joystick.setFocus(True)

    def AUIupdate(self):
        enable = self.mixedInitiative.AUItoggleButton.isChecked()
        self.parameters.contents.setEnabled(enable)

    def mouseMoveEvent(self, e):
        #hoveredWidget = QApplication.widgetAt(e.globalPos())
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

    def new_screenshot(self,num):
        ns = ActiveLabel.ActLabel(self.extraScreenGroup)
        ns.setText("Screenshot %d"%num)
        ns.setObjectName("img%d"%num)
        self.extraScreenshotLayout.addWidget(ns)
        self.sc_num = self.sc_num + 1

def main():
    app = QtGui.QApplication(sys.argv)
    main = AUI()

    main.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
