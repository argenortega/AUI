#!/usr/bin/env python
#  -*- coding: utf-8 -*-
"""
Mixed-Initiative Module

This module users the SMILE reasoning engine developed by the Decision Systems Laboratory of the University of
Pittsburgh available at http://genie.sis.pitt.edu/.
"""

__author__ = "Argentina Ortega Sainz"
__copyright__ = "Copyright (C) 2015 Argentina Ortega Sainz"
__license__ = "MIT"
__version__ = "2.0"


import sys
import jpype
from jpype import JClass, shutdownJVM, JavaException
import os.path
import networkx as nx
import glob
from time import strftime, localtime

from PyQt4 import QtGui
from PyQt4.QtGui import (QWidget, QSizePolicy, QDialog, QHBoxLayout, QPushButton, QApplication, QTextCharFormat)
from PyQt4.QtCore import pyqtSlot, pyqtSignal, QTimer, QThread, Qt
from PyQt4.uic import loadUi
from numpy import argmax, isclose

from aui.mi import ui_mixed_initiative as MixInitUI


class MixedInitiative(QWidget, MixInitUI.Ui_mixedInitiative):
    decision = pyqtSignal(str, name='decision')

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.buttonThread = QThread()
        self.node = 'gui'
        self.cost = 0
        self.hsm_node = None
        self.d = os.path.dirname(sys.modules['aui.mi'].__file__)
        self.hid = nx.read_gpickle(os.path.join(self.d, 'networks/hid.gpickle'))

        self.hsm = nx.get_node_attributes(self.hid, 'HSM')
        self.hsm_evidence = {}
        self.question = None

        self.answerTimer = QTimer()
        self.answerTimer.setSingleShot(True)

        self.small_pause = QTimer()

        self.decisionFormat = QTextCharFormat()
        self.decisionFormat.setForeground(QtGui.QColor(76, 175, 80))
        self.decisionFormat.setFontWeight(QtGui.QFont.Normal)

        self.questionFormat = QTextCharFormat()
        self.questionFormat.setForeground(QtGui.QColor(48, 131, 251))
        self.questionFormat.setFontWeight(QtGui.QFont.Bold)

        self.infoFormat = QTextCharFormat()
        self.infoFormat.setFontWeight(QtGui.QFont.Normal)
        self.infoFormat.setForeground(Qt.black)

        self.evidence = {'battery_level': 'Ok', 'wifi_level': 'Ok', 'LM': 'MV', 'focus': 'S', 'PC': 'AV',
                         'AS_visible': 'True', 'wifi_visible': 'True', 'battery_visible': 'True',
                         'C2': 'MV', 'C1': 'MV', 'AV_visible': 'True', 'GM': 'AV', 'joystick_direction': 'Backwards',
                         'SA': 'L2', 'SL': 'medium', 'CL': 'medium',
                         'Context': 'Exploration'}
        self.evidence = {}

        self.decision_path = []
        jvmPath = jpype.getDefaultJVMPath()
        jarpath = os.path.join(os.path.abspath('.'), '/Library/Java/Extensions/')
        jpype.startJVM(jvmPath, "-Djava.class.path=/Library/Java/Extensions/smile.jar")
        self.net = JClass("smile.Network")
        self.voi = JClass("smile.ValueOfInfo")

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

        self.messages.setReadOnly(True)

        self.AUIStatus.setVisible(False)
        self.defaultButton.setVisible(False)
        self.button2.setVisible(False)
        self.button3.setVisible(False)
        self.button4.setVisible(False)

        self.buttonGroup.setId(self.defaultButton, 0)
        self.buttonGroup.setId(self.button2, 1)
        self.buttonGroup.setId(self.button3, 2)
        self.buttonGroup.setId(self.button4, 3)

        self.buttonGroup.buttonClicked.connect(self.atomic_decision)

        # self.make_decision('main_views')
        # self.check_files()
        # self.hid_decision(self.node)
        # print self.decision

    def initial_evidence(self, ev):
        self.evidence.update(ev)
        # print self.evidence

    def voi_cost(self, value):
        self.cost = value

    def timestamp(self):
        return strftime('%H:%M:%S', localtime())

    def press(self, toggled):
        if toggled:
            self.AUItoggleButton.setText("On")
            self.setSizePolicy(self.sizePolicy)
            self.messages.setCurrentCharFormat(self.infoFormat)
            self.messages.append('[%s] Adaptive Capabilities Turned On'%self.timestamp())
            self.node = self.hid_decision(self.node)
        else:
            self.AUItoggleButton.setText("Off")
            self.setSizePolicy(self.sizePolicy)
            self.node = 'gui'
            self.hide_buttons()

    def adaptive(self, toggled):
        if toggled:
            self.AUIMsgs.setVisible(True)
            self.messages.setCurrentCharFormat(self.infoFormat)
            self.messages.append('[%s] Adaptive Capabilities Turned On'%self.timestamp())
            self.node = self.hid_decision(self.node)
            self.decision.emit(self.node)
        else:
            self.node = 'gui'
            self.AUIMsgs.setVisible(False)
            self.hide_buttons()

    def make_decision(self, node):
        if self.hid.successors(node):
            observed_nodes = self.hid.node[node]['evidence']
            observed_evidence = {k: v for k, v in self.evidence.iteritems() if k in observed_nodes}

            hsm_nodes = self.hsm.get(node, None)

            n = self.net()
            n.readFile(os.path.join(self.d, 'networks/%s.xdsl' % node))

            for k, v in observed_evidence.iteritems():
                n.setEvidence(k, v)

            n.updateBeliefs()

            if hsm_nodes is not None:
                question = []
                for h in hsm_nodes:
                    v = self.voi(n)
                    v.addNode(h)
                    v.setDecision('decision')
                    v.setPointOfView('decision')
                    v.update()
                    # print h, v.getValues()
                    evi = v.getValues()
                    # print h, evi
                    question.append(evi[0])

                # print question
                if question:
                    voi = max(question)
                    if voi - self.cost > 0 and not isclose(voi,0):
                        ask = hsm_nodes[argmax(question)]
                        ask = ask.replace('HSM_', '')
                        n.updateBeliefs()
                        options = dict(zip(n.getOutcomeIds(ask), n.getNodeValue(ask)))
                        print 'Options: ',options
                        self.hsm_dialogue(node, ask, options)
                        self.answerTimer.start(15000)
                        self.answer()
                        self.hide_buttons()

                        for k, v in self.hsm_evidence.iteritems():
                            n.setEvidence(k, v)

            n.updateBeliefs()
            result = n.getOutcomeId('decision', argmax(n.getNodeValue('decision')))
            # print 'Decision: ', result


            return result
        else:
            return node

    def hid_decision(self, node):
        result = self.make_decision(node)
        #self.decision_path.append(result)

        if result is not None:
            self.node = result
            if self.hid.successors(result):
                # self.decision.emit(result)
                return self.hid_decision(result)
            else:
                # self.decision.emit(result)
                self.messages.setCurrentCharFormat(self.decisionFormat)
                self.messages.append('[%s] Decision: %s'%(self.timestamp(),result))
                print 'Decision path: ', nx.shortest_path(self.hid, 'gui', self.node)
                return result
        else:
            return 'User input required'

    def check_files(self):
        for node in self.hid.nodes():
            print '***'*15
            print 'Node: ', node
            print 'HID decision', self.hid_decision(node)
            #if self.hid.successors(node):
            #    self.make_decision(node)

    @pyqtSlot(str, str)
    def update_evidence(self, key, value):
        sender = self.sender()
        print 'Key: %s Value: %s' % (key, value)
        k = str(key)
        v = str(value)
        self.key = k
        #TODO Check if there is a better place to do this
        self.hide_buttons()
        self.hsm_node = None
        self.question = None
        self.hsm_evidence = {}
        self.answerTimer.stop()



        if self.evidence.has_key(k):
            if not self.evidence.get(k) == v:
                self.evidence[k] = v
                if not self.small_pause.isActive() and self.AUItoggleButton.isChecked():
                    self.small_pause.singleShot(5000, self.update_decision)
        else:
            'Error: %s is not yet in evidence.' % key

    def update_decision(self):
        print 'Evidence: ', self.evidence
        if self.AUItoggleButton.isChecked():
            path = nx.shortest_path(self.hid, 'gui', self.node)
            parent = path.pop()
            path.reverse()
            for p in path:
                if self.key in self.hid.node[p]['evidence']:
                    parent = p

            self.node = self.hid_decision(parent)
            self.decision.emit(self.node)

    def closeEvent(self, event):
        self.answerTimer.stop()
        shutdownJVM()

    def hide_buttons(self):
        for b in self.buttonGroup.buttons():
            b.setVisible(False)


    def hsm_dialogue(self, node, question, options=None):
        print 'ID: %s Question: %s'%(node, question)
        if node != self.hsm_node:
            self.hsm_node = node

        self.question = question

        self.hide_buttons()

        self.hsm_evidence.clear()

        b = 0
        for k, v in sorted(options.iteritems(), key= options.get):
            if not isclose(v,0):
                self.buttonGroup.button(b).setVisible(True)
                self.buttonGroup.button(b).setText(k)
                b += 1

        message = '[%s] '%self.timestamp()
        self.messages.setCurrentCharFormat(self.questionFormat)

        if question == 'C1_View':
            message = message + 'Add Camera 1?'
        if question == 'C2_Parent':
            message = message + 'Location of Camera 2?'
        if question == 'LM_View':
            message = message + 'Add Local Map?'
        if question == 'GM_Parent':
            message = message + 'Location of Global Map?'
        if question == 'PC_Parent':
            message = message + 'Location of Point Cloud?'
        if question == 'AV':
            message = message + 'Visibility of Additional Views?'
        if question == 'View_Content':
            message = message + 'Display views appropriate context?'
        if question == 'Snapshot':
            message = message + 'Resize Snapshot?'
        if question == 'AS':
            message = message + 'Visibility of Additional Snapshots?'
        if question == 'Battery':
            message = message + 'Visibility of Battery information?'
        if question == 'Wifi':
            message = message + 'Visibility of Wifi information?'

        self.messages.append(message)

    def answer(self):
        no_answer = True
        while self.answerTimer.isActive():
            QApplication.processEvents()


    def atomic_decision(self, button):
        self.hsm_evidence[self.question] = str(button.text())
        self.answerTimer.stop()
        self.hide_buttons()
        message = '[%s] User input: %s'%(self.timestamp(), button.text())
        self.messages.setCurrentCharFormat(self.questionFormat)
        self.messages.append(message)


def main():
    app = QtGui.QApplication(sys.argv)
    mi = MixedInitiative(None)
    mi.show()
    # mi.check_files()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
