#!/usr/bin/env python
#  -*- coding: utf-8 -*-
"""
Demonstration Widget to set evidence required by the MI-module.

Timer function is based on the stopwatch found here:
http://thecodeinn.blogspot.de/2013/08/pyqt-stopwatch-and-timer.html
"""

__author__ = "Argentina Ortega Sainz"
__copyright__ = "Copyright (C) 2015 Argentina Ortega Sainz"
__license__ = "MIT"
__version__ = "2.0"

import sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QDockWidget, QDesktopWidget
from PyQt4.QtCore import pyqtSlot, pyqtSignal

from aui.mi import ui_parameters

s = 0
m = 0
h = 0


class AUIParameters(QDockWidget, ui_parameters.Ui_AUIParameters):
    '''
    Parameters related to the gui's adaptivity simulation.
    '''
    sa_level = pyqtSignal(str, str, name='sa_level')
    sl_level = pyqtSignal(str, str, name='sl_level')
    cl_level = pyqtSignal(str, str, name='cl_level')
    context_signal = pyqtSignal(str, str, name='context')


    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.Time)
        time = "%d:%02d:%02d" % (h, m, s)
        self.episodeTimer.setDigitCount(len(time))
        self.episodeTimer.display(time)

        self.startEpisodeButton.clicked.connect(self.Start)
        self.stopEpisodeButton.clicked.connect(lambda: self.timer.stop())
        self.resetEpisodeButton.clicked.connect(self.Reset)

        self.setWidget(self.contents)

        desktop = QDesktopWidget()
        available = QtCore.QRect(desktop.screenGeometry())
        win = QtCore.QRect(self.geometry())

        win_size = 'Window: %d x %d' % (win.height(), win.width())
        screen_size = 'Screen: %d x %d' % (available.height(), available.width())

        self.info.setText(win_size + '\n' + screen_size)

        self.joystickButtonGroup.setId(self.toggle, 0)
        self.joystickButtonGroup.setId(self.sustained, 1)

        self.contextButtonGroup.setId(self.navigation, 0)
        self.contextButtonGroup.setId(self.exploring, 1)
        self.contextButtonGroup.setId(self.mapping, 2)
        self.contextButtonGroup.setId(self.inspection, 3)

        #self.focusButtonGroup.setId(self.focus_C1, 0)
        #self.focusButtonGroup.setId(self.focus_C2, 1)
        #self.focusButtonGroup.setId(self.focus_LM, 2)
        #self.focusButtonGroup.setId(self.focus_GM, 3)
        #self.focusButtonGroup.setId(self.focus_PC, 4)
        #self.focusButtonGroup.setId(self.focus_S, 5)
        #self.focusButtonGroup.setId(self.focus_AS, 6)

        self.contextButtonGroup.buttonClicked.connect(self.context_slot)
        #self.focusButtonGroup.buttonClicked.connect(self.focus_slot)

        QtCore.QObject.connect(self.saSlider, QtCore.SIGNAL("valueChanged(int)"), self.situation_awareness)
        QtCore.QObject.connect(self.stressSlider, QtCore.SIGNAL("valueChanged(int)"), self.stress_level)
        QtCore.QObject.connect(self.cognitiveLoadSlider, QtCore.SIGNAL("valueChanged(int)"), self.cognitive_load)

    def Reset(self):
        global s, m, h

        self.timer.stop()

        s = 0
        m = 0
        h = 0

        time = "%d:%02d:%02d" % (h, m, s)

        self.episodeTimer.setDigitCount(len(time))
        self.episodeTimer.display(time)

    def Start(self):
        global s, m, h

        self.timer.start(1000)

    def Time(self):
        global s, m, h

        if s < 59:
            s += 1
        else:
            if m < 59:
                s = 0
                m += 1
            elif m == 59 and h < 24:
                h += 1
                m = 0
                s = 0
            else:
                self.timer.stop()

        time = "%d:%02d:%02d" % (h, m, s)

        self.episodeTimer.setDigitCount(len(time))
        self.episodeTimer.display(time)

    @pyqtSlot(str, str)
    def insideWidget(self, key, text):
        self.currentWidget.setText(text)

    @pyqtSlot(str, str)
    def jdirection(self, key, text):
        self.direction.setText(text)

    def context_slot(self, button):
        self.context_signal.emit('Context', button.text())

    def som_slot(self, button):
        print button.text()

    def focus_slot(self, button):
        print button.text()

    def situation_awareness(self, value):
        if value == 1:
            self.sa_level.emit('SA', 'L1')
        elif value == 2:
            self.sa_level.emit('SA','L2')
        elif value == 3:
            self.sa_level.emit('SA', 'L3')

    def stress_level(self, value):
        if value == 1:
            self.sl_level.emit('SL', 'low')
        elif value == 2:
            self.sl_level.emit('SL', 'medium')
        elif value == 3:
            self.sl_level.emit('SL', 'high')

    def cognitive_load(self, value):
        if value == 1:
            self.cl_level.emit('CL', 'low')
        elif value == 2:
            self.cl_level.emit('CL', 'medium')
        elif value == 3:
            self.cl_level.emit('CL', 'high')

    @pyqtSlot(int)
    def battery(self, value):
        self.batterySlider.setValue(value)

    @pyqtSlot(int)
    def wifi(self, value):
        self.wifiSlider.setValue(value)

    @pyqtSlot(str, str)
    def set_evidence(self, key, value):
        self.keys.setText(key)
        self.values.setText(value)

    @pyqtSlot(str)
    def set_decision_path(self, value):
        self.decision_path.setText(value)


def main():
    app = QtGui.QApplication(sys.argv)
    main = AUIParameters(None)

    main.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
