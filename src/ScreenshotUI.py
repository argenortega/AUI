# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Screenshot.ui'
#
# Created: Mon Apr  6 01:22:41 2015
#      by: PyQt4 UI code generator 4.10.4
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
        ScreenshotWidget.resize(306, 486)
        ScreenshotWidget.setMinimumSize(QtCore.QSize(0, 30))
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
        self.newS.setMinimumSize(QtCore.QSize(0, 44))
        self.newS.setMouseTracking(True)
        self.newS.setObjectName(_fromUtf8("newS"))
        self.buttonLayout.addWidget(self.newS)
        self.layout.addLayout(self.buttonLayout)
        self.extraScreenGroup = QtGui.QGroupBox(ScreenshotWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extraScreenGroup.sizePolicy().hasHeightForWidth())
        self.extraScreenGroup.setSizePolicy(sizePolicy)
        self.extraScreenGroup.setMinimumSize(QtCore.QSize(0, 0))
        self.extraScreenGroup.setBaseSize(QtCore.QSize(0, 0))
        self.extraScreenGroup.setObjectName(_fromUtf8("extraScreenGroup"))
        self.extraScreenshotGroupLayout = QtGui.QVBoxLayout(self.extraScreenGroup)
        self.extraScreenshotGroupLayout.setMargin(0)
        self.extraScreenshotGroupLayout.setObjectName(_fromUtf8("extraScreenshotGroupLayout"))
        self.scrollArea = QtGui.QScrollArea(self.extraScreenGroup)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Plain)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.extraScreenshots = QtGui.QWidget()
        self.extraScreenshots.setGeometry(QtCore.QRect(0, 0, 298, 76))
        self.extraScreenshots.setObjectName(_fromUtf8("extraScreenshots"))
        self.extraScreenshotLayout = QtGui.QHBoxLayout(self.extraScreenshots)
        self.extraScreenshotLayout.setMargin(0)
        self.extraScreenshotLayout.setObjectName(_fromUtf8("extraScreenshotLayout"))
        self.scrollArea.setWidget(self.extraScreenshots)
        self.extraScreenshotGroupLayout.addWidget(self.scrollArea)
        self.showLayout = QtGui.QHBoxLayout()
        self.showLayout.setSpacing(-1)
        self.showLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.showLayout.setObjectName(_fromUtf8("showLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 15, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.showLayout.addItem(spacerItem1)
        self.showB = QtGui.QPushButton(self.extraScreenGroup)
        self.showB.setMinimumSize(QtCore.QSize(0, 44))
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

