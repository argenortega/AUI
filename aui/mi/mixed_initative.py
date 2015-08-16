# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 04:42:13 2014

@author: Argen
"""

import sys
import jpype
from jpype import JClass, shutdownJVM, JavaException
import os.path
import networkx as nx
import glob

from PyQt4 import QtGui
from PyQt4.QtGui import (QWidget, QSizePolicy)
from PyQt4.QtCore import pyqtSlot

from aui.mi import ui_mixed_initiative as MixInitUI


class MixedInitiative(QWidget, MixInitUI.Ui_mixedInitiative):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.node = 'gui'
        self.setupUi(self)
        self.initUI()
        self.evidence = {}

    def initUI(self):
        self.AUItoggleButton.clicked[bool].connect(self.press)
        self.AUItoggleButton.toggled.connect(self.AUIMsgs.setVisible)

        self.AUIMsgs.hide()

        self.sizePolicy = QtGui.QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)

        self.setSizePolicy(self.sizePolicy)

        self.textBrowserAUIMix.setText('[00:00]: Adaptive capabilities turned on.\n'
                                       '[02:31]: Display recommended views for Navigation?')

        # self.make_decision('gui','yes')
        print self.parent()

    def press(self, toggled):
        if toggled:
            self.AUItoggleButton.setText("On")
            self.setSizePolicy(self.sizePolicy)
        else:
            self.AUItoggleButton.setText("Off")
            self.setSizePolicy(self.sizePolicy)
            self.node = 'gui'

    def make_decision(self, node, evidence):
        jvmPath = jpype.getDefaultJVMPath()
        jarpath = os.path.join(os.path.abspath('.'), '/Library/Java/Extensions/')
        jpype.startJVM(jvmPath, "-Djava.class.path=/Library/Java/Extensions/smile.jar")
        net = JClass("smile.Network")
        n = net()
        n.readFile('networks/%s.xdsl' % node)
        n.updateBeliefs()
        v1 = n.getNode('U')
        decision = n.getNode('decision')
        print decision
        shutdownJVM()

    @pyqtSlot(str, str)
    def update_evidence(self, key, value):
        sender = self.sender()
        print 'Key:', key, 'Value:', value


def main():
    app = QtGui.QApplication(sys.argv)
    mi = MixedInitiative(None)
    mi.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
