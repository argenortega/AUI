# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/map.ui'
#
# Created: Tue Aug 18 11:15:12 2015
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
        Map.resize(207, 190)
        Map.setStyleSheet(_fromUtf8("border-image: url(:/global/global.png);"))
        Map.setFrameShape(QtGui.QFrame.StyledPanel)
        Map.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout = QtGui.QHBoxLayout(Map)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.map = QtGui.QLabel(Map)
        self.map.setAutoFillBackground(False)
        self.map.setAlignment(QtCore.Qt.AlignCenter)
        self.map.setObjectName(_fromUtf8("map"))
        self.horizontalLayout.addWidget(self.map)

        self.retranslateUi(Map)
        QtCore.QMetaObject.connectSlotsByName(Map)

    def retranslateUi(self, Map):
        Map.setWindowTitle(_translate("Map", "Frame", None))
        self.map.setText(_translate("Map", "Global Map", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Map = QtGui.QFrame()
    ui = Ui_Map()
    ui.setupUi(Map)
    Map.show()
    sys.exit(app.exec_())

