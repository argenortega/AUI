# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/battery.ui'
#
# Created: Tue Aug 18 00:21:34 2015
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

class Ui_batteryStatus(object):
    def setupUi(self, batteryStatus):
        batteryStatus.setObjectName(_fromUtf8("batteryStatus"))
        batteryStatus.resize(109, 103)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(batteryStatus.sizePolicy().hasHeightForWidth())
        batteryStatus.setSizePolicy(sizePolicy)
        batteryStatus.setMinimumSize(QtCore.QSize(100, 0))
        self.BatteryLayout = QtGui.QVBoxLayout(batteryStatus)
        self.BatteryLayout.setSpacing(0)
        self.BatteryLayout.setMargin(0)
        self.BatteryLayout.setObjectName(_fromUtf8("BatteryLayout"))
        self.batteryLevel = QtGui.QGroupBox(batteryStatus)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batteryLevel.sizePolicy().hasHeightForWidth())
        self.batteryLevel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.batteryLevel.setFont(font)
        self.batteryLevel.setMouseTracking(True)
        self.batteryLevel.setInputMethodHints(QtCore.Qt.ImhNone)
        self.batteryLevel.setFlat(False)
        self.batteryLevel.setCheckable(True)
        self.batteryLevel.setChecked(True)
        self.batteryLevel.setObjectName(_fromUtf8("batteryLevel"))
        self.batteryBoxLayout = QtGui.QVBoxLayout(self.batteryLevel)
        self.batteryBoxLayout.setSpacing(0)
        self.batteryBoxLayout.setMargin(0)
        self.batteryBoxLayout.setObjectName(_fromUtf8("batteryBoxLayout"))
        self.frame = QtGui.QFrame(self.batteryLevel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(_fromUtf8(""))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.battery = CProgressBar(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.battery.sizePolicy().hasHeightForWidth())
        self.battery.setSizePolicy(sizePolicy)
        self.battery.setMinimumSize(QtCore.QSize(0, 25))
        self.battery.setProperty("value", 100)
        self.battery.setAlignment(QtCore.Qt.AlignCenter)
        self.battery.setObjectName(_fromUtf8("battery"))
        self.verticalLayout.addWidget(self.battery)
        self.charge = QtGui.QPushButton(self.frame)
        self.charge.setMinimumSize(QtCore.QSize(44, 44))
        self.charge.setStyleSheet(_fromUtf8("QPushButton{    \n"
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
        self.charge.setObjectName(_fromUtf8("charge"))
        self.verticalLayout.addWidget(self.charge)
        self.batteryBoxLayout.addWidget(self.frame)
        self.BatteryLayout.addWidget(self.batteryLevel)

        self.retranslateUi(batteryStatus)
        QtCore.QObject.connect(self.batteryLevel, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.frame.setVisible)
        QtCore.QMetaObject.connectSlotsByName(batteryStatus)

    def retranslateUi(self, batteryStatus):
        batteryStatus.setWindowTitle(_translate("batteryStatus", "Form", None))
        self.batteryLevel.setTitle(_translate("batteryStatus", "Battery", None))
        self.charge.setText(_translate("batteryStatus", "Charge", None))

from aui.mi.visual import CProgressBar

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    batteryStatus = QtGui.QWidget()
    ui = Ui_batteryStatus()
    ui.setupUi(batteryStatus)
    batteryStatus.show()
    sys.exit(app.exec_())

