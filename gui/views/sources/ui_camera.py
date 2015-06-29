# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/camera.ui'
#
# Created: Mon Jun 29 13:40:06 2015
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

class Ui_Camera(object):
    def setupUi(self, Camera):
        Camera.setObjectName(_fromUtf8("Camera"))
        Camera.resize(300, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(Camera.sizePolicy().hasHeightForWidth())
        Camera.setSizePolicy(sizePolicy)
        Camera.setMinimumSize(QtCore.QSize(0, 0))
        Camera.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Camera.setSizeIncrement(QtCore.QSize(3, 3))
        Camera.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        Camera.setMouseTracking(True)
        self.layout = QtGui.QVBoxLayout(Camera)
        self.layout.setMargin(0)
        self.layout.setObjectName(_fromUtf8("layout"))
        self.cam = ActLabel(Camera)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cam.sizePolicy().hasHeightForWidth())
        self.cam.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.cam.setFont(font)
        self.cam.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.cam.setMouseTracking(True)
        self.cam.setFrameShape(QtGui.QFrame.StyledPanel)
        self.cam.setFrameShadow(QtGui.QFrame.Sunken)
        self.cam.setAlignment(QtCore.Qt.AlignCenter)
        self.cam.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.cam.setObjectName(_fromUtf8("cam"))
        self.layout.addWidget(self.cam)

        self.retranslateUi(Camera)
        QtCore.QMetaObject.connectSlotsByName(Camera)

    def retranslateUi(self, Camera):
        Camera.setWindowTitle(_translate("Camera", "Camera", None))
        self.cam.setText(_translate("Camera", "Camera", None))

from ActiveLabel import ActLabel

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Camera = QtGui.QWidget()
    ui = Ui_Camera()
    ui.setupUi(Camera)
    Camera.show()
    sys.exit(app.exec_())

