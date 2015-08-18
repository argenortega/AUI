# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/user.ui'
#
# Created: Mon Aug 17 20:42:27 2015
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

class Ui_UserProfile(object):
    def setupUi(self, UserProfile):
        UserProfile.setObjectName(_fromUtf8("UserProfile"))
        UserProfile.resize(451, 152)
        UserProfile.setAutoFillBackground(True)
        self.horizontalLayout = QtGui.QHBoxLayout(UserProfile)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.leaderProfile = QtGui.QToolButton(UserProfile)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.leaderProfile.sizePolicy().hasHeightForWidth())
        self.leaderProfile.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.leaderProfile.setFont(font)
        self.leaderProfile.setStyleSheet(_fromUtf8("QToolButton{    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-color: rgb(193, 193, 193);\n"
"    border-style: solid;\n"
"    padding: 6px;\n"
"    \n"
"}\n"
"QToolButton:pressed {    \n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    background-color: rgb(48, 131, 251);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"    border-color: rgb(164, 205, 255);\n"
"    border-radius: 6px;\n"
"    border-width: 3px;\n"
"    border-style: solid;\n"
"}"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/user")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.leaderProfile.setIcon(icon)
        self.leaderProfile.setIconSize(QtCore.QSize(90, 100))
        self.leaderProfile.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.leaderProfile.setObjectName(_fromUtf8("leaderProfile"))
        self.horizontalLayout.addWidget(self.leaderProfile)
        self.operatorProfile = QtGui.QToolButton(UserProfile)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.operatorProfile.sizePolicy().hasHeightForWidth())
        self.operatorProfile.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.operatorProfile.setFont(font)
        self.operatorProfile.setStyleSheet(_fromUtf8("QToolButton{    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-color: rgb(193, 193, 193);\n"
"    border-style: solid;\n"
"    padding: 6px;\n"
"    \n"
"}\n"
"QToolButton:pressed {    \n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    background-color: rgb(48, 131, 251);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"    border-color: rgb(164, 205, 255);\n"
"    border-radius: 6px;\n"
"    border-width: 3px;\n"
"    border-style: solid;\n"
"}"))
        self.operatorProfile.setIcon(icon)
        self.operatorProfile.setIconSize(QtCore.QSize(90, 100))
        self.operatorProfile.setAutoExclusive(True)
        self.operatorProfile.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.operatorProfile.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.operatorProfile.setAutoRaise(True)
        self.operatorProfile.setArrowType(QtCore.Qt.NoArrow)
        self.operatorProfile.setObjectName(_fromUtf8("operatorProfile"))
        self.horizontalLayout.addWidget(self.operatorProfile)
        self.infieldProfile = QtGui.QToolButton(UserProfile)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.infieldProfile.sizePolicy().hasHeightForWidth())
        self.infieldProfile.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.infieldProfile.setFont(font)
        self.infieldProfile.setStyleSheet(_fromUtf8("QToolButton{    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-color: rgb(193, 193, 193);\n"
"    border-style: solid;\n"
"    padding: 6px;\n"
"    \n"
"}\n"
"QToolButton:pressed {    \n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    background-color: rgb(48, 131, 251);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"    border-color: rgb(164, 205, 255);\n"
"    border-radius: 6px;\n"
"    border-width: 3px;\n"
"    border-style: solid;\n"
"}"))
        self.infieldProfile.setIcon(icon)
        self.infieldProfile.setIconSize(QtCore.QSize(90, 100))
        self.infieldProfile.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.infieldProfile.setObjectName(_fromUtf8("infieldProfile"))
        self.horizontalLayout.addWidget(self.infieldProfile)

        self.retranslateUi(UserProfile)
        QtCore.QMetaObject.connectSlotsByName(UserProfile)

    def retranslateUi(self, UserProfile):
        UserProfile.setWindowTitle(_translate("UserProfile", "User Roles", None))
        self.leaderProfile.setText(_translate("UserProfile", "Team Leader", None))
        self.operatorProfile.setText(_translate("UserProfile", "Operator", None))
        self.infieldProfile.setText(_translate("UserProfile", "Infield Responder", None))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    UserProfile = QtGui.QWidget()
    ui = Ui_UserProfile()
    ui.setupUi(UserProfile)
    UserProfile.show()
    sys.exit(app.exec_())

