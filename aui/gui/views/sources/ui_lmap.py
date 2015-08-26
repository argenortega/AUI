# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/lmap.ui'
#
# Created: Sat Aug 22 15:47:07 2015
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

class Ui_NewView(object):
    def setupUi(self, NewView):
        NewView.setObjectName(_fromUtf8("NewView"))
        NewView.resize(70, 70)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(NewView.sizePolicy().hasHeightForWidth())
        NewView.setSizePolicy(sizePolicy)
        NewView.setMinimumSize(QtCore.QSize(70, 70))
        NewView.setMaximumSize(QtCore.QSize(70, 70))
        NewView.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        NewView.setMouseTracking(True)
        NewView.setStyleSheet(_fromUtf8("border-image: url(:/maps/local/local1);"))
        self.layout = QtGui.QVBoxLayout(NewView)
        self.layout.setSpacing(0)
        self.layout.setMargin(0)
        self.layout.setObjectName(_fromUtf8("layout"))
        self.map = ActLabel(NewView)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.map.setFont(font)
        self.map.setStyleSheet(_fromUtf8("border-image: url(:/maps/local);\n"
""))
        self.map.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.map.setObjectName(_fromUtf8("map"))
        self.layout.addWidget(self.map)

        self.retranslateUi(NewView)
        QtCore.QMetaObject.connectSlotsByName(NewView)

    def retranslateUi(self, NewView):
        NewView.setWindowTitle(_translate("NewView", "Local Map", None))
        NewView.setAccessibleName(_translate("NewView", "LM", None))
        self.map.setAccessibleName(_translate("NewView", "LM", None))
        self.map.setText(_translate("NewView", "Local Map", None))

from aui.utilities.ActiveLabel import ActLabel

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    NewView = QtGui.QWidget()
    ui = Ui_NewView()
    ui.setupUi(NewView)
    NewView.show()
    sys.exit(app.exec_())

