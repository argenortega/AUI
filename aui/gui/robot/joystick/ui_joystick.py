# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/joystick.ui'
#
# Created: Tue Aug 18 02:07:26 2015
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

class Ui_joystickWidget(object):
    def setupUi(self, joystickWidget):
        joystickWidget.setObjectName(_fromUtf8("joystickWidget"))
        joystickWidget.resize(150, 150)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(joystickWidget.sizePolicy().hasHeightForWidth())
        joystickWidget.setSizePolicy(sizePolicy)
        joystickWidget.setMinimumSize(QtCore.QSize(100, 100))
        joystickWidget.setMaximumSize(QtCore.QSize(150, 155))
        joystickWidget.setSizeIncrement(QtCore.QSize(1, 1))
        font = QtGui.QFont()
        font.setPointSize(12)
        joystickWidget.setFont(font)
        joystickWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.gridLayout_2 = QtGui.QGridLayout(joystickWidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.joystickControl = QtGui.QGroupBox(joystickWidget)
        self.joystickControl.setObjectName(_fromUtf8("joystickControl"))
        self.gridLayout = QtGui.QGridLayout(self.joystickControl)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.stackedWidget = QtGui.QStackedWidget(self.joystickControl)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.toggle = QtGui.QWidget()
        self.toggle.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.toggle.setObjectName(_fromUtf8("toggle"))
        self.gridLayout_3 = QtGui.QGridLayout(self.toggle)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.d = QtGui.QPushButton(self.toggle)
        self.d.setMinimumSize(QtCore.QSize(44, 44))
        self.d.setStyleSheet(_fromUtf8("QPushButton{    \n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    background-color: rgb(76, 175, 80);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
""))
        self.d.setCheckable(True)
        self.d.setAutoExclusive(True)
        self.d.setFlat(True)
        self.d.setObjectName(_fromUtf8("d"))
        self.gridLayout_3.addWidget(self.d, 5, 3, 1, 1)
        self.l = QtGui.QPushButton(self.toggle)
        self.l.setMinimumSize(QtCore.QSize(44, 44))
        self.l.setStyleSheet(_fromUtf8("QPushButton{    \n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    background-color: rgb(76, 175, 80);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
""))
        self.l.setCheckable(True)
        self.l.setAutoExclusive(True)
        self.l.setFlat(True)
        self.l.setObjectName(_fromUtf8("l"))
        self.gridLayout_3.addWidget(self.l, 3, 0, 1, 1)
        self.tl = QtGui.QPushButton(self.toggle)
        self.tl.setMinimumSize(QtCore.QSize(44, 44))
        self.tl.setStyleSheet(_fromUtf8("QPushButton{    \n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    background-color: rgb(76, 175, 80);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
""))
        self.tl.setCheckable(True)
        self.tl.setAutoExclusive(True)
        self.tl.setFlat(True)
        self.tl.setObjectName(_fromUtf8("tl"))
        self.gridLayout_3.addWidget(self.tl, 0, 0, 1, 1)
        self.dl = QtGui.QPushButton(self.toggle)
        self.dl.setMinimumSize(QtCore.QSize(44, 44))
        self.dl.setStyleSheet(_fromUtf8("QPushButton{    \n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    background-color: rgb(76, 175, 80);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
""))
        self.dl.setCheckable(True)
        self.dl.setAutoExclusive(True)
        self.dl.setAutoDefault(True)
        self.dl.setDefault(True)
        self.dl.setFlat(True)
        self.dl.setObjectName(_fromUtf8("dl"))
        self.gridLayout_3.addWidget(self.dl, 5, 0, 1, 1)
        self.u = QtGui.QPushButton(self.toggle)
        self.u.setMinimumSize(QtCore.QSize(44, 44))
        self.u.setStyleSheet(_fromUtf8("QPushButton{    \n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    background-color: rgb(76, 175, 80);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
""))
        self.u.setCheckable(True)
        self.u.setAutoExclusive(True)
        self.u.setFlat(True)
        self.u.setObjectName(_fromUtf8("u"))
        self.gridLayout_3.addWidget(self.u, 0, 3, 1, 1)
        self.c = QtGui.QPushButton(self.toggle)
        self.c.setMinimumSize(QtCore.QSize(44, 44))
        self.c.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.c.setStyleSheet(_fromUtf8("QPushButton{    \n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    background-color: rgb(76, 175, 80);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
""))
        self.c.setCheckable(True)
        self.c.setChecked(True)
        self.c.setAutoExclusive(True)
        self.c.setFlat(True)
        self.c.setObjectName(_fromUtf8("c"))
        self.gridLayout_3.addWidget(self.c, 3, 3, 1, 1)
        self.tr = QtGui.QPushButton(self.toggle)
        self.tr.setMinimumSize(QtCore.QSize(44, 44))
        self.tr.setStyleSheet(_fromUtf8("QPushButton{    \n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    background-color: rgb(76, 175, 80);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
""))
        self.tr.setCheckable(True)
        self.tr.setAutoExclusive(True)
        self.tr.setFlat(True)
        self.tr.setObjectName(_fromUtf8("tr"))
        self.gridLayout_3.addWidget(self.tr, 0, 4, 1, 1)
        self.r = QtGui.QPushButton(self.toggle)
        self.r.setMinimumSize(QtCore.QSize(44, 44))
        self.r.setStyleSheet(_fromUtf8("QPushButton{    \n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    background-color: rgb(76, 175, 80);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
""))
        self.r.setCheckable(True)
        self.r.setAutoExclusive(True)
        self.r.setFlat(True)
        self.r.setObjectName(_fromUtf8("r"))
        self.gridLayout_3.addWidget(self.r, 3, 4, 1, 1)
        self.dr = QtGui.QPushButton(self.toggle)
        self.dr.setMinimumSize(QtCore.QSize(44, 44))
        self.dr.setStyleSheet(_fromUtf8("QPushButton{    \n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    background-color: rgb(76, 175, 80);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
""))
        self.dr.setCheckable(True)
        self.dr.setAutoExclusive(True)
        self.dr.setFlat(True)
        self.dr.setObjectName(_fromUtf8("dr"))
        self.gridLayout_3.addWidget(self.dr, 5, 4, 1, 1)
        self.stackedWidget.addWidget(self.toggle)
        self.sustained = QtGui.QWidget()
        self.sustained.setObjectName(_fromUtf8("sustained"))
        self.gridLayout_4 = QtGui.QGridLayout(self.sustained)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.topleft = QtGui.QLabel(self.sustained)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.topleft.setFont(font)
        self.topleft.setFrameShape(QtGui.QFrame.StyledPanel)
        self.topleft.setScaledContents(True)
        self.topleft.setAlignment(QtCore.Qt.AlignCenter)
        self.topleft.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.topleft.setObjectName(_fromUtf8("topleft"))
        self.gridLayout_4.addWidget(self.topleft, 0, 0, 1, 1)
        self.left = QtGui.QLabel(self.sustained)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.left.setFont(font)
        self.left.setFrameShape(QtGui.QFrame.StyledPanel)
        self.left.setScaledContents(True)
        self.left.setAlignment(QtCore.Qt.AlignCenter)
        self.left.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.left.setObjectName(_fromUtf8("left"))
        self.gridLayout_4.addWidget(self.left, 1, 0, 1, 1)
        self.center = QtGui.QLabel(self.sustained)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.center.setFont(font)
        self.center.setFrameShape(QtGui.QFrame.StyledPanel)
        self.center.setScaledContents(True)
        self.center.setAlignment(QtCore.Qt.AlignCenter)
        self.center.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.center.setObjectName(_fromUtf8("center"))
        self.gridLayout_4.addWidget(self.center, 1, 1, 1, 1)
        self.right = QtGui.QLabel(self.sustained)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.right.setFont(font)
        self.right.setFrameShape(QtGui.QFrame.StyledPanel)
        self.right.setScaledContents(True)
        self.right.setAlignment(QtCore.Qt.AlignCenter)
        self.right.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.right.setObjectName(_fromUtf8("right"))
        self.gridLayout_4.addWidget(self.right, 1, 2, 1, 1)
        self.up = QtGui.QLabel(self.sustained)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.up.setFont(font)
        self.up.setFrameShape(QtGui.QFrame.StyledPanel)
        self.up.setScaledContents(True)
        self.up.setAlignment(QtCore.Qt.AlignCenter)
        self.up.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.up.setObjectName(_fromUtf8("up"))
        self.gridLayout_4.addWidget(self.up, 0, 1, 1, 1)
        self.topright = QtGui.QLabel(self.sustained)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.topright.setFont(font)
        self.topright.setFrameShape(QtGui.QFrame.StyledPanel)
        self.topright.setScaledContents(True)
        self.topright.setAlignment(QtCore.Qt.AlignCenter)
        self.topright.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.topright.setObjectName(_fromUtf8("topright"))
        self.gridLayout_4.addWidget(self.topright, 0, 2, 1, 1)
        self.downleft = QtGui.QLabel(self.sustained)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.downleft.setFont(font)
        self.downleft.setFrameShape(QtGui.QFrame.StyledPanel)
        self.downleft.setFrameShadow(QtGui.QFrame.Plain)
        self.downleft.setScaledContents(True)
        self.downleft.setAlignment(QtCore.Qt.AlignCenter)
        self.downleft.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.downleft.setObjectName(_fromUtf8("downleft"))
        self.gridLayout_4.addWidget(self.downleft, 3, 0, 1, 1)
        self.down = QtGui.QLabel(self.sustained)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.down.setFont(font)
        self.down.setFrameShape(QtGui.QFrame.StyledPanel)
        self.down.setFrameShadow(QtGui.QFrame.Plain)
        self.down.setScaledContents(True)
        self.down.setAlignment(QtCore.Qt.AlignCenter)
        self.down.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.down.setObjectName(_fromUtf8("down"))
        self.gridLayout_4.addWidget(self.down, 3, 1, 1, 1)
        self.downright = QtGui.QLabel(self.sustained)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.downright.setFont(font)
        self.downright.setFrameShape(QtGui.QFrame.StyledPanel)
        self.downright.setFrameShadow(QtGui.QFrame.Plain)
        self.downright.setScaledContents(True)
        self.downright.setAlignment(QtCore.Qt.AlignCenter)
        self.downright.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.downright.setObjectName(_fromUtf8("downright"))
        self.gridLayout_4.addWidget(self.downright, 3, 2, 1, 1)
        self.stackedWidget.addWidget(self.sustained)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.joystickControl, 0, 0, 1, 1)

        self.retranslateUi(joystickWidget)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(joystickWidget)

    def retranslateUi(self, joystickWidget):
        self.joystickControl.setTitle(_translate("joystickWidget", "Joystick", None))
        self.d.setText(_translate("joystickWidget", "↓", None))
        self.l.setText(_translate("joystickWidget", "←", None))
        self.tl.setText(_translate("joystickWidget", "↖︎", None))
        self.dl.setText(_translate("joystickWidget", "↙︎", None))
        self.u.setText(_translate("joystickWidget", "↑", None))
        self.c.setText(_translate("joystickWidget", "•", None))
        self.tr.setText(_translate("joystickWidget", "↗︎", None))
        self.r.setText(_translate("joystickWidget", "→", None))
        self.dr.setText(_translate("joystickWidget", "↘︎", None))
        self.topleft.setText(_translate("joystickWidget", "↖︎", None))
        self.left.setText(_translate("joystickWidget", "←", None))
        self.center.setText(_translate("joystickWidget", "•", None))
        self.right.setText(_translate("joystickWidget", "→", None))
        self.up.setText(_translate("joystickWidget", "↑", None))
        self.topright.setText(_translate("joystickWidget", "↗︎", None))
        self.downleft.setText(_translate("joystickWidget", "↙︎", None))
        self.down.setText(_translate("joystickWidget", "↓", None))
        self.downright.setText(_translate("joystickWidget", "↘︎", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    joystickWidget = QtGui.QWidget()
    ui = Ui_joystickWidget()
    ui.setupUi(joystickWidget)
    joystickWidget.show()
    sys.exit(app.exec_())

