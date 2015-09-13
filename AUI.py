#!/usr/bin/env python
#  -*- coding: utf-8 -*-
"""
Mixed-Initiative Adaptive User Interface
"""

__author__ = "Argentina Ortega Sainz"
__copyright__ = "Copyright (C) 2015 Argentina Ortega Sainz"
__license__ = "MIT"
__version__ = "2.0"

import sys
import os

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSignal, QObject, SIGNAL, QSettings, QSize, QPoint
from PyQt4.QtGui import (QMainWindow, QHBoxLayout, QVBoxLayout, QDialog, QMessageBox, QDesktopWidget, QFrame)

from aui.gui.views.sources import camera, lmap, gmap, pointcloud
from aui.gui.robot.internal import battery, wifi
from aui.gui.robot.joystick import joystick
from aui.gui.snapshots import snapshot, image
from aui.gui.views import mainviews
from aui.gui.status import statusbar
from aui.mi import mixed_initative
from aui.mi import parameters

import ui_aui, ui_user

from PyQt4.uic import loadUi


class Login(QDialog, ui_user.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.loginButton.clicked.connect(self.login)
        self.username = 'user'
        self.passphrase = '1234'
        self.device = 'UGV'

    def login(self):
        self.username = self.user.text()
        self.passphrase = self.password.text()
        self.device = self.profile()
        self.accept()

    def getValues(self):
        return self.username, self.device

    def profile(self):
        if self.operatorProfile.isChecked():
            return 'UGV'
        elif self.teamLeaderProfile.isChecked():
            return 'CommandTable'
        elif self.infieldProfile.isChecked():
            return 'InField'


class AUI(QMainWindow, ui_aui.Ui_MainWin):
    """
    Adaptive User Interface
    """
    closing = pyqtSignal()

    def __init__(self, parent=None, user='user', device='UGV'):
        super(AUI, self).__init__()
        self.setupUi(self)
        self.user = user
        desktop = QDesktopWidget()
        self.available = QtCore.QRect(desktop.screenGeometry())
        screen_size = 'Screen: %d x %d' % (self.available.height(), self.available.width())
        print screen_size

        QSettings.setPath(QSettings.IniFormat, QSettings.UserScope, 'config/user')
        QSettings.setPath(QSettings.IniFormat, QSettings.SystemScope, 'config/sys')

        self.globalsettings = QSettings(QSettings.IniFormat, QSettings.SystemScope, "TRADR", device)
        self.usersettings = QSettings(QSettings.IniFormat, QSettings.UserScope, "TRADR", device)

        self.sc_num = 0
        self.evidence = {}
        self.initUI()
        self.read_settings()
        self.closing.connect(self.mixedInitiative.close)
        self.showMaximized()
        win = QtCore.QRect(self.geometry())
        win_size = 'Window: %d x %d' % (win.height(), win.width())
        print win_size

    def initUI(self):
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
        self.GUILayout.addWidget(self.views)

        self.Screenshots = snapshot.Screenshots(self)
        self.GUILayout.addWidget(self.Screenshots)

        self.battery = battery.Battery(self)
        self.wifi = wifi.Wifi(self)
        self.joystick = joystick.Joystick(self)

        self.StatusLayout.addWidget(self.battery)
        self.StatusLayout.addWidget(self.wifi)
        self.StatusLayout.addStretch()
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
        # self.mixedInitiative.AUItoggleButton.clicked[bool].connect(self.AUIupdate)
        # self.statusBar.adaptiveStatus.clicked[bool].connect(self.AUIupdate)
        # self.AUIupdate()
        # QtCore.QObject.connect(self.parameters.wifiSlider, QtCore.SIGNAL("valueChanged(int)"), self.wifi.value.setNum)
        # QtCore.QObject.connect(self.parameters.batterySlider, QtCore.SIGNAL("valueChanged(int)"),
        # self.battery.value.setNum)
        QObject.connect(self.parameters.batterySlider, SIGNAL("valueChanged(int)"),
                               self.battery.battery.setValue)
        QtCore.QObject.connect(self.parameters.wifiSlider, QtCore.SIGNAL("valueChanged(int)"), self.wifi.wifi.setValue)

        #QObject.connect(self.battery.battery.valueChanged, SIGNAL('valueChanged(int)'), self.parameters.battery)
        #QObject.connect(self.wifi.wifi.valueChanged, SIGNAL('valueChanged(int)'), self.parameters.wifi)

        #self.battery.charge.clicked.connect(self.chargeBattery)
        #self.wifi.repair.clicked.connect(self.repairWifi)

        self.battery.recharge_signal.connect(self.parameters.batterySlider.setValue)
        self.wifi.repair_signal.connect(self.parameters.wifiSlider.setValue)

        QObject.connect(self.wifi.wifi, SIGNAL("valueChanged(int)"), self.statusBar.wifiBar.setValue)
        QObject.connect(self.battery.battery, SIGNAL("valueChanged(int)"), self.statusBar.batteryBar.setValue)

        self.Screenshots.newS.clicked.connect(self.new_screenshot)

        self.views.camera1.cam.inside.connect(self.parameters.insideWidget)
        self.views.camera2.cam.inside.connect(self.parameters.insideWidget)
        self.views.localmap.map.inside.connect(self.parameters.insideWidget)
        self.views.pointcloud.pointcloud.inside.connect(self.parameters.insideWidget)
        self.views.globalmap.map.inside.connect(self.parameters.insideWidget)
        self.Screenshots.currentScreenshot.inside.connect(self.parameters.insideWidget)
        self.joystick.joystick_direction.connect(self.parameters.jdirection)
        QtCore.QObject.connect(self.parameters.joystickButtonGroup, QtCore.SIGNAL('buttonClicked(int)'),
                               self.joystick.stackedWidget.setCurrentIndex)
        # self.parameters.joystickButtonGroup.connect(self.joystick.stackedWidget.setCurrentIndex, QtCore.SIGNAL('buttonPressed(int)'))
        self.mixedInitiative.AUItoggleButton.clicked.connect(self.statusBar.adaptiveStatus.setChecked)
        self.statusBar.adaptiveStatus.clicked.connect(self.mixedInitiative.AUItoggleButton.setChecked)
        self.statusBar.adaptiveStatus.clicked.connect(self.mixedInitiative.adaptive)
        QtCore.QObject.connect(self.parameters.costSlider, QtCore.SIGNAL("valueChanged(int)"),
                               self.mixedInitiative.voi_cost)

        QtCore.QMetaObject.connectSlotsByName(self)

        # Evidence connections
        self.views.camera1.cam.inside.connect(self.mixedInitiative.update_evidence)
        self.views.camera2.cam.inside.connect(self.mixedInitiative.update_evidence)
        self.views.localmap.map.inside.connect(self.mixedInitiative.update_evidence)
        self.views.pointcloud.pointcloud.inside.connect(self.mixedInitiative.update_evidence)
        self.views.globalmap.map.inside.connect(self.mixedInitiative.update_evidence)
        self.Screenshots.currentScreenshot.inside.connect(self.mixedInitiative.update_evidence)
        self.Screenshots.extraScreenGroup.inside.connect(self.mixedInitiative.update_evidence)
        self.views.viewsGroup.inside.connect(self.mixedInitiative.update_evidence)


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

        self.parameters.cl_level.connect(self.mixedInitiative.update_evidence)
        self.parameters.sa_level.connect(self.mixedInitiative.update_evidence)
        self.parameters.sl_level.connect(self.mixedInitiative.update_evidence)
        self.parameters.context_signal.connect(self.mixedInitiative.update_evidence)

        # Evidence initialization (manual)
        # TODO find a way to initialize evidence automatically
        self.evidence.update({'C1': 'MV', 'C2': 'MV', 'PC': 'AV', 'LM': 'AV', 'GM': 'AV'})
        self.evidence.update({'battery_level': 'Ok', 'battery_visible': str(self.battery.batteryLevel.isChecked())})
        self.evidence.update({'wifi_level': 'Ok', 'wifi_visible': str(self.wifi.wifiLevel.isChecked())})
        self.evidence.update({'AV_visible': str(self.views.viewsGroup.isChecked())})
        self.evidence.update({'AS_visible': str(self.Screenshots.extraScreenGroup.isChecked())})
        self.evidence.update({'joystick_direction': 'False'})
        self.evidence.update({'focus': 'C1'})
        self.evidence.update({'SA': 'L2', 'SL': 'low', 'CL': 'low'})
        self.evidence.update({'Context': 'Navigation'})

        self.mixedInitiative.initial_evidence(self.evidence)

        # Atomic action connections
        self.mixedInitiative.decision.connect(self.battery.atomic_decision)
        self.mixedInitiative.decision.connect(self.wifi.atomic_decision)
        self.mixedInitiative.decision.connect(self.Screenshots.atomic_decision)
        self.mixedInitiative.decision.connect(self.views.atomic_decision)

        self.logbar.showMessage('Ready')

        self.mixedInitiative.evidence_signal.connect(self.parameters.set_evidence)
        self.mixedInitiative.decision_path_signal.connect(self.parameters.set_decision_path)

    def read_settings(self):
        self.globalsettings.beginGroup('Views')

        self.views.camera1.setVisible(self.globalsettings.value('Camera1', True).toBool())
        self.views.camera2.setVisible(self.globalsettings.value('Camera2', True).toBool())
        self.views.localmap.setVisible(self.globalsettings.value('LocalMap', True).toBool())
        self.views.globalmap.setVisible(self.globalsettings.value('GlobalMap', True).toBool())
        self.views.pointcloud.setVisible(self.globalsettings.value('PointCloud', True).toBool())
        self.globalsettings.endGroup()

        self.globalsettings.beginGroup("Snapshots")
        self.Screenshots.setVisible(self.globalsettings.value("Snapshots", True).toBool())
        self.globalsettings.endGroup()

        self.globalsettings.beginGroup("RobotState")
        self.battery.setVisible(self.globalsettings.value("Battery", True).toBool())
        self.wifi.setVisible(self.globalsettings.value("Wifi", True).toBool())
        self.joystick.setVisible(self.globalsettings.value("Joystick", True).toBool())
        self.globalsettings.endGroup()

        self.usersettings.beginGroup(self.user)

        self.resize(self.usersettings.value('MainWindow/size', QSize(751, 1280)).toSize())
        self.move(self.usersettings.value('MainWindow/pos', QPoint(200,200)).toPoint())
        # self.restoreState(self.usersettings.value('windowState').toByteArray())

        parent_str = self.usersettings.value('Camera1').toString()
        parent = self.views.findChild(QFrame, parent_str)
        self.views.camera1.setParent(parent)
        parent.add_widget(self.views.camera1)

        parent_str = self.usersettings.value('Camera2').toString()
        parent = self.views.findChild(QFrame, parent_str)
        self.views.camera2.setParent(parent)
        parent.add_widget(self.views.camera2)

        parent_str = self.usersettings.value('LocalMap').toString()
        parent = self.views.findChild(QFrame, parent_str)
        self.views.localmap.setParent(parent)
        parent.add_widget(self.views.localmap)

        parent_str = self.usersettings.value('GlobalMap').toString()
        parent = self.views.findChild(QFrame, parent_str)
        self.views.globalmap.setParent(parent)
        parent.add_widget(self.views.globalmap)

        parent_str = self.usersettings.value('PointCloud').toString()
        parent = self.views.findChild(QFrame, parent_str)
        self.views.pointcloud.setParent(parent)
        parent.add_widget(self.views.pointcloud)



        visible = self.usersettings.value('AV', True).toBool()
        self.views.availableViews.setVisible(visible)
        self.views.viewsGroup.setChecked(visible)
        self.evidence.update({'AV_visible': str(visible)})

        visible = self.usersettings.value('AS', True).toBool()
        self.Screenshots.extraScreenGroup.setChecked(visible)
        self.Screenshots.scrollArea.setVisible(visible)
        self.evidence.update({'AS_visible': str(visible)})

        visible = self.usersettings.value('Battery', True).toBool()
        self.battery.batteryLevel.setChecked(visible)
        self.battery.frame.setVisible(visible)
        self.evidence.update({'battery_level': str(self.battery.get_level()), 'battery_visible': str(visible)})

        visible = self.usersettings.value('Wifi', True).toBool()
        self.wifi.wifiLevel.setChecked(visible)
        self.wifi.frame.setVisible(visible)
        self.evidence.update({'wifi_level': str(self.wifi.get_level()), 'wifi_visible': str(visible)})

        self.usersettings.endGroup()

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

    def new_screenshot(self):
        self.sc_num = self.sc_num + 1
        ns = image.Screenshot(self.Screenshots.extraScreenGroup, self.sc_num)
        ns.screenshot.inside.connect(self.parameters.insideWidget)
        self.Screenshots.extraScreenshotLayout.addWidget(ns)
        ns.chosen.connect(self.Screenshots.setScreenshot)
        ns.screenshot.inside.connect(self.mixedInitiative.update_evidence)

    def write_settings(self):

        self.usersettings.beginGroup(self.user)

        self.usersettings.setValue('MainWindow/size', self.size())
        self.usersettings.setValue('MainWindow/pos', self.pos())

        self.usersettings.setValue('Camera1', self.views.camera1.parent().objectName())
        self.usersettings.setValue('Camera2', self.views.camera2.parent().objectName())
        self.usersettings.setValue('LocalMap', self.views.localmap.parent().objectName())
        self.usersettings.setValue('GlobalMap', self.views.globalmap.parent().objectName())
        self.usersettings.setValue('PointCloud', self.views.pointcloud.parent().objectName())


        self.usersettings.setValue('AV', str(self.views.viewsGroup.isChecked()))

        self.usersettings.setValue('AS', str(self.Screenshots.extraScreenGroup.isChecked()))

        self.usersettings.setValue('Battery', str(self.battery.batteryLevel.isChecked()))

        self.usersettings.setValue('Wifi', str(self.wifi.wifiLevel.isChecked()))

        self.usersettings.remove('windowState')

        # self.usersettings.setValue('windowState', self.saveState())

        self.usersettings.endGroup()

        self.usersettings.sync()

    def closeEvent(self, event):
        self.write_settings()
        self.closing.emit()


def login():
    app = QtGui.QApplication(sys.argv)
    login_widget = Login()

    if login_widget.exec_():
        username, device = login_widget.getValues()
        adaptive_interface = AUI(user=username, device=device)
        adaptive_interface.show()
        adaptive_interface.raise_()
        sys.exit(app.exec_())


def main():
    app = QtGui.QApplication(sys.argv)
    adaptive_interface = AUI()
    adaptive_interface.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    login()
    # main()
