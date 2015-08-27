from PyQt4.QtCore import pyqtSignal

__author__ = 'Argen'

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import (QFrame, QLabel)

from aui.gui.views.sources import camera


class DView(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self, parent)
        self.setAcceptDrops(True)  # Aceptar objetos
        self.setStyleSheet("background-color: #E6E6E6;")

    def dragEnterEvent(self, event):
        # Ignorar objetos arrastrados sin informacion
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        # Establecer el widget en una nueva posicion
        pos = event.pos()
        self.wid = event.source()
        self.wid.setParent(self)
        self.layout().addWidget(self.wid)
        event.acceptProposedAction()

        if self.parent().objectName() == 'currentViews':
            print 'Current views'
            minSize = QtCore.QSize(100, 100)
            maxSize = QtCore.QSize(16777215, 16777215)
            self.wid.setMaximumSize(maxSize)
            self.wid.setMinimumSize(minSize)
            self.wid.resize(16777215, 16777215)
            self.wid.updateGeometry()
        elif self.parent().objectName() == 'viewsGroup':
            print 'Available views'
            minSize = QtCore.QSize(50, 50)
            maxSize = QtCore.QSize(70, 70)
            self.wid.setMaximumSize(maxSize)
            self.wid.setMinimumSize(minSize)
            self.wid.resize(70, 70)
            self.wid.updateGeometry()

        self.wid.show()

        print self.objectName()
        print self.children()


class DCurrentView(QFrame):
    viewnames = ['trightLabel', 'tleftLabel', 'bleftLabel', 'brightLabel']
    widgetnames = ['']
    content = pyqtSignal(str, str, name='MV')

    def __init__(self, parent):
        QFrame.__init__(self, parent)
        self.setAcceptDrops(True)  # Aceptar objetos
        self.setStyleSheet("background-color: #E6E6E6;")

    def add_widget(self, widget):
        widget.setParent(self)
        self.layout().addWidget(widget)

        children = self.findChildren(Marker)
        for child in children:
            child.setVisible(False)

        minSize = QtCore.QSize(100, 100)
        maxSize = QtCore.QSize(16777215, 16777215)
        widget.setMaximumSize(maxSize)
        widget.setMinimumSize(minSize)
        widget.resize(16777215, 16777215)
        widget.updateGeometry()
        widget.show()

        self.content.emit(str(widget.objectName()), 'MV')

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        widget = event.source()
        event.acceptProposedAction()

        self.add_widget(widget)

    def dragLeaveEvent(self, event):
        marker = self.findChildren(Marker)
        children = self.children()
        if len(children) == 3:
            for mark in marker:
                mark.setVisible(True)


class Marker(QLabel):
    def __init__(self, parent):
        QLabel.__init__(self, parent)


class DAvailableView(QFrame):
    viewnames = ['trightLabel', 'tleftLabel', 'bleftLabel', 'brightLabel']
    av_wid = pyqtSignal(str, str, name='AV')

    def __init__(self, parent):
        QFrame.__init__(self, parent)
        self.setAcceptDrops(True)  # Aceptar objetos
        self.setStyleSheet("background-color: #E6E6E6;")

    def add_widget(self, widget):
        widget.setParent(self)
        self.layout().addWidget(widget)

        children = self.findChildren(Marker)
        for child in children:
            child.setVisible(False)

        minSize = QtCore.QSize(70, 70)
        maxSize = QtCore.QSize(70, 70)
        widget.setMaximumSize(maxSize)
        widget.setMinimumSize(minSize)
        widget.resize(70, 70)
        widget.updateGeometry()
        widget.show()

        self.av_wid.emit(str(widget.objectName()), 'AV')


    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        widget = event.source()
        event.acceptProposedAction()

        self.add_widget(widget)

    def dragLeaveEvent(self, event):
        pass
