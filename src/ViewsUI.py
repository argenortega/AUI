# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Views.ui'
#
# Created: Mon Apr 13 00:34:06 2015
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
        viewsWidget.resize(682, 117)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(viewsWidget.sizePolicy().hasHeightForWidth())
        viewsWidget.setSizePolicy(sizePolicy)
        viewsWidget.setMinimumSize(QtCore.QSize(0, 70))
        viewsWidget.setMaximumSize(QtCore.QSize(16777215, 150))
        self.horizontalLayout = QtGui.QHBoxLayout(viewsWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.viewsGroup = QtGui.QGroupBox(viewsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewsGroup.sizePolicy().hasHeightForWidth())
        self.viewsGroup.setSizePolicy(sizePolicy)
        self.viewsGroup.setMinimumSize(QtCore.QSize(0, 70))
        self.viewsGroup.setBaseSize(QtCore.QSize(0, 70))
        self.viewsGroup.setObjectName(_fromUtf8("viewsGroup"))
        self.viewsGroupLayout = QtGui.QHBoxLayout(self.viewsGroup)
        self.viewsGroupLayout.setMargin(0)
        self.viewsGroupLayout.setObjectName(_fromUtf8("viewsGroupLayout"))
        self.horizontalLayout.addWidget(self.viewsGroup)
        self.pushButton = QtGui.QPushButton(viewsWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(44, 44))
        self.pushButton.setMaximumSize(QtCore.QSize(44, 44))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi(viewsWidget)
        QtCore.QMetaObject.connectSlotsByName(viewsWidget)

    def retranslateUi(self, viewsWidget):
        viewsWidget.setWindowTitle(_translate("viewsWidget", "Form", None))
        self.viewsGroup.setTitle(_translate("viewsWidget", "Available Views", None))
        self.pushButton.setText(_translate("viewsWidget", "-", None))

