# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TRADR_AUI.ui'
#
# Created: Sun Dec 14 12:01:38 2014
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(770, 382)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.widget)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox = QtGui.QGroupBox(self.widget)
        self.groupBox.setEnabled(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.camera1 = QtGui.QLabel(self.groupBox)
        self.camera1.setGeometry(QtCore.QRect(-30, 10, 300, 311))
        self.camera1.setMinimumSize(QtCore.QSize(300, 300))
        self.camera1.setMouseTracking(True)
        self.camera1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.camera1.setAlignment(QtCore.Qt.AlignCenter)
        self.camera1.setMargin(1)
        self.camera1.setObjectName(_fromUtf8("camera1"))
        self.camera2 = QtGui.QLabel(self.groupBox)
        self.camera2.setGeometry(QtCore.QRect(-60, 10, 300, 314))
        self.camera2.setMinimumSize(QtCore.QSize(300, 300))
        self.camera2.setMouseTracking(True)
        self.camera2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.camera2.setAlignment(QtCore.Qt.AlignCenter)
        self.camera2.setObjectName(_fromUtf8("camera2"))
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)
        self.widget_2 = QtGui.QWidget(Form)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout.addWidget(self.widget_2, 1, 1, 1, 1)
        self.AUIParameters = QtGui.QDockWidget(Form)
        self.AUIParameters.setObjectName(_fromUtf8("AUIParameters"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.horizontalSlider = QtGui.QSlider(self.dockWidgetContents)
        self.horizontalSlider.setGeometry(QtCore.QRect(140, 150, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.dial = QtGui.QDial(self.dockWidgetContents)
        self.dial.setGeometry(QtCore.QRect(50, 60, 50, 64))
        self.dial.setObjectName(_fromUtf8("dial"))
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setGeometry(QtCore.QRect(70, 130, 56, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.lcdNumber = QtGui.QLCDNumber(self.dockWidgetContents)
        self.lcdNumber.setGeometry(QtCore.QRect(210, 20, 64, 23))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.progressBar = QtGui.QProgressBar(self.dockWidgetContents)
        self.progressBar.setGeometry(QtCore.QRect(150, 120, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.AUIParameters.setWidget(self.dockWidgetContents)
        self.gridLayout.addWidget(self.AUIParameters, 1, 2, 1, 1)
        self.widget_3 = QtGui.QWidget(Form)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.gridLayout.addWidget(self.widget_3, 2, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "GroupBox", None))
        self.camera1.setText(_translate("Form", "Camera 1", None))
        self.camera2.setText(_translate("Form", "Camera 2", None))
        self.label.setText(_translate("Form", "Stress", None))

