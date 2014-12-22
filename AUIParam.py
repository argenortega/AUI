# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AUIParam.ui'
#
# Created: Sun Dec 14 12:33:20 2014
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

class Ui_AUIParameters(object):
    def setupUi(self, AUIParameters):
        AUIParameters.setObjectName(_fromUtf8("AUIParameters"))
        AUIParameters.resize(300, 324)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.groupBox = QtGui.QGroupBox(self.dockWidgetContents)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 251, 80))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.progressBar = QtGui.QProgressBar(self.groupBox)
        self.progressBar.setGeometry(QtCore.QRect(20, 30, 211, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalSlider = QtGui.QSlider(self.groupBox)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 50, 211, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.groupBox_2 = QtGui.QGroupBox(self.dockWidgetContents)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 110, 251, 80))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.comboBox = QtGui.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(20, 30, 211, 26))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.groupBox_3 = QtGui.QGroupBox(self.dockWidgetContents)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 200, 251, 80))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(20, 30, 111, 31))
        self.label.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label.setFrameShadow(QtGui.QFrame.Raised)
        self.label.setObjectName(_fromUtf8("label"))
        AUIParameters.setWidget(self.dockWidgetContents)

        self.retranslateUi(AUIParameters)
        QtCore.QMetaObject.connectSlotsByName(AUIParameters)

    def retranslateUi(self, AUIParameters):
        AUIParameters.setWindowTitle(_translate("AUIParameters", "AUI Parameters", None))
        self.groupBox.setTitle(_translate("AUIParameters", "Stress Level", None))
        self.groupBox_2.setTitle(_translate("AUIParameters", "Task Context", None))
        self.groupBox_3.setTitle(_translate("AUIParameters", "Widget Attention", None))
        self.label.setText(_translate("AUIParameters", "Camera 1", None))

