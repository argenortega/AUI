# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/map.ui'
#
# Created: Mon Jun 29 20:04:52 2015
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

class Ui_Map(object):
    def setupUi(self, Map):
        Map.setObjectName(_fromUtf8("Map"))
        Map.resize(276, 273)
        Map.setFrameShape(QtGui.QFrame.StyledPanel)
        Map.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout = QtGui.QHBoxLayout(Map)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.frame = FocusedWidget(Map)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setStyleSheet(_fromUtf8("border-image: url(:/maps/resources/maps/0007.png);"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Map)
        QtCore.QMetaObject.connectSlotsByName(Map)

    def retranslateUi(self, Map):
        Map.setWindowTitle(_translate("Map", "Frame", None))
        self.label.setText(_translate("Map", "Global Map", None))

from aui.utilities.focusedframe import FocusedWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Map = QtGui.QFrame()
    ui = Ui_Map()
    ui.setupUi(Map)
    Map.show()
    sys.exit(app.exec_())

