# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mixed_initiative.ui'
#
# Created: Sun Sep 13 14:36:02 2015
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

class Ui_mixedInitiative(object):
    def setupUi(self, mixedInitiative):
        mixedInitiative.setObjectName(_fromUtf8("mixedInitiative"))
        mixedInitiative.resize(1056, 50)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mixedInitiative.sizePolicy().hasHeightForWidth())
        mixedInitiative.setSizePolicy(sizePolicy)
        mixedInitiative.setMinimumSize(QtCore.QSize(0, 0))
        mixedInitiative.setMaximumSize(QtCore.QSize(16777215, 200))
        mixedInitiative.setBaseSize(QtCore.QSize(0, 100))
        self.mixedInitiativeLayout = QtGui.QHBoxLayout(mixedInitiative)
        self.mixedInitiativeLayout.setSpacing(18)
        self.mixedInitiativeLayout.setContentsMargins(6, 0, 6, 0)
        self.mixedInitiativeLayout.setObjectName(_fromUtf8("mixedInitiativeLayout"))
        self.hsmWidget = QtGui.QWidget(mixedInitiative)
        self.hsmWidget.setStyleSheet(_fromUtf8("QPushButton{    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-color: rgb(193, 193, 193);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
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
"}\n"
"\n"
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
        self.hsmWidget.setObjectName(_fromUtf8("hsmWidget"))
        self.hsmLayout = QtGui.QHBoxLayout(self.hsmWidget)
        self.hsmLayout.setSpacing(15)
        self.hsmLayout.setMargin(0)
        self.hsmLayout.setObjectName(_fromUtf8("hsmLayout"))
        self.defaultButton = QtGui.QPushButton(self.hsmWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.defaultButton.sizePolicy().hasHeightForWidth())
        self.defaultButton.setSizePolicy(sizePolicy)
        self.defaultButton.setMinimumSize(QtCore.QSize(60, 44))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.defaultButton.setFont(font)
        self.defaultButton.setMouseTracking(True)
        self.defaultButton.setStyleSheet(_fromUtf8("QPushButton{    \n"
"    background-color: rgb(48, 131, 251);\n"
"    color: rgb(255, 255, 255);\n"
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
"    background-color: rgb(51, 94, 242);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-color: rgb(164, 205, 255);\n"
"    border-radius: 6px;\n"
"    border-width: 3px;\n"
"    border-style: solid;\n"
"}"))
        self.defaultButton.setAutoExclusive(True)
        self.defaultButton.setDefault(True)
        self.defaultButton.setFlat(False)
        self.defaultButton.setObjectName(_fromUtf8("defaultButton"))
        self.buttonGroup = QtGui.QButtonGroup(mixedInitiative)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.defaultButton)
        self.hsmLayout.addWidget(self.defaultButton)
        self.button2 = QtGui.QPushButton(self.hsmWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button2.sizePolicy().hasHeightForWidth())
        self.button2.setSizePolicy(sizePolicy)
        self.button2.setMinimumSize(QtCore.QSize(60, 44))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button2.setFont(font)
        self.button2.setStyleSheet(_fromUtf8("QPushButton{    \n"
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
        self.button2.setAutoExclusive(True)
        self.button2.setObjectName(_fromUtf8("button2"))
        self.buttonGroup.addButton(self.button2)
        self.hsmLayout.addWidget(self.button2)
        self.button4 = QtGui.QPushButton(self.hsmWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button4.sizePolicy().hasHeightForWidth())
        self.button4.setSizePolicy(sizePolicy)
        self.button4.setMinimumSize(QtCore.QSize(44, 44))
        self.button4.setAutoExclusive(True)
        self.button4.setObjectName(_fromUtf8("button4"))
        self.buttonGroup.addButton(self.button4)
        self.hsmLayout.addWidget(self.button4)
        self.button3 = QtGui.QPushButton(self.hsmWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button3.sizePolicy().hasHeightForWidth())
        self.button3.setSizePolicy(sizePolicy)
        self.button3.setMinimumSize(QtCore.QSize(44, 44))
        self.button3.setAutoExclusive(True)
        self.button3.setObjectName(_fromUtf8("button3"))
        self.buttonGroup.addButton(self.button3)
        self.hsmLayout.addWidget(self.button3)
        self.mixedInitiativeLayout.addWidget(self.hsmWidget)
        self.AUIMsgs = QtGui.QFrame(mixedInitiative)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AUIMsgs.sizePolicy().hasHeightForWidth())
        self.AUIMsgs.setSizePolicy(sizePolicy)
        self.AUIMsgs.setMinimumSize(QtCore.QSize(0, 50))
        self.AUIMsgs.setFrameShape(QtGui.QFrame.NoFrame)
        self.AUIMsgs.setFrameShadow(QtGui.QFrame.Plain)
        self.AUIMsgs.setObjectName(_fromUtf8("AUIMsgs"))
        self.AUIMsgsLayout = QtGui.QHBoxLayout(self.AUIMsgs)
        self.AUIMsgsLayout.setMargin(0)
        self.AUIMsgsLayout.setObjectName(_fromUtf8("AUIMsgsLayout"))
        self.messages = QtGui.QTextEdit(self.AUIMsgs)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messages.sizePolicy().hasHeightForWidth())
        self.messages.setSizePolicy(sizePolicy)
        self.messages.setMinimumSize(QtCore.QSize(650, 30))
        self.messages.setMaximumSize(QtCore.QSize(16777215, 44))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.messages.setFont(font)
        self.messages.setMouseTracking(True)
        self.messages.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.messages.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.messages.setObjectName(_fromUtf8("messages"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.messages)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.AUIMsgsLayout.addWidget(self.messages)
        self.mixedInitiativeLayout.addWidget(self.AUIMsgs)
        self.AUIStatus = QtGui.QWidget(mixedInitiative)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AUIStatus.sizePolicy().hasHeightForWidth())
        self.AUIStatus.setSizePolicy(sizePolicy)
        self.AUIStatus.setMaximumSize(QtCore.QSize(16777215, 44))
        self.AUIStatus.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.AUIStatus.setObjectName(_fromUtf8("AUIStatus"))
        self.AUIStatusLayout = QtGui.QHBoxLayout(self.AUIStatus)
        self.AUIStatusLayout.setMargin(0)
        self.AUIStatusLayout.setObjectName(_fromUtf8("AUIStatusLayout"))
        self.AUIStatusLabel = QtGui.QLabel(self.AUIStatus)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AUIStatusLabel.sizePolicy().hasHeightForWidth())
        self.AUIStatusLabel.setSizePolicy(sizePolicy)
        self.AUIStatusLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.AUIStatusLabel.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AUIStatusLabel.setFont(font)
        self.AUIStatusLabel.setMouseTracking(True)
        self.AUIStatusLabel.setScaledContents(False)
        self.AUIStatusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AUIStatusLabel.setWordWrap(False)
        self.AUIStatusLabel.setObjectName(_fromUtf8("AUIStatusLabel"))
        self.AUIStatusLayout.addWidget(self.AUIStatusLabel)
        self.AUItoggleButton = QtGui.QPushButton(self.AUIStatus)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AUItoggleButton.sizePolicy().hasHeightForWidth())
        self.AUItoggleButton.setSizePolicy(sizePolicy)
        self.AUItoggleButton.setMinimumSize(QtCore.QSize(44, 44))
        self.AUItoggleButton.setMaximumSize(QtCore.QSize(16777215, 44))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AUItoggleButton.setFont(font)
        self.AUItoggleButton.setMouseTracking(True)
        self.AUItoggleButton.setStyleSheet(_fromUtf8("QPushButton{    \n"
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
"}\n"
"\n"
"QPushButton:checked{    \n"
"    background-color: rgb(76, 175, 80);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-color: rgb(193, 193, 193);\n"
"    border-style: solid;\n"
"    padding: 6px;\n"
"    color: rgb(255, 255, 255);\n"
"}"))
        self.AUItoggleButton.setCheckable(True)
        self.AUItoggleButton.setObjectName(_fromUtf8("AUItoggleButton"))
        self.AUIStatusLayout.addWidget(self.AUItoggleButton)
        self.mixedInitiativeLayout.addWidget(self.AUIStatus)

        self.retranslateUi(mixedInitiative)
        QtCore.QMetaObject.connectSlotsByName(mixedInitiative)

    def retranslateUi(self, mixedInitiative):
        mixedInitiative.setWindowTitle(_translate("mixedInitiative", "Form", None))
        self.defaultButton.setText(_translate("mixedInitiative", "Accept", None))
        self.button2.setText(_translate("mixedInitiative", "Reject", None))
        self.button4.setText(_translate("mixedInitiative", "Opt 3", None))
        self.button3.setText(_translate("mixedInitiative", "Opt 4", None))
        self.AUIStatusLabel.setText(_translate("mixedInitiative", "AUI Status", None))
        self.AUItoggleButton.setText(_translate("mixedInitiative", "Off", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mixedInitiative = QtGui.QWidget()
    ui = Ui_mixedInitiative()
    ui.setupUi(mixedInitiative)
    mixedInitiative.show()
    sys.exit(app.exec_())

