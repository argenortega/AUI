# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/Views.ui'
#
# Created: Sat Feb 28 00:34:17 2015
#      by: PyQt4 UI code generator 4.11.1
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

class Ui_views(object):
    def setupUi(self, views):
        views.setObjectName(_fromUtf8("views"))
        views.resize(550, 150)
        views.setMinimumSize(QtCore.QSize(550, 70))
        views.setMaximumSize(QtCore.QSize(5000, 150))
        self.viewsGroupLayout = QtGui.QHBoxLayout(views)
        self.viewsGroupLayout.setObjectName(_fromUtf8("viewsGroupLayout"))

        self.retranslateUi(views)
        QtCore.QMetaObject.connectSlotsByName(views)

    def retranslateUi(self, views):
        views.setTitle(_translate("views", "Available Views", None))

