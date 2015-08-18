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
from PyQt4.QtCore import pyqtSlot, pyqtSignal
from numpy import argmax

from aui.mi import ui_mixed_initiative as MixInitUI


class MixedInitiative(QWidget, MixInitUI.Ui_mixedInitiative):
    decision = pyqtSignal(str, name='decision')

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.node = 'gui'
        # data = os.path.abspath('networks/hid.gpickle')
        self.d = os.path.dirname(sys.modules['aui.mi'].__file__)
        self.hid = nx.read_gpickle(os.path.join(self.d, 'networks/hid.gpickle'))
        # self.evidence = {}
        self.evidence = {'battery_level': 'Ok', 'wifi_level': 'Ok', 'LM': 'AV', 'focus': 'S', 'PC': 'AV',
                         'AS_visible': 'True', 'wifi_visible': 'True', 'battery_visible': 'True',
                         'C2': 'AV', 'C1': 'MV', 'AV_visible': 'True', 'GM': 'AV', 'joystick_direction': 'Forward'}
        self.decision_path = []
        jvmPath = jpype.getDefaultJVMPath()
        jarpath = os.path.join(os.path.abspath('.'), '/Library/Java/Extensions/')
        jpype.startJVM(jvmPath, "-Djava.class.path=/Library/Java/Extensions/smile.jar")
        self.net = JClass("smile.Network")

        self.setupUi(self)
        self.initUI()

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
        self.AUIStatus.setVisible(False)

        # self.make_decision(self.node)
        # self.check_files()
        # self.hid_decision(self.node)
        # print self.decision

    def initial_evidence(self, ev):
        self.evidence.update(ev)
        # print self.evidence

    def press(self, toggled):
        if toggled:
            self.AUItoggleButton.setText("On")
            self.setSizePolicy(self.sizePolicy)
            self.node = self.hid_decision(self.node)
        else:
            self.AUItoggleButton.setText("Off")
            self.setSizePolicy(self.sizePolicy)
            self.node = 'gui'

    def adaptive(self, toggled):
        if toggled:
            self.node = self.hid_decision(self.node)
            self.AUIMsgs.setVisible(True)
        else:
            self.node = 'gui'
            self.AUIMsgs.setVisible(False)

    def make_decision(self, node):
        if self.hid.successors(node):
            observed_nodes = self.hid.node[node]['evidence']
            observed_evidence = {k: v for k, v in self.evidence.iteritems() if k in observed_nodes}

            n = self.net()
            n.readFile(os.path.join(self.d, 'networks/%s.xdsl' % node))

            for k, v in observed_evidence.iteritems():
                n.setEvidence(k, v)

            n.updateBeliefs()
            # utility = n.getNode('U')
            # decision = n.getNode('decision')
            # print n.getOutcomeIds('decision')
            # print argmax(n.getNodeValue('decision'))
            result = n.getOutcomeId('decision', argmax(n.getNodeValue('decision')))
            print 'Decision: ', result
            return result
        else:
            return node

    def hid_decision(self, node):
        result = self.make_decision(node)
        self.decision_path.append(result)
        if self.hid.successors(result):
            # self.decision.emit(result)
            return self.hid_decision(result)
        else:
            self.decision.emit(result)
            return result

    def check_files(self):
        for node in self.hid.nodes():
            print 'Node: ', node
            if self.hid.successors(node):
                self.make_decision(node, self.evidence)

    @pyqtSlot(str, str)
    def update_evidence(self, key, value):
        sender = self.sender()
        print 'Key: %s Value: %s' % (key, value)
        k = str(key)
        v = str(value)
        if self.evidence.has_key(k):
            if not self.evidence.get(k) == v:
                self.evidence[k] = v
                if self.AUItoggleButton.isChecked():
                    # print 'Updating decision'
                    path = nx.shortest_path(self.hid, 'gui', self.node)
                    parent = path.pop()
                    path.reverse()
                    for p in path:
                        if k in self.hid.node[p]['evidence']:
                            parent = p

                    self.node = self.hid_decision(parent)
        else:
            'Error: %s is not yet in evidence.' % key

    def closeEvent(self, event):
        # print 'MI shutdown'
        shutdownJVM()


def main():
    app = QtGui.QApplication(sys.argv)
    mi = MixedInitiative(None)
    mi.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
