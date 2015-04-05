# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Views.ui'
#
# Created: Mon Apr  6 01:22:42 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_viewsWidget(object):
    def setupUi(self, viewsWidget):
        viewsWidget.setObjectName(_fromUtf8("viewsWidget"))
        viewsWidget.resize(550, 101)
        viewsWidget.setMinimumSize(QtCore.QSize(550, 70))
        viewsWidget.setMaximumSize(QtCore.QSize(5000, 150))
        self.viewsGroupLayout = QtGui.QHBoxLayout(viewsWidget)
        self.viewsGroupLayout.setObjectName(_fromUtf8("viewsGroupLayout"))

        self.retranslateUi(viewsWidget)
        QtCore.QMetaObject.connectSlotsByName(viewsWidget)

    def retranslateUi(self, viewsWidget):
        viewsWidget.setTitle(_translate("viewsWidget", "Available Views", None))

