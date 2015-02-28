# -*- coding: utf-8 -*-
"""
Created on Sat Dec 27 02:57:21 2014

@author: Argentina Ortega Sáinz
@version: 0.0.2
"""
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QWidget, QFrame, 
                         QHBoxLayout, QVBoxLayout, 
                         QSizePolicy, QLabel)
from PyQt4.uic import loadUi
                         
import Camera
import MixedInitiative
import NewView
import Map
import Pointcloud
import Screenshot
import Wifi
import Battery
import Joystick
import Parameters
import Views


'''
Adaptive User Interface for TRADR project
'''
class AUI(QWidget):    
    def __init__(self,parent=None):
        super(AUI, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(0, 0 , 1280, 800)
        self.setWindowTitle("Adaptive TRADR OCU")
        self.setMouseTracking(True)
        
        '''        
        Layout Definitions for the complete AUI
        '''
        
        #Global Layout for AUI Parameters + TRADR GUI
        self.globalLayout = QHBoxLayout()
        self.setLayout(self.globalLayout)

        self.MainLayout = QVBoxLayout()
        self.MainLayout.setObjectName("MainLayout")
        self.globalLayout.addLayout(self.MainLayout)
        
        self.GUILayout = QHBoxLayout()
        self.GUILayout.setObjectName("GUILayout")
        
        self.ViewsLayout = QVBoxLayout()
        self.ViewsLayout.setObjectName("ViewsLayout")        
                
        
        self.ScreenshotLayout = QVBoxLayout()
        self.ScreenshotLayout.setObjectName("ScreenshotLayout")
        
        self.StatusLayout = QVBoxLayout()
        self.StatusLayout.setObjectName("StatusLayout")
        
        '''
        Widgets
        '''
        #self.horizontalLayout_4 = QtGui.QHBoxLayout(self)
        #self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        
        self.mixedInitiative = MixedInitiative.MixedInitiative(self)
        self.MainLayout.addWidget(self.mixedInitiative)
        
        self.MainLayout.addLayout(self.GUILayout)
        self.views = QtGui.QGroupBox("Available Views",self)

        self.views.setMinimumSize(QtCore.QSize(550, 70))
        self.views.setMaximumSize(QtCore.QSize(5000, 150))
        self.views.setObjectName("views")
        self.viewsGroupLayout = QtGui.QHBoxLayout(self.views)
        self.viewsGroupLayout.setObjectName("viewsGroupLayout")


        #minSize = QtCore.QSize(50, 50)
        #maxSize = QtCore.QSize(70, 70)
        #stretch = 0
        self.pointcloud = Pointcloud.Pointcloud(self)
        self.viewsGroupLayout.addWidget(self.pointcloud)

        #minSize = QtCore.QSize(50, 50)
        #maxSize = QtCore.QSize(70, 70)
        #stretch = 0
        self.map = Map.Map(self)
        self.viewsGroupLayout.addWidget(self.map)

        #minSize = QtCore.QSize(50, 50)
        #maxSize = QtCore.QSize(70, 70)
        #stretch = 0
        self.extra = NewView.NewView(self)
        self.viewsGroupLayout.addWidget(self.extra)
        self.ViewsLayout.addWidget(self.views)
        
        
        self.MainViews = QtGui.QGridLayout()
        self.MainViews.setObjectName("MainViews")

        
        #minSize = QtCore.QSize(100, 100)
        #maxSize = QtCore.QSize(300, 300)
        #stretch = 3
        self.Camera1 = Camera.Camera(self,1)
        self.MainViews.addWidget(self.Camera1,1,2)
        
        
        #minSize = QtCore.QSize(100, 100)
        #maxSize = QtCore.QSize(300, 300)
        #stretch = 1
        self.Camera2 = Camera.Camera(self,2)
        self.MainViews.addWidget(self.Camera2, 0, 0)
        
        self.ViewsLayout.addLayout(self.MainViews)
        self.GUILayout.addLayout(self.ViewsLayout)
        
        #minSize = QtCore.QSize(150, 150)
        #maxSize = QtCore.QSize(200, 200)
        #stretch = 1
        self.CurrentScreenshot = Screenshot.Screenshots(self)
        
        
        self.GUILayout.addWidget(self.CurrentScreenshot)
        
        #minSize = QtCore.QSize(80, 80)
        #maxSize = QtCore.QSize(120, 120)
        
        self.battery = Battery.Battery(self)
        self.wifi = Wifi.Wifi(self)

        self.joystick = Joystick.Joystick(self)
        
        self.StatusLayout.addWidget(self.battery)
        self.StatusLayout.addWidget(self.wifi)
        self.StatusLayout.addStretch()        
        self.StatusLayout.addWidget(self.joystick)
        
        self.GUILayout.addLayout(self.StatusLayout)
        
        self.parameters = Parameters.AUIParameters(self)
        self.globalLayout.addWidget(self.parameters)
        
        
        
        '''
        Connect internal widgets
        '''
        self.mixedInitiative.AUItoggleButton.clicked[bool].connect(self.AUIupdate)
        self.AUIupdate()
        QtCore.QObject.connect(self.parameters.wifiSlider, QtCore.SIGNAL("valueChanged(int)"), self.wifi.value.setNum)        
        QtCore.QObject.connect(self.parameters.batterySlider, QtCore.SIGNAL("valueChanged(int)"), self.battery.value.setNum)
        QtCore.QObject.connect(self.parameters.batterySlider, QtCore.SIGNAL("valueChanged(int)"), self.battery.battery.setValue)
        QtCore.QObject.connect(self.parameters.wifiSlider, QtCore.SIGNAL("valueChanged(int)"), self.wifi.wifi.setValue)

        self.battery.charge.clicked.connect(self.chargeBattery)
        self.wifi.repair.clicked.connect(self.repairWifi)

        QtCore.QMetaObject.connectSlotsByName(self) 

        '''
        State machine.
        machine = QtCore.QStateMachine()
        state1 = QtCore.QState(machine)
        state2 = QtCore.QState(machine)
        state3 = QtCore.QState(machine)
        machine.setInitialState(state1)
        '''
        
        self.show()


    def chargeBattery(self):
        self.parameters.batterySlider.setValue(100)
        self.battery.battery.setValue(100)
        self.battery.value.setText('100')

    def repairWifi(self):
        self.parameters.wifiSlider.setValue(100)
        self.wifi.wifi.setValue(100)
        self.battery.value.setText('100')

    def keyPressEvent(self,e):
        self.joystick.setFocus(True)
    
    def AUIupdate(self):
        enable = self.mixedInitiative.AUItoggleButton.isChecked()
        self.parameters.contents.setEnabled(enable)
    
    def mouseMoveEvent(self,e):
        #print "Mouse moving"
        #if self.mixedInitiative.AUItoggleButton.isChecked():
        #self.Camera1.setFocus(True)
        if self.Camera1.underMouse():
            #print "Camera 1"
            self.parameters.currentWidget.setText("Camera 1")
        elif self.Camera2.underMouse():
            #print "Camera 2"
            self.parameters.currentWidget.setText("Camera 2")
        else:
            self.parameters.currentWidget.setText("")
    
    def mouseReleaseEvent(self,e):
        #print "Mouse entered"
        if self.Camera1.underMouse():
            #print "Camera 1"
            #self.parameters.currentWidget.clear()
            #self.parameters.currentWidget.setText("Camera 1")
            pass
    
def main():
    app = QtGui.QApplication(sys.argv)
    main = AUI()
    
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()
