#!/usr/bin/env python
#  -*- coding: utf-8 -*-
"""
Script for creating global settings used as adaptable properties in the MI module
"""

__author__ = "Argentina Ortega Sainz"
__copyright__ = "Copyright (C) 2015 Argentina Ortega Sainz"
__license__ = "MIT"
__version__ = "2.0"

from PyQt4.QtCore import QSettings, QVariant
from PyQt4.QtGui import QWidget, QApplication
import sys

class CreateSettings(QWidget):
    def __init__(self, device=None):
        QWidget.__init__(self)
        QSettings.setPath(QSettings.IniFormat, QSettings.UserScope, "../../config/user")
        QSettings.setPath(QSettings.IniFormat, QSettings.SystemScope, "../../config/sys")

        if device == 'UGV':
            self.settings = QSettings(QSettings.SystemScope, "TRADR", "UGV")
            self.settings_ugv()
        elif device == 'UAV':
            self.settings_uav()
        elif device == 'InField':
            self.settings_infield()
        elif device == 'CommandTable':
            self.settings_commandtable()
        else:
            self.settings = QSettings(QSettings.IniFormat, QSettings.SystemScope, "TRADR", "InField")
            print self.settings.contains("RobotState/Battery")
            print self.settings.value("RobotState/Battery", 'Not there').toString()


def main():
    app = QApplication(sys.argv)
    win = CreateSettings()
    win.show()
    win.activateWindow()
    win.raise_()
    sys.exit(app.exec_())


def clear_settings():
    settings = QSettings(QSettings.SystemScope, 'TRADR', 'UGV')
    settings.clear()

    settings = QSettings(QSettings.SystemScope,'TRADR', 'UAV')
    settings.clear()

    settings = QSettings(QSettings.SystemScope,'TRADR', 'InField')
    settings.clear()

    settings = QSettings(QSettings.SystemScope, 'TRADR', 'CommandTable')
    settings.clear()


def settings():
    QSettings.setPath(QSettings.IniFormat, QSettings.UserScope, '../../config/user')
    QSettings.setPath(QSettings.IniFormat, QSettings.SystemScope, '../../config/sys')

    settings = QSettings(QSettings.IniFormat, QSettings.SystemScope, "TRADR", "UGV")

    settings.beginGroup("Views")
    settings.setValue("Camera1", True)
    settings.setValue("Camera2", True)
    settings.setValue("LocalMap", True)
    settings.setValue("GlobalMap", True)
    settings.setValue("PointCloud", True)
    settings.endGroup()

    settings.beginGroup("Snapshots")
    settings.setValue("Snapshots", True)
    settings.endGroup()

    settings.beginGroup("RobotState")
    settings.setValue("Battery", True)
    settings.setValue("Wifi", True)
    settings.setValue("Joystick", True)
    settings.endGroup()
    settings.sync()

    settings = QSettings(QSettings.IniFormat, QSettings.SystemScope, "TRADR", "UAV")
    settings.beginGroup("Views")
    settings.setValue("Camera1", True)
    settings.setValue("Camera2", True)
    settings.setValue("LocalMap", True)
    settings.setValue("GlobalMap", True)
    settings.setValue("PointCloud", False)
    settings.endGroup()

    settings.beginGroup("Snapshots")
    settings.setValue("Snapshots", True)
    settings.endGroup()

    settings.beginGroup("RobotState")
    settings.setValue("Battery", True)
    settings.setValue("Wifi", True)
    settings.setValue("Joystick", False)
    settings.endGroup()
    settings.sync()

    settings = QSettings(QSettings.IniFormat, QSettings.SystemScope, "TRADR", "InField")
    settings.beginGroup("Views")
    settings.setValue("Camera1", False)
    settings.setValue("Camera2", False)
    settings.setValue("LocalMap", True)
    settings.setValue("GlobalMap", True)
    settings.setValue("PointCloud", False)
    settings.endGroup()

    settings.beginGroup("Snapshots")
    settings.setValue("Snapshots", True)
    settings.endGroup()

    settings.beginGroup("RobotState")
    settings.setValue("Battery", True)
    settings.setValue("Wifi", True)
    settings.setValue("Joystick", False)
    settings.endGroup()
    settings.sync()

    settings = QSettings(QSettings.IniFormat, QSettings.SystemScope, "TRADR", "CommandTable")
    settings.beginGroup("Views")
    settings.setValue("Camera1",False)
    settings.setValue("Camera2", False)
    settings.setValue("LocalMap", True)
    settings.setValue("GlobalMap", True)
    settings.setValue("PointCloud", False)
    settings.endGroup()

    settings.beginGroup("Snapshots")
    settings.setValue("Snapshots", True)
    settings.endGroup()

    settings.beginGroup("RobotState")
    settings.setValue("Battery", False)
    settings.setValue("Wifi", False)
    settings.setValue("Joystick", False)
    settings.endGroup()
    settings.sync()




if __name__ == "__main__":
    # clear_settings()
    settings()
    # main()
