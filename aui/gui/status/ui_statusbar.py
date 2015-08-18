# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/statusbar.ui'
#
# Created: Tue Aug 18 00:07:26 2015
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

class Ui_statusBarWidget(object):
    def setupUi(self, statusBarWidget):
        statusBarWidget.setObjectName(_fromUtf8("statusBarWidget"))
        statusBarWidget.resize(556, 35)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(statusBarWidget.sizePolicy().hasHeightForWidth())
        statusBarWidget.setSizePolicy(sizePolicy)
        statusBarWidget.setMinimumSize(QtCore.QSize(0, 35))
        statusBarWidget.setMaximumSize(QtCore.QSize(16777215, 35))
        statusBarWidget.setStyleSheet(_fromUtf8("background-color: rgb(154, 154, 154);"))
        self.statusBarLayout = QtGui.QHBoxLayout(statusBarWidget)
        self.statusBarLayout.setSpacing(2)
        self.statusBarLayout.setContentsMargins(5, 4, 5, 4)
        self.statusBarLayout.setObjectName(_fromUtf8("statusBarLayout"))
        self.batteryStatus = CButton(statusBarWidget)
        self.batteryStatus.setMinimumSize(QtCore.QSize(60, 25))
        self.batteryStatus.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.batteryStatus.setFont(font)
        self.batteryStatus.setFlat(True)
        self.batteryStatus.setObjectName(_fromUtf8("batteryStatus"))
        self.statusBarLayout.addWidget(self.batteryStatus)
        self.batteryBar = CProgressBar(statusBarWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batteryBar.sizePolicy().hasHeightForWidth())
        self.batteryBar.setSizePolicy(sizePolicy)
        self.batteryBar.setMinimumSize(QtCore.QSize(0, 25))
        self.batteryBar.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.batteryBar.setFont(font)
        self.batteryBar.setProperty("value", 100)
        self.batteryBar.setAlignment(QtCore.Qt.AlignCenter)
        self.batteryBar.setObjectName(_fromUtf8("batteryBar"))
        self.statusBarLayout.addWidget(self.batteryBar)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.statusBarLayout.addItem(spacerItem)
        self.adaptiveStatus = QtGui.QPushButton(statusBarWidget)
        self.adaptiveStatus.setMinimumSize(QtCore.QSize(60, 25))
        self.adaptiveStatus.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.adaptiveStatus.setFont(font)
        self.adaptiveStatus.setStyleSheet(_fromUtf8("QPushButton{\n"
"            border-style: transparent;\n"
"            border-width: 1px;\n"
"            border-radius: 6px;\n"
"            background-color: rgb(244, 67, 54);\n"
"            color: rgb(255, 255, 255);\n"
"            }\n"
"QPushButton:checked {\n"
"            border-style: solid;\n"
"            border-width: 1px;\n"
"            border-radius: 6px;\n"
"            background-color: rgb(76, 175, 80);\n"
"            color: rgb(255, 255, 255);\n"
"            }"))
        self.adaptiveStatus.setCheckable(True)
        self.adaptiveStatus.setFlat(True)
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
        self.wifiBar.setMinimumSize(QtCore.QSize(0, 25))
        self.wifiBar.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wifiBar.setFont(font)
        self.wifiBar.setProperty("value", 100)
        self.wifiBar.setAlignment(QtCore.Qt.AlignCenter)
        self.wifiBar.setObjectName(_fromUtf8("wifiBar"))
        self.statusBarLayout.addWidget(self.wifiBar)
        self.wifiStatus = CButton(statusBarWidget)
        self.wifiStatus.setMinimumSize(QtCore.QSize(60, 25))
        self.wifiStatus.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wifiStatus.setFont(font)
        self.wifiStatus.setFlat(True)
        self.wifiStatus.setObjectName(_fromUtf8("wifiStatus"))
        self.statusBarLayout.addWidget(self.wifiStatus)

        self.retranslateUi(statusBarWidget)
        QtCore.QMetaObject.connectSlotsByName(statusBarWidget)

    def retranslateUi(self, statusBarWidget):
        statusBarWidget.setWindowTitle(_translate("statusBarWidget", "Frame", None))
        self.batteryStatus.setText(_translate("statusBarWidget", "Battery", None))
        self.adaptiveStatus.setText(_translate("statusBarWidget", "Adaptive", None))
        self.wifiStatus.setText(_translate("statusBarWidget", "Wifi", None))

from aui.mi.visual import CButton, CProgressBar

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    statusBarWidget = QtGui.QFrame()
    ui = Ui_statusBarWidget()
    ui.setupUi(statusBarWidget)
    statusBarWidget.show()
    sys.exit(app.exec_())

