# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/AUI.ui'
#
# Created: Wed Apr 15 16:44:19 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_UI(object):
    def setupUi(self, UI):
        UI.setObjectName(_fromUtf8("UI"))
        UI.resize(400, 300)
        self.globalLayout = QtGui.QHBoxLayout(UI)
        self.globalLayout.setSpacing(1)
        self.globalLayout.setContentsMargins(6, 0, 6, 6)
        self.globalLayout.setObjectName(_fromUtf8("globalLayout"))
        self.label = QtGui.QLabel(UI)
        self.label.setObjectName(_fromUtf8("label"))
        self.globalLayout.addWidget(self.label)

        self.retranslateUi(UI)
        QtCore.QMetaObject.connectSlotsByName(UI)

    def retranslateUi(self, UI):
        UI.setWindowTitle(_translate("UI", "AUI - TRADR Proyect", None))
        self.label.setText(_translate("UI", "TextLabel", None))

