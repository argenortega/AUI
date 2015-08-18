# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/gmap.ui'
#
# Created: Tue Aug 18 11:15:11 2015
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

class Ui_MapWidget(object):
    def setupUi(self, MapWidget):
        MapWidget.setObjectName(_fromUtf8("MapWidget"))
        MapWidget.setWindowModality(QtCore.Qt.NonModal)
        MapWidget.resize(70, 70)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MapWidget.sizePolicy().hasHeightForWidth())
        MapWidget.setSizePolicy(sizePolicy)
        MapWidget.setMinimumSize(QtCore.QSize(50, 50))
        MapWidget.setMaximumSize(QtCore.QSize(70, 70))
        MapWidget.setSizeIncrement(QtCore.QSize(1, 1))
        MapWidget.setBaseSize(QtCore.QSize(50, 50))
        MapWidget.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        MapWidget.setMouseTracking(True)
        MapWidget.setStyleSheet(_fromUtf8("border-image: url(:/maps/global/global2);"))
        self.layout = QtGui.QVBoxLayout(MapWidget)
        self.layout.setMargin(0)
        self.layout.setObjectName(_fromUtf8("layout"))
        self.map = ActLabel(MapWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.map.setFont(font)
        self.map.setStyleSheet(_fromUtf8("border-image: url(:/maps/global);\n"
""))
        self.map.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.map.setObjectName(_fromUtf8("map"))
        self.layout.addWidget(self.map)

        self.retranslateUi(MapWidget)
        QtCore.QMetaObject.connectSlotsByName(MapWidget)

    def retranslateUi(self, MapWidget):
        MapWidget.setWindowTitle(_translate("MapWidget", "Map", None))
        MapWidget.setAccessibleName(_translate("MapWidget", "GM", None))
        self.map.setAccessibleName(_translate("MapWidget", "GM", None))
        self.map.setText(_translate("MapWidget", "Global Map", None))

from aui.utilities.ActiveLabel import ActLabel

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MapWidget = QtGui.QWidget()
    ui = Ui_MapWidget()
    ui.setupUi(MapWidget)
    MapWidget.show()
    sys.exit(app.exec_())

