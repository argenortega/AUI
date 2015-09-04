# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/views.ui'
#
# Created: Fri Sep  4 01:29:58 2015
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

class Ui_viewsWidget(object):
    def setupUi(self, viewsWidget):
        viewsWidget.setObjectName(_fromUtf8("viewsWidget"))
        viewsWidget.resize(500, 490)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(viewsWidget.sizePolicy().hasHeightForWidth())
        viewsWidget.setSizePolicy(sizePolicy)
        viewsWidget.setMinimumSize(QtCore.QSize(500, 0))
        self.verticalLayout = QtGui.QVBoxLayout(viewsWidget)
        self.verticalLayout.setMargin(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.currentViews = QtGui.QWidget(viewsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentViews.sizePolicy().hasHeightForWidth())
        self.currentViews.setSizePolicy(sizePolicy)
        self.currentViews.setObjectName(_fromUtf8("currentViews"))
        self.currentViewsLayout = QtGui.QGridLayout(self.currentViews)
        self.currentViewsLayout.setMargin(0)
        self.currentViewsLayout.setObjectName(_fromUtf8("currentViewsLayout"))
        self.tleft = DCurrentView(self.currentViews)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.tleft.sizePolicy().hasHeightForWidth())
        self.tleft.setSizePolicy(sizePolicy)
        self.tleft.setAcceptDrops(True)
        self.tleft.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tleft.setFrameShadow(QtGui.QFrame.Raised)
        self.tleft.setObjectName(_fromUtf8("tleft"))
        self.tleftLayout = QtGui.QHBoxLayout(self.tleft)
        self.tleftLayout.setMargin(0)
        self.tleftLayout.setObjectName(_fromUtf8("tleftLayout"))
        self.tleftLabel = Marker(self.tleft)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tleftLabel.setFont(font)
        self.tleftLabel.setStyleSheet(_fromUtf8("color: rgb(102, 102, 102);"))
        self.tleftLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tleftLabel.setObjectName(_fromUtf8("tleftLabel"))
        self.tleftLayout.addWidget(self.tleftLabel)
        self.currentViewsLayout.addWidget(self.tleft, 0, 0, 1, 1)
        self.bleft = DCurrentView(self.currentViews)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.bleft.sizePolicy().hasHeightForWidth())
        self.bleft.setSizePolicy(sizePolicy)
        self.bleft.setAcceptDrops(True)
        self.bleft.setFrameShape(QtGui.QFrame.StyledPanel)
        self.bleft.setFrameShadow(QtGui.QFrame.Raised)
        self.bleft.setObjectName(_fromUtf8("bleft"))
        self.bleftLayout = QtGui.QHBoxLayout(self.bleft)
        self.bleftLayout.setMargin(0)
        self.bleftLayout.setObjectName(_fromUtf8("bleftLayout"))
        self.bleftLabel = Marker(self.bleft)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bleftLabel.setFont(font)
        self.bleftLabel.setStyleSheet(_fromUtf8("color: rgb(102, 102, 102);\n"
""))
        self.bleftLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bleftLabel.setObjectName(_fromUtf8("bleftLabel"))
        self.bleftLayout.addWidget(self.bleftLabel)
        self.currentViewsLayout.addWidget(self.bleft, 1, 0, 1, 1)
        self.bright = DCurrentView(self.currentViews)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.bright.sizePolicy().hasHeightForWidth())
        self.bright.setSizePolicy(sizePolicy)
        self.bright.setAcceptDrops(True)
        self.bright.setFrameShape(QtGui.QFrame.StyledPanel)
        self.bright.setFrameShadow(QtGui.QFrame.Raised)
        self.bright.setObjectName(_fromUtf8("bright"))
        self.brightLayout = QtGui.QHBoxLayout(self.bright)
        self.brightLayout.setMargin(0)
        self.brightLayout.setObjectName(_fromUtf8("brightLayout"))
        self.brightLabel = Marker(self.bright)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.brightLabel.setFont(font)
        self.brightLabel.setStyleSheet(_fromUtf8("color: rgb(102, 102, 102);"))
        self.brightLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.brightLabel.setObjectName(_fromUtf8("brightLabel"))
        self.brightLayout.addWidget(self.brightLabel)
        self.currentViewsLayout.addWidget(self.bright, 1, 1, 1, 1)
        self.tright = DCurrentView(self.currentViews)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.tright.sizePolicy().hasHeightForWidth())
        self.tright.setSizePolicy(sizePolicy)
        self.tright.setAcceptDrops(True)
        self.tright.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tright.setFrameShadow(QtGui.QFrame.Raised)
        self.tright.setObjectName(_fromUtf8("tright"))
        self.trightLayout = QtGui.QHBoxLayout(self.tright)
        self.trightLayout.setMargin(0)
        self.trightLayout.setObjectName(_fromUtf8("trightLayout"))
        self.trightLabel = Marker(self.tright)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.trightLabel.setFont(font)
        self.trightLabel.setStyleSheet(_fromUtf8("color: rgb(102, 102, 102);"))
        self.trightLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.trightLabel.setObjectName(_fromUtf8("trightLabel"))
        self.trightLayout.addWidget(self.trightLabel)
        self.currentViewsLayout.addWidget(self.tright, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.currentViews)
        self.buttonViews = QtGui.QHBoxLayout()
        self.buttonViews.setObjectName(_fromUtf8("buttonViews"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.buttonViews.addItem(spacerItem)
        self.four = QtGui.QPushButton(viewsWidget)
        self.four.setMinimumSize(QtCore.QSize(44, 44))
        self.four.setStyleSheet(_fromUtf8("QPushButton{    \n"
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
        self.four.setCheckable(True)
        self.four.setAutoExclusive(True)
        self.four.setObjectName(_fromUtf8("four"))
        self.buttonViews.addWidget(self.four)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.buttonViews.addItem(spacerItem1)
        self.vert = QtGui.QPushButton(viewsWidget)
        self.vert.setMinimumSize(QtCore.QSize(44, 44))
        self.vert.setStyleSheet(_fromUtf8("QPushButton{    \n"
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
        self.vert.setCheckable(True)
        self.vert.setAutoExclusive(True)
        self.vert.setObjectName(_fromUtf8("vert"))
        self.buttonViews.addWidget(self.vert)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.buttonViews.addItem(spacerItem2)
        self.hor = QtGui.QPushButton(viewsWidget)
        self.hor.setMinimumSize(QtCore.QSize(44, 44))
        self.hor.setStyleSheet(_fromUtf8("QPushButton{    \n"
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
        self.hor.setCheckable(True)
        self.hor.setChecked(True)
        self.hor.setAutoExclusive(True)
        self.hor.setObjectName(_fromUtf8("hor"))
        self.buttonViews.addWidget(self.hor)
        spacerItem3 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.buttonViews.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.buttonViews)
        self.viewsGroup = FocusGroupBox(viewsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewsGroup.sizePolicy().hasHeightForWidth())
        self.viewsGroup.setSizePolicy(sizePolicy)
        self.viewsGroup.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.viewsGroup.setFont(font)
        self.viewsGroup.setCheckable(True)
        self.viewsGroup.setObjectName(_fromUtf8("viewsGroup"))
        self.viewsGroupLayout = QtGui.QHBoxLayout(self.viewsGroup)
        self.viewsGroupLayout.setSpacing(0)
        self.viewsGroupLayout.setMargin(0)
        self.viewsGroupLayout.setObjectName(_fromUtf8("viewsGroupLayout"))
        self.availableViews = DAvailableView(self.viewsGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.availableViews.sizePolicy().hasHeightForWidth())
        self.availableViews.setSizePolicy(sizePolicy)
        self.availableViews.setAcceptDrops(True)
        self.availableViews.setFrameShape(QtGui.QFrame.NoFrame)
        self.availableViews.setObjectName(_fromUtf8("availableViews"))
        self.availableViewsLayout = QtGui.QHBoxLayout(self.availableViews)
        self.availableViewsLayout.setMargin(1)
        self.availableViewsLayout.setObjectName(_fromUtf8("availableViewsLayout"))
        self.viewsGroupLayout.addWidget(self.availableViews)
        self.verticalLayout.addWidget(self.viewsGroup)

        self.retranslateUi(viewsWidget)
        QtCore.QObject.connect(self.viewsGroup, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.availableViews.setVisible)
        QtCore.QMetaObject.connectSlotsByName(viewsWidget)

    def retranslateUi(self, viewsWidget):
        viewsWidget.setWindowTitle(_translate("viewsWidget", "Form", None))
        self.tleft.setAccessibleName(_translate("viewsWidget", "MV", None))
        self.tleftLabel.setText(_translate("viewsWidget", "Drag any view here", None))
        self.bleft.setAccessibleName(_translate("viewsWidget", "MV", None))
        self.bleftLabel.setText(_translate("viewsWidget", "Drag any view here", None))
        self.bright.setAccessibleName(_translate("viewsWidget", "MV", None))
        self.brightLabel.setText(_translate("viewsWidget", "Drag any view here", None))
        self.tright.setAccessibleName(_translate("viewsWidget", "MV", None))
        self.trightLabel.setText(_translate("viewsWidget", "Drag any view here", None))
        self.four.setText(_translate("viewsWidget", "┼", None))
        self.vert.setText(_translate("viewsWidget", "│", None))
        self.hor.setText(_translate("viewsWidget", "─", None))
        self.viewsGroup.setAccessibleName(_translate("viewsWidget", "AV", None))
        self.viewsGroup.setTitle(_translate("viewsWidget", "Available Views", None))
        self.availableViews.setAccessibleName(_translate("viewsWidget", "AV", None))

from aui.mi.visual import FocusGroupBox
from aui.utilities.DropView import DCurrentView, Marker, DAvailableView

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    viewsWidget = QtGui.QWidget()
    ui = Ui_viewsWidget()
    ui.setupUi(viewsWidget)
    viewsWidget.show()
    sys.exit(app.exec_())

