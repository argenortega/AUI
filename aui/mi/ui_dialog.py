# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/dialog.ui'
#
# Created: Wed Aug 26 18:53:57 2015
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 77)
        Dialog.setStyleSheet(_fromUtf8("QPushButton{    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-color: rgb(193, 193, 193);\n"
"    border-style: solid;\n"
"    padding: 6px;\n"
"    \n"
"}\n"
"QPushButton:pressed {    \n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    background-color: rgb(48, 131, 251);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-color: rgb(164, 205, 255);\n"
"    border-radius: 6px;\n"
"    border-width: 3px;\n"
"    border-style: solid;\n"
"}"))
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

