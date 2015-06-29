# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/snapshots.ui'
#
# Created: Mon Jun 29 15:41:24 2015
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
        ScreenshotWidget.setMinimumSize(QtCore.QSize(0, 0))
        ScreenshotWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        ScreenshotWidget.setMouseTracking(True)
        self.layout = QtGui.QVBoxLayout(ScreenshotWidget)
        self.layout.setMargin(1)
        self.layout.setObjectName(_fromUtf8("layout"))
        self.currentScreenshot = ActLabel(ScreenshotWidget)
        self.currentScreenshot.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.currentScreenshot.sizePolicy().hasHeightForWidth())
        self.currentScreenshot.setSizePolicy(sizePolicy)
        self.currentScreenshot.setMinimumSize(QtCore.QSize(250, 250))
        self.currentScreenshot.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.currentScreenshot.setSizeIncrement(QtCore.QSize(1, 1))
        self.currentScreenshot.setBaseSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.currentScreenshot.setFont(font)
        self.currentScreenshot.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.currentScreenshot.setMouseTracking(True)
        self.currentScreenshot.setAcceptDrops(True)
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
        self.newS = HButton(ScreenshotWidget)
        self.newS.setMinimumSize(QtCore.QSize(44, 44))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.newS.setFont(font)
        self.newS.setMouseTracking(True)
        self.newS.setFocusPolicy(QtCore.Qt.NoFocus)
        self.newS.setObjectName(_fromUtf8("newS"))
        self.buttonLayout.addWidget(self.newS)
        self.layout.addLayout(self.buttonLayout)
        self.extraScreenGroup = QtGui.QGroupBox(ScreenshotWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extraScreenGroup.sizePolicy().hasHeightForWidth())
        self.extraScreenGroup.setSizePolicy(sizePolicy)
        self.extraScreenGroup.setMinimumSize(QtCore.QSize(0, 0))
        self.extraScreenGroup.setBaseSize(QtCore.QSize(0, 0))
        self.extraScreenGroup.setMouseTracking(True)
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
        self.extraScreenshots.setGeometry(QtCore.QRect(0, 0, 193, 110))
        self.extraScreenshots.setMinimumSize(QtCore.QSize(0, 110))
        self.extraScreenshots.setMouseTracking(True)
        self.extraScreenshots.setObjectName(_fromUtf8("extraScreenshots"))
        self.extraScreenshotLayout = QtGui.QHBoxLayout(self.extraScreenshots)
        self.extraScreenshotLayout.setMargin(0)
        self.extraScreenshotLayout.setObjectName(_fromUtf8("extraScreenshotLayout"))
        self.scrollArea.setWidget(self.extraScreenshots)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.showB = HButton(self.extraScreenGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showB.sizePolicy().hasHeightForWidth())
        self.showB.setSizePolicy(sizePolicy)
        self.showB.setMinimumSize(QtCore.QSize(44, 44))
        self.showB.setMaximumSize(QtCore.QSize(44, 44))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.showB.setFont(font)
        self.showB.setMouseTracking(True)
        self.showB.setFocusPolicy(QtCore.Qt.NoFocus)
        self.showB.setCheckable(True)
        self.showB.setObjectName(_fromUtf8("showB"))
        self.horizontalLayout.addWidget(self.showB)
        self.layout.addWidget(self.extraScreenGroup)

        self.retranslateUi(ScreenshotWidget)
        QtCore.QMetaObject.connectSlotsByName(ScreenshotWidget)

    def retranslateUi(self, ScreenshotWidget):
        ScreenshotWidget.setWindowTitle(_translate("ScreenshotWidget", "Form", None))
        self.currentScreenshot.setText(_translate("ScreenshotWidget", "Select a screenshot", None))
        self.newS.setText(_translate("ScreenshotWidget", "New", None))
        self.extraScreenGroup.setTitle(_translate("ScreenshotWidget", "Screenshots", None))
        self.showB.setText(_translate("ScreenshotWidget", "-", None))

from aui.utilities.HoverButtons import HButton
from aui.utilities.ActiveLabel import ActLabel

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ScreenshotWidget = QtGui.QWidget()
    ui = Ui_ScreenshotWidget()
    ui.setupUi(ScreenshotWidget)
    ScreenshotWidget.show()
    sys.exit(app.exec_())

