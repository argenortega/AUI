# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/aui.ui'
#
# Created: Mon Aug 31 11:35:59 2015
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

class Ui_MainWin(object):
    def setupUi(self, MainWin):
        MainWin.setObjectName(_fromUtf8("MainWin"))
        MainWin.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWin.setFont(font)
        MainWin.setAcceptDrops(True)
        MainWin.setDockNestingEnabled(True)
        MainWin.setUnifiedTitleAndToolBarOnMac(True)
        self.AUIWidget = QtGui.QWidget(MainWin)
        self.AUIWidget.setObjectName(_fromUtf8("AUIWidget"))
        self.globalLayout = QtGui.QHBoxLayout(self.AUIWidget)
        self.globalLayout.setMargin(0)
        self.globalLayout.setObjectName(_fromUtf8("globalLayout"))
        self.label = QtGui.QLabel(self.AUIWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.globalLayout.addWidget(self.label)
        MainWin.setCentralWidget(self.AUIWidget)
        self.menubar = QtGui.QMenuBar(MainWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWin.setMenuBar(self.menubar)
        self.logbar = QtGui.QStatusBar(MainWin)
        self.logbar.setObjectName(_fromUtf8("logbar"))
        MainWin.setStatusBar(self.logbar)
        self.actionHola = QtGui.QAction(MainWin)
        self.actionHola.setObjectName(_fromUtf8("actionHola"))

        self.retranslateUi(MainWin)
        QtCore.QMetaObject.connectSlotsByName(MainWin)

    def retranslateUi(self, MainWin):
        MainWin.setWindowTitle(_translate("MainWin", "Adaptive OCU", None))
        self.label.setText(_translate("MainWin", "TextLabel", None))
        self.actionHola.setText(_translate("MainWin", "Hola", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWin = QtGui.QMainWindow()
    ui = Ui_MainWin()
    ui.setupUi(MainWin)
    MainWin.show()
    sys.exit(app.exec_())

