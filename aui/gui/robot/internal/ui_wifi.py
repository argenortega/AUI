# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/wifi.ui'
#
# Created: Thu Jul  2 13:42:17 2015
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
        WifiStatus.resize(147, 100)
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
        self.wifiLevel.setObjectName(_fromUtf8("wifiLevel"))
        self.wifiLayout = QtGui.QVBoxLayout(self.wifiLevel)
        self.wifiLayout.setMargin(3)
        self.wifiLayout.setObjectName(_fromUtf8("wifiLayout"))
        self.wifiBoxLevel = QtGui.QHBoxLayout()
        self.wifiBoxLevel.setSpacing(1)
        self.wifiBoxLevel.setObjectName(_fromUtf8("wifiBoxLevel"))
        self.wifi = CProgressBar(self.wifiLevel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wifi.sizePolicy().hasHeightForWidth())
        self.wifi.setSizePolicy(sizePolicy)
        self.wifi.setProperty("value", 100)
        self.wifi.setAlignment(QtCore.Qt.AlignCenter)
        self.wifi.setTextVisible(False)
        self.wifi.setInvertedAppearance(False)
        self.wifi.setObjectName(_fromUtf8("wifi"))
        self.wifiBoxLevel.addWidget(self.wifi)
        self.value = QtGui.QLabel(self.wifiLevel)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.value.setFont(font)
        self.value.setObjectName(_fromUtf8("value"))
        self.wifiBoxLevel.addWidget(self.value)
        self.p = QtGui.QLabel(self.wifiLevel)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.p.setFont(font)
        self.p.setObjectName(_fromUtf8("p"))
        self.wifiBoxLevel.addWidget(self.p)
        self.wifiLayout.addLayout(self.wifiBoxLevel)
        self.repair = HButton(self.wifiLevel)
        self.repair.setMinimumSize(QtCore.QSize(0, 44))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.repair.setFont(font)
        self.repair.setObjectName(_fromUtf8("repair"))
        self.wifiLayout.addWidget(self.repair)
        self.horizontalLayout_2.addWidget(self.wifiLevel)

        self.retranslateUi(WifiStatus)
        QtCore.QObject.connect(self.repair, QtCore.SIGNAL(_fromUtf8("clicked()")), self.wifi.reset)
        QtCore.QObject.connect(self.wifi, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.value.setNum)
        QtCore.QMetaObject.connectSlotsByName(WifiStatus)

    def retranslateUi(self, WifiStatus):
        WifiStatus.setWindowTitle(_translate("WifiStatus", "Form", None))
        self.wifiLevel.setTitle(_translate("WifiStatus", "WiFi", None))
        self.value.setText(_translate("WifiStatus", "100", None))
        self.p.setText(_translate("WifiStatus", "%", None))
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

