# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/wifi.ui'
#
# Created: Mon Aug 31 12:21:34 2015
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
        WifiStatus.resize(105, 108)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(WifiStatus.sizePolicy().hasHeightForWidth())
        WifiStatus.setSizePolicy(sizePolicy)
        WifiStatus.setMinimumSize(QtCore.QSize(100, 0))
        WifiStatus.setMaximumSize(QtCore.QSize(150, 16777215))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(WifiStatus)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.wifiLevel = QtGui.QGroupBox(WifiStatus)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wifiLevel.sizePolicy().hasHeightForWidth())
        self.wifiLevel.setSizePolicy(sizePolicy)
        self.wifiLevel.setMinimumSize(QtCore.QSize(0, 30))
        self.wifiLevel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.wifiLevel.setFont(font)
        self.wifiLevel.setCheckable(True)
        self.wifiLevel.setObjectName(_fromUtf8("wifiLevel"))
        self.wifiLayout = QtGui.QVBoxLayout(self.wifiLevel)
        self.wifiLayout.setSpacing(0)
        self.wifiLayout.setMargin(0)
        self.wifiLayout.setObjectName(_fromUtf8("wifiLayout"))
        self.frame = QtGui.QFrame(self.wifiLevel)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
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
        self.verticalLayout.addWidget(self.wifi)
        self.repair = QtGui.QPushButton(self.frame)
        self.repair.setMinimumSize(QtCore.QSize(44, 44))
        self.repair.setStyleSheet(_fromUtf8("QPushButton{    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-color: rgb(193, 193, 193);\n"
"    border-style: solid;\n"
"    padding: 6px;\n"
"    \n"
"}\n"
"QPushButton:pressed {    \n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    background-color: rgb(48, 131, 251);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-color: rgb(164, 205, 255);\n"
"    border-radius: 6px;\n"
"    border-width: 3px;\n"
"    border-style: solid;\n"
"}"))
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

from aui.mi.visual import CProgressBar

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WifiStatus = QtGui.QWidget()
    ui = Ui_WifiStatus()
    ui.setupUi(WifiStatus)
    WifiStatus.show()
    sys.exit(app.exec_())

