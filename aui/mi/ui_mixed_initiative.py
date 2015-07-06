# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mixed_initiative.ui'
#
# Created: Mon Jun 29 20:31:27 2015
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

class Ui_mixedInitiative(object):
    def setupUi(self, mixedInitiative):
        mixedInitiative.setObjectName(_fromUtf8("mixedInitiative"))
        mixedInitiative.resize(1047, 50)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mixedInitiative.sizePolicy().hasHeightForWidth())
        mixedInitiative.setSizePolicy(sizePolicy)
        mixedInitiative.setMinimumSize(QtCore.QSize(0, 0))
        mixedInitiative.setMaximumSize(QtCore.QSize(16777215, 200))
        mixedInitiative.setBaseSize(QtCore.QSize(0, 100))
        self.mixedInitiativeLayout = QtGui.QHBoxLayout(mixedInitiative)
        self.mixedInitiativeLayout.setSpacing(18)
        self.mixedInitiativeLayout.setMargin(0)
        self.mixedInitiativeLayout.setObjectName(_fromUtf8("mixedInitiativeLayout"))
        self.AUIMsgs = QtGui.QFrame(mixedInitiative)
        self.AUIMsgs.setMinimumSize(QtCore.QSize(0, 50))
        self.AUIMsgs.setFrameShape(QtGui.QFrame.NoFrame)
        self.AUIMsgs.setFrameShadow(QtGui.QFrame.Plain)
        self.AUIMsgs.setObjectName(_fromUtf8("AUIMsgs"))
        self.AUIMsgsLayout = QtGui.QHBoxLayout(self.AUIMsgs)
        self.AUIMsgsLayout.setMargin(0)
        self.AUIMsgsLayout.setObjectName(_fromUtf8("AUIMsgsLayout"))
        self.textBrowserAUIMix = QtGui.QTextBrowser(self.AUIMsgs)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowserAUIMix.sizePolicy().hasHeightForWidth())
        self.textBrowserAUIMix.setSizePolicy(sizePolicy)
        self.textBrowserAUIMix.setMinimumSize(QtCore.QSize(650, 30))
        self.textBrowserAUIMix.setMaximumSize(QtCore.QSize(16777215, 44))
        self.textBrowserAUIMix.setSizeIncrement(QtCore.QSize(5, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textBrowserAUIMix.setFont(font)
        self.textBrowserAUIMix.setMouseTracking(True)
        self.textBrowserAUIMix.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.textBrowserAUIMix.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowserAUIMix.setFrameShadow(QtGui.QFrame.Plain)
        self.textBrowserAUIMix.setLineWidth(1)
        self.textBrowserAUIMix.setMidLineWidth(0)
        self.textBrowserAUIMix.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowserAUIMix.setObjectName(_fromUtf8("textBrowserAUIMix"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.textBrowserAUIMix)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.AUIMsgsLayout.addWidget(self.textBrowserAUIMix)
        self.Accept = QtGui.QPushButton(self.AUIMsgs)
        self.Accept.setMinimumSize(QtCore.QSize(0, 44))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Accept.setFont(font)
        self.Accept.setMouseTracking(True)
        self.Accept.setDefault(True)
        self.Accept.setFlat(False)
        self.Accept.setObjectName(_fromUtf8("Accept"))
        self.AUIMsgsLayout.addWidget(self.Accept)
        self.Reject = QtGui.QPushButton(self.AUIMsgs)
        self.Reject.setMinimumSize(QtCore.QSize(0, 44))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Reject.setFont(font)
        self.Reject.setObjectName(_fromUtf8("Reject"))
        self.AUIMsgsLayout.addWidget(self.Reject)
        self.mixedInitiativeLayout.addWidget(self.AUIMsgs)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.mixedInitiativeLayout.addItem(spacerItem)
        self.AUIStatus = QtGui.QWidget(mixedInitiative)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AUIStatus.sizePolicy().hasHeightForWidth())
        self.AUIStatus.setSizePolicy(sizePolicy)
        self.AUIStatus.setMaximumSize(QtCore.QSize(16777215, 44))
        self.AUIStatus.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.AUIStatus.setObjectName(_fromUtf8("AUIStatus"))
        self.AUIStatusLayout = QtGui.QHBoxLayout(self.AUIStatus)
        self.AUIStatusLayout.setMargin(6)
        self.AUIStatusLayout.setObjectName(_fromUtf8("AUIStatusLayout"))
        self.AUIStatusLabel = QtGui.QLabel(self.AUIStatus)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AUIStatusLabel.sizePolicy().hasHeightForWidth())
        self.AUIStatusLabel.setSizePolicy(sizePolicy)
        self.AUIStatusLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.AUIStatusLabel.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AUIStatusLabel.setFont(font)
        self.AUIStatusLabel.setMouseTracking(True)
        self.AUIStatusLabel.setScaledContents(False)
        self.AUIStatusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AUIStatusLabel.setWordWrap(False)
        self.AUIStatusLabel.setObjectName(_fromUtf8("AUIStatusLabel"))
        self.AUIStatusLayout.addWidget(self.AUIStatusLabel)
        self.AUItoggleButton = QtGui.QPushButton(self.AUIStatus)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AUItoggleButton.sizePolicy().hasHeightForWidth())
        self.AUItoggleButton.setSizePolicy(sizePolicy)
        self.AUItoggleButton.setMinimumSize(QtCore.QSize(44, 44))
        self.AUItoggleButton.setMaximumSize(QtCore.QSize(16777215, 44))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AUItoggleButton.setFont(font)
        self.AUItoggleButton.setMouseTracking(True)
        self.AUItoggleButton.setCheckable(True)
        self.AUItoggleButton.setChecked(False)
        self.AUItoggleButton.setObjectName(_fromUtf8("AUItoggleButton"))
        self.AUIStatusLayout.addWidget(self.AUItoggleButton)
        self.mixedInitiativeLayout.addWidget(self.AUIStatus)

        self.retranslateUi(mixedInitiative)
        QtCore.QMetaObject.connectSlotsByName(mixedInitiative)

    def retranslateUi(self, mixedInitiative):
        mixedInitiative.setWindowTitle(_translate("mixedInitiative", "Form", None))
        self.textBrowserAUIMix.setHtml(_translate("mixedInitiative", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.Helvetica Neue DeskInterface\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[00:00]: Adaptive capabilities turned on.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#0a5dff;\">[02:31]: Display recommended views for Navigation?</span></p></body></html>", None))
        self.Accept.setText(_translate("mixedInitiative", "Accept", None))
        self.Reject.setText(_translate("mixedInitiative", "Reject", None))
        self.AUIStatusLabel.setText(_translate("mixedInitiative", "AUI Status", None))
        self.AUItoggleButton.setText(_translate("mixedInitiative", "Off", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mixedInitiative = QtGui.QWidget()
    ui = Ui_mixedInitiative()
    ui.setupUi(mixedInitiative)
    mixedInitiative.show()
    sys.exit(app.exec_())

