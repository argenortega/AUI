# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ExtraView.ui'
#
# Created: Mon Apr 13 20:12:44 2015
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

class Ui_NewView(object):
    def setupUi(self, NewView):
        NewView.setObjectName(_fromUtf8("NewView"))
        NewView.resize(70, 70)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(NewView.sizePolicy().hasHeightForWidth())
        NewView.setSizePolicy(sizePolicy)
        NewView.setMinimumSize(QtCore.QSize(50, 50))
        NewView.setMaximumSize(QtCore.QSize(70, 70))
        NewView.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        NewView.setMouseTracking(True)
        self.layout = QtGui.QVBoxLayout(NewView)
        self.layout.setMargin(0)
        self.layout.setObjectName(_fromUtf8("layout"))
        self.view = QtGui.QLabel(NewView)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view.sizePolicy().hasHeightForWidth())
        self.view.setSizePolicy(sizePolicy)
        self.view.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.view.setFont(font)
        self.view.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.view.setMouseTracking(True)
        self.view.setFrameShape(QtGui.QFrame.StyledPanel)
        self.view.setFrameShadow(QtGui.QFrame.Sunken)
        self.view.setScaledContents(True)
        self.view.setAlignment(QtCore.Qt.AlignCenter)
        self.view.setWordWrap(True)
        self.view.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.view.setObjectName(_fromUtf8("view"))
        self.layout.addWidget(self.view)

        self.retranslateUi(NewView)
        QtCore.QMetaObject.connectSlotsByName(NewView)

    def retranslateUi(self, NewView):
        NewView.setWindowTitle(_translate("NewView", "3D Pointcloud", None))
        self.view.setText(_translate("NewView", "Additional View", None))

