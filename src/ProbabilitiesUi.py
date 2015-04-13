# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Probabilities.ui'
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

class Ui_probabilities(object):
    def setupUi(self, probabilities):
        probabilities.setObjectName(_fromUtf8("probabilities"))
        probabilities.resize(278, 484)
        self.utilitiesLayout = QtGui.QVBoxLayout(probabilities)
        self.utilitiesLayout.setObjectName(_fromUtf8("utilitiesLayout"))
        self.probPlot = QtGui.QLabel(probabilities)
        self.probPlot.setMinimumSize(QtCore.QSize(0, 70))
        self.probPlot.setMaximumSize(QtCore.QSize(300, 300))
        self.probPlot.setText(_fromUtf8(""))
        self.probPlot.setScaledContents(True)
        self.probPlot.setObjectName(_fromUtf8("probPlot"))
        self.utilitiesLayout.addWidget(self.probPlot)
        self.goalLabel = QtGui.QLabel(probabilities)
        self.goalLabel.setObjectName(_fromUtf8("goalLabel"))
        self.utilitiesLayout.addWidget(self.goalLabel)
        self.goalList = QtGui.QComboBox(probabilities)
        self.goalList.setObjectName(_fromUtf8("goalList"))
        self.goalList.addItem(_fromUtf8(""))
        self.goalList.addItem(_fromUtf8(""))
        self.goalList.addItem(_fromUtf8(""))
        self.goalList.addItem(_fromUtf8(""))
        self.goalList.addItem(_fromUtf8(""))
        self.goalList.addItem(_fromUtf8(""))
        self.goalList.addItem(_fromUtf8(""))
        self.utilitiesLayout.addWidget(self.goalList)
        self.probTable = QtGui.QTableView(probabilities)
        self.probTable.setObjectName(_fromUtf8("probTable"))
        self.utilitiesLayout.addWidget(self.probTable)
        self.updateLayout = QtGui.QHBoxLayout()
        self.updateLayout.setSpacing(0)
        self.updateLayout.setMargin(1)
        self.updateLayout.setObjectName(_fromUtf8("updateLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.updateLayout.addItem(spacerItem)
        self.updateButton = QtGui.QPushButton(probabilities)
        self.updateButton.setMinimumSize(QtCore.QSize(0, 32))
        self.updateButton.setObjectName(_fromUtf8("updateButton"))
        self.updateLayout.addWidget(self.updateButton)
        self.utilitiesLayout.addLayout(self.updateLayout)
        self.probPlot.setBuddy(self.updateButton)
        self.goalLabel.setBuddy(self.goalList)

        self.retranslateUi(probabilities)
        QtCore.QObject.connect(self.updateButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.probPlot.update)
        QtCore.QMetaObject.connectSlotsByName(probabilities)
        probabilities.setTabOrder(self.goalList, self.updateButton)

    def retranslateUi(self, probabilities):
        probabilities.setWindowTitle(_translate("probabilities", "Form", None))
        self.goalLabel.setText(_translate("probabilities", "Goal:", None))
        self.goalList.setItemText(0, _translate("probabilities", "<Select>", None))
        self.goalList.setItemText(1, _translate("probabilities", "Detect", None))
        self.goalList.setItemText(2, _translate("probabilities", "Map", None))
        self.goalList.setItemText(3, _translate("probabilities", "Navigate", None))
        self.goalList.setItemText(4, _translate("probabilities", "Review status", None))
        self.goalList.setItemText(5, _translate("probabilities", "Inspect current site", None))
        self.goalList.setItemText(6, _translate("probabilities", "Explore", None))
        self.updateButton.setText(_translate("probabilities", "Update", None))

