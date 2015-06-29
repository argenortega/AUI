# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/pointcloud.ui'
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

class Ui_PointcloudWidget(object):
    def setupUi(self, PointcloudWidget):
        PointcloudWidget.setObjectName(_fromUtf8("PointcloudWidget"))
        PointcloudWidget.resize(70, 70)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(PointcloudWidget.sizePolicy().hasHeightForWidth())
        PointcloudWidget.setSizePolicy(sizePolicy)
        PointcloudWidget.setMinimumSize(QtCore.QSize(50, 50))
        PointcloudWidget.setMaximumSize(QtCore.QSize(70, 70))
        PointcloudWidget.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        PointcloudWidget.setMouseTracking(True)
        self.layout = QtGui.QVBoxLayout(PointcloudWidget)
        self.layout.setMargin(0)
        self.layout.setObjectName(_fromUtf8("layout"))
        self.pointcloud = ActLabel(PointcloudWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pointcloud.sizePolicy().hasHeightForWidth())
        self.pointcloud.setSizePolicy(sizePolicy)
        self.pointcloud.setMaximumSize(QtCore.QSize(70, 70))
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
        self.pointcloud.setText(_translate("PointcloudWidget", "3D pointcloud", None))

from ActiveLabel import ActLabel

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PointcloudWidget = QtGui.QWidget()
    ui = Ui_PointcloudWidget()
    ui.setupUi(PointcloudWidget)
    PointcloudWidget.show()
    sys.exit(app.exec_())

