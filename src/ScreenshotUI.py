# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/Screenshot.ui'
#
# Created: Fri Feb 27 23:45:24 2015
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
        ScreenshotWidget.resize(252, 439)
        ScreenshotWidget.setMouseTracking(True)
        self.layout = QtGui.QVBoxLayout(ScreenshotWidget)
        self.layout.setMargin(1)
        self.layout.setObjectName(_fromUtf8("layout"))
        self.currentScreenshot = QtGui.QLabel(ScreenshotWidget)
        self.currentScreenshot.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.currentScreenshot.sizePolicy().hasHeightForWidth())
        self.currentScreenshot.setSizePolicy(sizePolicy)
        self.currentScreenshot.setMinimumSize(QtCore.QSize(250, 250))
        self.currentScreenshot.setMaximumSize(QtCore.QSize(300, 300))
        self.currentScreenshot.setSizeIncrement(QtCore.QSize(1, 1))
        self.currentScreenshot.setBaseSize(QtCore.QSize(1, 1))
        self.currentScreenshot.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.currentScreenshot.setMouseTracking(True)
        self.currentScreenshot.setFrameShape(QtGui.QFrame.StyledPanel)
        self.currentScreenshot.setFrameShadow(QtGui.QFrame.Sunken)
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
        self.newS.setMouseTracking(True)
        self.newS.setObjectName(_fromUtf8("newS"))
        self.buttonLayout.addWidget(self.newS)
        self.layout.addLayout(self.buttonLayout)
        self.extraScreenGroup = QtGui.QGroupBox(ScreenshotWidget)
        self.extraScreenGroup.setObjectName(_fromUtf8("extraScreenGroup"))
        self.extraScreenshotGroupLayout = QtGui.QVBoxLayout(self.extraScreenGroup)
        self.extraScreenshotGroupLayout.setMargin(6)
        self.extraScreenshotGroupLayout.setObjectName(_fromUtf8("extraScreenshotGroupLayout"))
        self.showLayout = QtGui.QHBoxLayout()
        self.showLayout.setObjectName(_fromUtf8("showLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.showLayout.addItem(spacerItem1)
        self.showB = QtGui.QPushButton(self.extraScreenGroup)
        self.showB.setMouseTracking(True)
        self.showB.setCheckable(True)
        self.showB.setObjectName(_fromUtf8("showB"))
        self.showLayout.addWidget(self.showB)
        self.extraScreenshotGroupLayout.addLayout(self.showLayout)
        self.layout.addWidget(self.extraScreenGroup)

        self.retranslateUi(ScreenshotWidget)
        QtCore.QMetaObject.connectSlotsByName(ScreenshotWidget)

    def retranslateUi(self, ScreenshotWidget):
        ScreenshotWidget.setWindowTitle(_translate("ScreenshotWidget", "Form", None))
        self.currentScreenshot.setText(_translate("ScreenshotWidget", "Image 1", None))
        self.newS.setText(_translate("ScreenshotWidget", "New", None))
        self.extraScreenGroup.setTitle(_translate("ScreenshotWidget", "Screenshots", None))
        self.showB.setText(_translate("ScreenshotWidget", "Hide", None))

