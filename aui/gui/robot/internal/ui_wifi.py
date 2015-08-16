# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/wifi.ui'
#
# Created: Sun Aug 16 14:17:50 2015
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

class Ui_WifiStatus(object):
    def setupUi(self, WifiStatus):
        WifiStatus.setObjectName(_fromUtf8("WifiStatus"))
        WifiStatus.resize(138, 98)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WifiStatus.sizePolicy().hasHeightForWidth())
        WifiStatus.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(WifiStatus)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.wifiLevel = QtGui.QGroupBox(WifiStatus)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wifiLevel.sizePolicy().hasHeightForWidth())
        self.wifiLevel.setSizePolicy(sizePolicy)
        self.wifiLevel.setCheckable(True)
        self.wifiLevel.setObjectName(_fromUtf8("wifiLevel"))
        self.wifiLayout = QtGui.QVBoxLayout(self.wifiLevel)
        self.wifiLayout.setMargin(3)
        self.wifiLayout.setObjectName(_fromUtf8("wifiLayout"))
        self.frame = QtGui.QFrame(self.wifiLevel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.wifiBoxLevel = QtGui.QHBoxLayout()
        self.wifiBoxLevel.setSpacing(-1)
        self.wifiBoxLevel.setObjectName(_fromUtf8("wifiBoxLevel"))
        self.wifi = CProgressBar(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wifi.sizePolicy().hasHeightForWidth())
        self.wifi.setSizePolicy(sizePolicy)
        self.wifi.setMinimumSize(QtCore.QSize(0, 25))
        self.wifi.setProperty("value", 100)
        self.wifi.setAlignment(QtCore.Qt.AlignCenter)
        self.wifi.setObjectName(_fromUtf8("wifi"))
        self.wifiBoxLevel.addWidget(self.wifi)
        self.verticalLayout.addLayout(self.wifiBoxLevel)
        self.repair = HButton(self.frame)
        self.repair.setMinimumSize(QtCore.QSize(0, 44))
        self.repair.setStyleSheet(_fromUtf8(""))
        self.repair.setObjectName(_fromUtf8("repair"))
        self.verticalLayout.addWidget(self.repair)
        self.wifiLayout.addWidget(self.frame)
        self.horizontalLayout_2.addWidget(self.wifiLevel)

        self.retranslateUi(WifiStatus)
        QtCore.QObject.connect(self.wifiLevel, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.frame.setVisible)
        QtCore.QMetaObject.connectSlotsByName(WifiStatus)

    def retranslateUi(self, WifiStatus):
        WifiStatus.setWindowTitle(_translate("WifiStatus", "Form", None))
        self.wifiLevel.setTitle(_translate("WifiStatus", "WiFi", None))
        self.repair.setText(_translate("WifiStatus", "Repair", None))

from aui.utilities.ColorProgressBar import CProgressBar
from aui.utilities.HoverButtons import HButton

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WifiStatus = QtGui.QWidget()
    ui = Ui_WifiStatus()
    ui.setupUi(WifiStatus)
    WifiStatus.show()
    sys.exit(app.exec_())

