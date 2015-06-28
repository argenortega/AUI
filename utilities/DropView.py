__author__ = 'Argen'

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import (QFrame)

from GUI.Views.Sources import Camera


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
            print 'Current Views'
            minSize = QtCore.QSize(100, 100)
            maxSize = QtCore.QSize(16777215, 16777215)
            self.wid.setMaximumSize(maxSize)
            self.wid.setMinimumSize(minSize)
            self.wid.resize(16777215, 16777215)
        elif self.parent().objectName() == 'viewsGroup':
            print 'Available Views'
            minSize = QtCore.QSize(50, 50)
            maxSize = QtCore.QSize(70, 70)
            self.wid.setMaximumSize(maxSize)
            self.wid.setMinimumSize(minSize)
            self.wid.resize(70, 70)

        self.wid.show()

        print self.objectName()
        print self.children()

class DCurrentView(QFrame):
    viewnames = ['trightLabel','tleftLabel','bleftLabel','brightLabel']
    widgetnames = ['']
    def __init__(self, parent):
        QFrame.__init__(self, parent)
        self.setAcceptDrops(True)  # Aceptar objetos
        self.setStyleSheet("background-color: #E6E6E6;")
    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()
    def dropEvent(self, event):
        pos = event.pos()
        self.wid = event.source()
        avViews = self.wid.parent()
        self.wid.setParent(self)
        self.layout().addWidget(self.wid)
        event.acceptProposedAction()

        children = self.findChildren(Camera.Camera)
        if children != 0:
            print 'Cam!'
            for child in children:
                avViews.layout().addWidget(child)


        children = self.findChildren(QtGui.QLabel)
        for child in children:
            if child.objectName() in self.viewnames:
                child.setVisible(False)


        if self.parent().objectName() == 'currentViews':
            minSize = QtCore.QSize(100, 100)
            maxSize = QtCore.QSize(16777215, 16777215)
            self.wid.setMaximumSize(maxSize)
            self.wid.setMinimumSize(minSize)
            self.wid.resize(16777215, 16777215)

        self.wid.show()
    '''
    def dragLeaveEvent(self, event):
        children = self.findChildren(QtGui.QLabel)
        for child in children:
            if child.objectName() in self.viewnames:
                child.setVisible(True)
                event.source.setVisible(False)
    '''


class DAvailableView(QFrame):
    viewnames = ['trightLabel','tleftLabel','bleftLabel','brightLabel']

    def __init__(self, parent):
        QFrame.__init__(self, parent)
        self.setAcceptDrops(True)  # Aceptar objetos
        self.setStyleSheet("background-color: #E6E6E6;")
    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()
    def dropEvent(self, event):
        pos = event.pos()
        self.wid = event.source()
        prevView = self.wid.parent()

        children = prevView.findChildren(QtGui.QLabel)
        for child in children:
            if child.objectName() in self.viewnames:
                child.setVisible(True)

        self.wid.setParent(self)
        self.layout().addWidget(self.wid)
        event.acceptProposedAction()
        print event.source()

        if self.parent().objectName() == 'viewsGroup':
            minSize = QtCore.QSize(50, 50)
            maxSize = QtCore.QSize(70, 70)
            self.wid.setMaximumSize(maxSize)
            self.wid.setMinimumSize(minSize)
            self.wid.resize(70, 70)

        self.wid.show()

    '''
    def dragLeaveEvent(self, event):
        children = self.findChildren(QtGui.QLabel)
        for child in children:
            if child.objectName() in self.viewnames:
                child.setVisible(True)
                event.source.setVisible(False)
    '''



