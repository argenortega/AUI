# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/image.ui'
#
# Created: Mon Jun 29 19:59:26 2015
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
        ScreenshotWidget.resize(85, 85)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(ScreenshotWidget.sizePolicy().hasHeightForWidth())
        ScreenshotWidget.setSizePolicy(sizePolicy)
        ScreenshotWidget.setMinimumSize(QtCore.QSize(85, 85))
        ScreenshotWidget.setMaximumSize(QtCore.QSize(100, 100))
        ScreenshotWidget.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        ScreenshotWidget.setMouseTracking(True)
        self.layout = QtGui.QVBoxLayout(ScreenshotWidget)
        self.layout.setMargin(0)
        self.layout.setObjectName(_fromUtf8("layout"))
        self.screenshot = ActLabel(ScreenshotWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screenshot.sizePolicy().hasHeightForWidth())
        self.screenshot.setSizePolicy(sizePolicy)
        self.screenshot.setMinimumSize(QtCore.QSize(85, 85))
        self.screenshot.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.screenshot.setFont(font)
        self.screenshot.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.screenshot.setMouseTracking(True)
        self.screenshot.setAutoFillBackground(False)
        self.screenshot.setFrameShape(QtGui.QFrame.StyledPanel)
        self.screenshot.setFrameShadow(QtGui.QFrame.Sunken)
        self.screenshot.setScaledContents(True)
        self.screenshot.setAlignment(QtCore.Qt.AlignCenter)
        self.screenshot.setWordWrap(True)
        self.screenshot.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.screenshot.setObjectName(_fromUtf8("screenshot"))
        self.layout.addWidget(self.screenshot)

        self.retranslateUi(ScreenshotWidget)
        QtCore.QMetaObject.connectSlotsByName(ScreenshotWidget)

    def retranslateUi(self, ScreenshotWidget):
        ScreenshotWidget.setWindowTitle(_translate("ScreenshotWidget", "3D Pointcloud", None))
        self.screenshot.setText(_translate("ScreenshotWidget", "Screenshot 1", None))

from aui.utilities.ActiveLabel import ActLabel

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ScreenshotWidget = QtGui.QWidget()
    ui = Ui_ScreenshotWidget()
    ui.setupUi(ScreenshotWidget)
    ScreenshotWidget.show()
    sys.exit(app.exec_())

