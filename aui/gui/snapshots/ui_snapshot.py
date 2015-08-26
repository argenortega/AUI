# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/snapshot.ui'
#
# Created: Sat Aug 22 15:47:07 2015
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

class Ui_ScreenshotWidget(object):
    def setupUi(self, ScreenshotWidget):
        ScreenshotWidget.setObjectName(_fromUtf8("ScreenshotWidget"))
        ScreenshotWidget.resize(252, 514)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ScreenshotWidget.sizePolicy().hasHeightForWidth())
        ScreenshotWidget.setSizePolicy(sizePolicy)
        ScreenshotWidget.setMouseTracking(True)
        self.layout = QtGui.QVBoxLayout(ScreenshotWidget)
        self.layout.setMargin(1)
        self.layout.setObjectName(_fromUtf8("layout"))
        self.currentScreenshot = ActLabel(ScreenshotWidget)
        self.currentScreenshot.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.currentScreenshot.sizePolicy().hasHeightForWidth())
        self.currentScreenshot.setSizePolicy(sizePolicy)
        self.currentScreenshot.setMinimumSize(QtCore.QSize(250, 250))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.currentScreenshot.setFont(font)
        self.currentScreenshot.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.currentScreenshot.setMouseTracking(True)
        self.currentScreenshot.setStyleSheet(_fromUtf8("QLabel{\n"
"border-color: rgb(154, 154, 154); \n"
"border-style: solid; \n"
"border-width: 2px; \n"
"border-radius: 6px;\n"
"}"))
        self.currentScreenshot.setFrameShape(QtGui.QFrame.StyledPanel)
        self.currentScreenshot.setFrameShadow(QtGui.QFrame.Sunken)
        self.currentScreenshot.setScaledContents(True)
        self.currentScreenshot.setAlignment(QtCore.Qt.AlignCenter)
        self.currentScreenshot.setWordWrap(True)
        self.currentScreenshot.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.currentScreenshot.setObjectName(_fromUtf8("currentScreenshot"))
        self.layout.addWidget(self.currentScreenshot)
        self.buttonLayout = QtGui.QHBoxLayout()
        self.buttonLayout.setObjectName(_fromUtf8("buttonLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.buttonLayout.addItem(spacerItem)
        self.newS = QtGui.QPushButton(ScreenshotWidget)
        self.newS.setMinimumSize(QtCore.QSize(44, 44))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.newS.setFont(font)
        self.newS.setMouseTracking(True)
        self.newS.setFocusPolicy(QtCore.Qt.NoFocus)
        self.newS.setStyleSheet(_fromUtf8("QPushButton{    \n"
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
        self.newS.setObjectName(_fromUtf8("newS"))
        self.buttonLayout.addWidget(self.newS)
        self.layout.addLayout(self.buttonLayout)
        self.extraScreenGroup = FocusGroupBox(ScreenshotWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extraScreenGroup.sizePolicy().hasHeightForWidth())
        self.extraScreenGroup.setSizePolicy(sizePolicy)
        self.extraScreenGroup.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.extraScreenGroup.setFont(font)
        self.extraScreenGroup.setMouseTracking(True)
        self.extraScreenGroup.setCheckable(True)
        self.extraScreenGroup.setObjectName(_fromUtf8("extraScreenGroup"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.extraScreenGroup)
        self.horizontalLayout.setMargin(3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.scrollArea = QtGui.QScrollArea(self.extraScreenGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 110))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.scrollArea.setFont(font)
        self.scrollArea.setMouseTracking(True)
        self.scrollArea.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Plain)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.extraScreenshots = QtGui.QWidget()
        self.extraScreenshots.setGeometry(QtCore.QRect(0, 0, 238, 110))
        self.extraScreenshots.setMinimumSize(QtCore.QSize(0, 110))
        self.extraScreenshots.setMouseTracking(True)
        self.extraScreenshots.setObjectName(_fromUtf8("extraScreenshots"))
        self.extraScreenshotLayout = QtGui.QHBoxLayout(self.extraScreenshots)
        self.extraScreenshotLayout.setMargin(0)
        self.extraScreenshotLayout.setObjectName(_fromUtf8("extraScreenshotLayout"))
        self.scrollArea.setWidget(self.extraScreenshots)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.layout.addWidget(self.extraScreenGroup)

        self.retranslateUi(ScreenshotWidget)
        QtCore.QObject.connect(self.extraScreenGroup, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.scrollArea.setVisible)
        QtCore.QMetaObject.connectSlotsByName(ScreenshotWidget)

    def retranslateUi(self, ScreenshotWidget):
        ScreenshotWidget.setWindowTitle(_translate("ScreenshotWidget", "Form", None))
        self.currentScreenshot.setAccessibleName(_translate("ScreenshotWidget", "S", None))
        self.currentScreenshot.setText(_translate("ScreenshotWidget", "Select a snapshot", None))
        self.newS.setText(_translate("ScreenshotWidget", "New", None))
        self.extraScreenGroup.setAccessibleName(_translate("ScreenshotWidget", "AS", None))
        self.extraScreenGroup.setTitle(_translate("ScreenshotWidget", "Screenshots", None))

from aui.mi.visual import FocusGroupBox
from aui.utilities.ActiveLabel import ActLabel

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ScreenshotWidget = QtGui.QWidget()
    ui = Ui_ScreenshotWidget()
    ui.setupUi(ScreenshotWidget)
    ScreenshotWidget.show()
    sys.exit(app.exec_())

