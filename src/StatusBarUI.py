# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/StatusBar.ui'
#
# Created: Sun Jun 28 22:26:29 2015
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

class Ui_statusBarWidget(object):
    def setupUi(self, statusBarWidget):
        statusBarWidget.setObjectName(_fromUtf8("statusBarWidget"))
        statusBarWidget.resize(707, 35)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(statusBarWidget.sizePolicy().hasHeightForWidth())
        statusBarWidget.setSizePolicy(sizePolicy)
        statusBarWidget.setMinimumSize(QtCore.QSize(0, 35))
        statusBarWidget.setMaximumSize(QtCore.QSize(16777215, 35))
        self.statusBarLayout = QtGui.QHBoxLayout(statusBarWidget)
        self.statusBarLayout.setSpacing(2)
        self.statusBarLayout.setContentsMargins(5, 4, 5, 4)
        self.statusBarLayout.setObjectName(_fromUtf8("statusBarLayout"))
        self.batteryStatus = QtGui.QLabel(statusBarWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batteryStatus.sizePolicy().hasHeightForWidth())
        self.batteryStatus.setSizePolicy(sizePolicy)
        self.batteryStatus.setMinimumSize(QtCore.QSize(60, 25))
        self.batteryStatus.setMaximumSize(QtCore.QSize(16777215, 25))
        self.batteryStatus.setBaseSize(QtCore.QSize(30, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.batteryStatus.setFont(font)
        self.batteryStatus.setMouseTracking(True)
        self.batteryStatus.setStyleSheet(_fromUtf8("background-color: rgb(64, 128, 0);\n"
"color: rgb(255, 255, 255);"))
        self.batteryStatus.setFrameShape(QtGui.QFrame.Box)
        self.batteryStatus.setScaledContents(True)
        self.batteryStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.batteryStatus.setMargin(6)
        self.batteryStatus.setObjectName(_fromUtf8("batteryStatus"))
        self.statusBarLayout.addWidget(self.batteryStatus)
        self.batteryBar = CProgressBar(statusBarWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batteryBar.sizePolicy().hasHeightForWidth())
        self.batteryBar.setSizePolicy(sizePolicy)
        self.batteryBar.setMaximumSize(QtCore.QSize(50, 6))
        self.batteryBar.setProperty("value", 100)
        self.batteryBar.setAlignment(QtCore.Qt.AlignCenter)
        self.batteryBar.setTextVisible(False)
        self.batteryBar.setObjectName(_fromUtf8("batteryBar"))
        self.statusBarLayout.addWidget(self.batteryBar)
        self.percent2 = QtGui.QLabel(statusBarWidget)
        self.percent2.setIndent(0)
        self.percent2.setObjectName(_fromUtf8("percent2"))
        self.statusBarLayout.addWidget(self.percent2)
        self.batteryValue = QtGui.QLabel(statusBarWidget)
        self.batteryValue.setObjectName(_fromUtf8("batteryValue"))
        self.statusBarLayout.addWidget(self.batteryValue)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.statusBarLayout.addItem(spacerItem)
        self.adaptiveStatus = QtGui.QLabel(statusBarWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adaptiveStatus.sizePolicy().hasHeightForWidth())
        self.adaptiveStatus.setSizePolicy(sizePolicy)
        self.adaptiveStatus.setMinimumSize(QtCore.QSize(60, 25))
        self.adaptiveStatus.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.adaptiveStatus.setFont(font)
        self.adaptiveStatus.setMouseTracking(True)
        self.adaptiveStatus.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.adaptiveStatus.setFrameShape(QtGui.QFrame.Box)
        self.adaptiveStatus.setScaledContents(True)
        self.adaptiveStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.adaptiveStatus.setMargin(6)
        self.adaptiveStatus.setObjectName(_fromUtf8("adaptiveStatus"))
        self.statusBarLayout.addWidget(self.adaptiveStatus)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.statusBarLayout.addItem(spacerItem1)
        self.wifiBar = CProgressBar(statusBarWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wifiBar.sizePolicy().hasHeightForWidth())
        self.wifiBar.setSizePolicy(sizePolicy)
        self.wifiBar.setMaximumSize(QtCore.QSize(50, 6))
        self.wifiBar.setProperty("value", 100)
        self.wifiBar.setAlignment(QtCore.Qt.AlignCenter)
        self.wifiBar.setTextVisible(False)
        self.wifiBar.setObjectName(_fromUtf8("wifiBar"))
        self.statusBarLayout.addWidget(self.wifiBar)
        self.wifiValue = QtGui.QLabel(statusBarWidget)
        self.wifiValue.setObjectName(_fromUtf8("wifiValue"))
        self.statusBarLayout.addWidget(self.wifiValue)
        self.percent1 = QtGui.QLabel(statusBarWidget)
        self.percent1.setObjectName(_fromUtf8("percent1"))
        self.statusBarLayout.addWidget(self.percent1)
        self.wifiStatus = QtGui.QLabel(statusBarWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wifiStatus.sizePolicy().hasHeightForWidth())
        self.wifiStatus.setSizePolicy(sizePolicy)
        self.wifiStatus.setMinimumSize(QtCore.QSize(60, 25))
        self.wifiStatus.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.wifiStatus.setFont(font)
        self.wifiStatus.setMouseTracking(True)
        self.wifiStatus.setStyleSheet(_fromUtf8("background-color: rgb(64, 128, 0);\n"
"color: rgb(255, 255, 255);"))
        self.wifiStatus.setFrameShape(QtGui.QFrame.Box)
        self.wifiStatus.setScaledContents(True)
        self.wifiStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.wifiStatus.setMargin(6)
        self.wifiStatus.setObjectName(_fromUtf8("wifiStatus"))
        self.statusBarLayout.addWidget(self.wifiStatus)

        self.retranslateUi(statusBarWidget)
        QtCore.QObject.connect(self.batteryBar, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.batteryValue.setNum)
        QtCore.QObject.connect(self.wifiBar, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.wifiValue.setNum)
        QtCore.QMetaObject.connectSlotsByName(statusBarWidget)

    def retranslateUi(self, statusBarWidget):
        statusBarWidget.setWindowTitle(_translate("statusBarWidget", "Frame", None))
        self.batteryStatus.setText(_translate("statusBarWidget", "Battery", None))
        self.percent2.setText(_translate("statusBarWidget", "%", None))
        self.batteryValue.setText(_translate("statusBarWidget", "100", None))
        self.adaptiveStatus.setText(_translate("statusBarWidget", "Adaptive", None))
        self.wifiValue.setText(_translate("statusBarWidget", "100", None))
        self.percent1.setText(_translate("statusBarWidget", "%", None))
        self.wifiStatus.setText(_translate("statusBarWidget", "WiFi", None))

from utilities.ColorProgressBar import CProgressBar
