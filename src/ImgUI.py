# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Img.ui'
#
# Created: Mon Apr 13 21:15:33 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_PointcloudWidget(object):
    def setupUi(self, PointcloudWidget):
        PointcloudWidget.setObjectName(_fromUtf8("PointcloudWidget"))
        PointcloudWidget.resize(85, 85)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(PointcloudWidget.sizePolicy().hasHeightForWidth())
        PointcloudWidget.setSizePolicy(sizePolicy)
        PointcloudWidget.setMinimumSize(QtCore.QSize(85, 85))
        PointcloudWidget.setMaximumSize(QtCore.QSize(100, 100))
        PointcloudWidget.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        PointcloudWidget.setMouseTracking(True)
        PointcloudWidget.setStyleSheet(_fromUtf8("background-color: rgb(179, 179, 179);"))
        self.layout = QtGui.QVBoxLayout(PointcloudWidget)
        self.layout.setMargin(0)
        self.layout.setObjectName(_fromUtf8("layout"))
        self.pointcloud = QtGui.QLabel(PointcloudWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pointcloud.sizePolicy().hasHeightForWidth())
        self.pointcloud.setSizePolicy(sizePolicy)
        self.pointcloud.setMinimumSize(QtCore.QSize(85, 85))
        self.pointcloud.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pointcloud.setFont(font)
        self.pointcloud.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pointcloud.setMouseTracking(True)
        self.pointcloud.setFrameShape(QtGui.QFrame.StyledPanel)
        self.pointcloud.setFrameShadow(QtGui.QFrame.Sunken)
        self.pointcloud.setScaledContents(True)
        self.pointcloud.setAlignment(QtCore.Qt.AlignCenter)
        self.pointcloud.setWordWrap(True)
        self.pointcloud.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.pointcloud.setObjectName(_fromUtf8("pointcloud"))
        self.layout.addWidget(self.pointcloud)

        self.retranslateUi(PointcloudWidget)
        QtCore.QMetaObject.connectSlotsByName(PointcloudWidget)

    def retranslateUi(self, PointcloudWidget):
        PointcloudWidget.setWindowTitle(_translate("PointcloudWidget", "3D Pointcloud", None))
        self.pointcloud.setText(_translate("PointcloudWidget", "Screenshot 1", None))
