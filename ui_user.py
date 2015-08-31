# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/user.ui'
#
# Created: Mon Aug 31 11:36:01 2015
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(457, 269)
        Dialog.setStyleSheet(_fromUtf8("QPushButton{    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-color: rgb(193, 193, 193);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    min-width: 44px;\n"
"    min-height: 44px;\n"
"    \n"
"}\n"
"QPushButton:default{    \n"
"    background-color: rgb(48, 131, 251);\n"
"    color: rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-color: rgb(193, 193, 193);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    min-width: 44px;\n"
"    min-height: 44px;\n"
"}\n"
"\n"
"QPushButton:pressed {    \n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    background-color: rgb(48, 131, 251);\n"
"    color: rgb(255, 255, 255);\n"
"    min-width: 44px;\n"
"    min-height: 44px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-color: rgb(164, 205, 255);\n"
"    border-radius: 6px;\n"
"    border-width: 3px;\n"
"    border-style: solid;\n"
"    min-width: 44px;\n"
"    min-height: 44px;\n"
"}\n"
"\n"
"QToolButton:checked{    \n"
"    border-color: rgb(48, 131, 251);\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 3px;\n"
"    border-radius: 6px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"}\n"
"QToolButton{    \n"
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
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.user = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user.sizePolicy().hasHeightForWidth())
        self.user.setSizePolicy(sizePolicy)
        self.user.setEchoMode(QtGui.QLineEdit.Normal)
        self.user.setObjectName(_fromUtf8("user"))
        self.gridLayout.addWidget(self.user, 2, 1, 1, 1)
        self.password = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName(_fromUtf8("password"))
        self.gridLayout.addWidget(self.password, 3, 1, 1, 1)
        self.teamLeaderProfile = QtGui.QToolButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teamLeaderProfile.sizePolicy().hasHeightForWidth())
        self.teamLeaderProfile.setSizePolicy(sizePolicy)
        self.teamLeaderProfile.setMinimumSize(QtCore.QSize(135, 135))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.teamLeaderProfile.setFont(font)
        self.teamLeaderProfile.setStyleSheet(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/user")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.teamLeaderProfile.setIcon(icon)
        self.teamLeaderProfile.setIconSize(QtCore.QSize(90, 100))
        self.teamLeaderProfile.setCheckable(True)
        self.teamLeaderProfile.setAutoExclusive(True)
        self.teamLeaderProfile.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.teamLeaderProfile.setObjectName(_fromUtf8("teamLeaderProfile"))
        self.buttonGroup = QtGui.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.teamLeaderProfile)
        self.gridLayout.addWidget(self.teamLeaderProfile, 0, 0, 1, 1)
        self.operatorProfile = QtGui.QToolButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.operatorProfile.sizePolicy().hasHeightForWidth())
        self.operatorProfile.setSizePolicy(sizePolicy)
        self.operatorProfile.setMinimumSize(QtCore.QSize(135, 135))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.operatorProfile.setFont(font)
        self.operatorProfile.setIcon(icon)
        self.operatorProfile.setIconSize(QtCore.QSize(90, 100))
        self.operatorProfile.setCheckable(True)
        self.operatorProfile.setChecked(True)
        self.operatorProfile.setAutoExclusive(True)
        self.operatorProfile.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.operatorProfile.setObjectName(_fromUtf8("operatorProfile"))
        self.buttonGroup.addButton(self.operatorProfile)
        self.gridLayout.addWidget(self.operatorProfile, 0, 1, 1, 1)
        self.infieldProfile = QtGui.QToolButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infieldProfile.sizePolicy().hasHeightForWidth())
        self.infieldProfile.setSizePolicy(sizePolicy)
        self.infieldProfile.setMinimumSize(QtCore.QSize(135, 135))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.infieldProfile.setFont(font)
        self.infieldProfile.setStyleSheet(_fromUtf8(""))
        self.infieldProfile.setIcon(icon)
        self.infieldProfile.setIconSize(QtCore.QSize(90, 100))
        self.infieldProfile.setCheckable(True)
        self.infieldProfile.setAutoExclusive(True)
        self.infieldProfile.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.infieldProfile.setObjectName(_fromUtf8("infieldProfile"))
        self.buttonGroup.addButton(self.infieldProfile)
        self.gridLayout.addWidget(self.infieldProfile, 0, 3, 1, 1)
        self.loginButton = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setMinimumSize(QtCore.QSize(50, 50))
        self.loginButton.setDefault(True)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.gridLayout.addWidget(self.loginButton, 4, 3, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "User Profile", None))
        self.label.setText(_translate("Dialog", "User", None))
        self.label_2.setText(_translate("Dialog", "Password", None))
        self.teamLeaderProfile.setText(_translate("Dialog", "Team Leader", None))
        self.operatorProfile.setText(_translate("Dialog", "Operator", None))
        self.infieldProfile.setText(_translate("Dialog", "Infield Responder", None))
        self.loginButton.setText(_translate("Dialog", "Login", None))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

