# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/battery.ui'
#
# Created: Sun Aug 16 14:17:49 2015
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
        batteryStatus.resize(117, 108)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(batteryStatus.sizePolicy().hasHeightForWidth())
        batteryStatus.setSizePolicy(sizePolicy)
        self.BatteryLayout = QtGui.QVBoxLayout(batteryStatus)
        self.BatteryLayout.setSpacing(1)
        self.BatteryLayout.setMargin(0)
        self.BatteryLayout.setObjectName(_fromUtf8("BatteryLayout"))
        self.batteryLevel = QtGui.QGroupBox(batteryStatus)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batteryLevel.sizePolicy().hasHeightForWidth())
        self.batteryLevel.setSizePolicy(sizePolicy)
        self.batteryLevel.setMouseTracking(True)
        self.batteryLevel.setInputMethodHints(QtCore.Qt.ImhNone)
        self.batteryLevel.setFlat(False)
        self.batteryLevel.setCheckable(True)
        self.batteryLevel.setChecked(True)
        self.batteryLevel.setObjectName(_fromUtf8("batteryLevel"))
        self.batteryBoxLayout = QtGui.QVBoxLayout(self.batteryLevel)
        self.batteryBoxLayout.setMargin(3)
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
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.batteryBoxLevel = QtGui.QHBoxLayout()
        self.batteryBoxLevel.setSpacing(1)
        self.batteryBoxLevel.setObjectName(_fromUtf8("batteryBoxLevel"))
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
        self.batteryBoxLevel.addWidget(self.battery)
        self.verticalLayout.addLayout(self.batteryBoxLevel)
        self.charge = QtGui.QPushButton(self.frame)
        self.charge.setMinimumSize(QtCore.QSize(0, 44))
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

from aui.utilities.ColorProgressBar import CProgressBar

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    batteryStatus = QtGui.QWidget()
    ui = Ui_batteryStatus()
    ui.setupUi(batteryStatus)
    batteryStatus.show()
    sys.exit(app.exec_())

