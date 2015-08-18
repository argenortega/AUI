# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 03:33:10 2014

@author: Argen
@version: 2.0


Timer function is based on the stopwatch found here: 
http://thecodeinn.blogspot.de/2013/08/pyqt-stopwatch-and-timer.html
"""

import sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QDockWidget, QDesktopWidget
from PyQt4.QtCore import pyqtSlot

from aui.mi import probabilities, utilities, ui_parameters

s = 0
m = 0
h = 0


class AUIParameters(QDockWidget, ui_parameters.Ui_AUIParameters):
    '''
    Parameters related to the gui's adaptivity simulation.
    '''

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

        # self.tab2 = utilities.Utilities(self)

        # self.tab3 = probabilities.Probabilities(self)

        # self.contents.addTab(self.tab2, "Utilities")
        # self.contents.addTab(self.tab3, "Probabilities")
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

        self.focusButtonGroup.setId(self.focus_C1, 0)
        self.focusButtonGroup.setId(self.focus_C2, 1)
        self.focusButtonGroup.setId(self.focus_LM, 2)
        self.focusButtonGroup.setId(self.focus_GM, 3)
        self.focusButtonGroup.setId(self.focus_PC, 4)
        self.focusButtonGroup.setId(self.focus_S, 5)
        self.focusButtonGroup.setId(self.focus_AS, 6)

        self.joystickButtonGroup.buttonClicked.connect(self.context_slot)
        self.contextButtonGroup.buttonClicked.connect(self.context_slot)
        self.focusButtonGroup.buttonClicked.connect(self.focus_slot)

        # print self.contextButtonGroup.buttonClicked()

        # self.userInfo.setVisible(False)

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
        print button.text()

    def som_slot(self, button):
        print button.text()

    def focus_slot(self, button):
        print button.text()


def main():
    app = QtGui.QApplication(sys.argv)
    main = AUIParameters(None)

    main.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
