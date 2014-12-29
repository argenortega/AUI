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
                         
import Camera
import MixedInitiative
import NewView
import Map
import Pointcloud
import Screenshot

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
        self.views.setMinimumSize(QtCore.QSize(650, 70))
        self.views.setMaximumSize(QtCore.QSize(5000, 150))
        self.views.setObjectName("views")
        self.viewsGroupLayout = QtGui.QHBoxLayout(self.views)
        self.viewsGroupLayout.setObjectName("viewsGroupLayout")
        
        minSize = QtCore.QSize(80, 80)
        maxSize = QtCore.QSize(100, 100)
        stretch = 0
        self.pointcloud = Pointcloud.Pointcloud(self,minSize,maxSize,stretch)
        self.viewsGroupLayout.addWidget(self.pointcloud)

        minSize = QtCore.QSize(80, 80)
        maxSize = QtCore.QSize(100, 100)
        stretch = 0
        self.map = Map.Map(self,minSize,maxSize,stretch)
        self.viewsGroupLayout.addWidget(self.map)

        minSize = QtCore.QSize(80, 80)
        maxSize = QtCore.QSize(100, 100)
        stretch = 0         
        self.extra = NewView.NewView(self,minSize,maxSize,stretch)        
        self.viewsGroupLayout.addWidget(self.extra)
        self.ViewsLayout.addWidget(self.views)
        
        
        self.MainViews = QtGui.QGridLayout()
        self.MainViews.setObjectName("MainViews")

        
        minSize = QtCore.QSize(100, 100)
        maxSize = QtCore.QSize(300, 300)
        stretch = 3        
        self.Camera1 = Camera.Camera(self,1,minSize,maxSize,stretch)        
        self.MainViews.addWidget(self.Camera1,1,2)
        
        
        minSize = QtCore.QSize(100, 100)
        maxSize = QtCore.QSize(200, 200)
        stretch = 1 
        self.Camera2 = Camera.Camera(self,2,minSize,maxSize,stretch)
        self.MainViews.addWidget(self.Camera2, 0, 0)
        
        self.ViewsLayout.addLayout(self.MainViews)
        self.GUILayout.addLayout(self.ViewsLayout)
        
        minSize = QtCore.QSize(150, 150)
        maxSize = QtCore.QSize(200, 200)
        stretch = 1
        self.CurrentScreenshot = Screenshot.Screenshots(self,minSize,maxSize,stretch)
        
        
        self.GUILayout.addWidget(self.CurrentScreenshot)
        
        '''
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.StatusLayout)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        
        
        
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        
        self.verticalLayout_4.addWidget(self.joystick)
        self.GUILayout.addWidget(self.StatusLayout)

        self.MainLayout.addLayout(self.GUILayout)
        
        self.horizontalLayout_4.addLayout(self.MainLayout)
        self.AUIParameters = QtGui.QDockWidget(self)
        self.AUIParameters.setObjectName("AUIParameters")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.episodes_groupbox = QtGui.QGroupBox(self.dockWidgetContents)
        self.episodes_groupbox.setObjectName("episodes_groupbox")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.episodes_groupbox)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem3 = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.episodeTimer = QtGui.QLCDNumber(self.episodes_groupbox)
        self.episodeTimer.setMinimumSize(QtCore.QSize(60, 0))
        self.episodeTimer.setMaximumSize(QtCore.QSize(16777215, 60))
        self.episodeTimer.setFrameShape(QtGui.QFrame.StyledPanel)
        self.episodeTimer.setFrameShadow(QtGui.QFrame.Plain)
        self.episodeTimer.setObjectName("episodeTimer")
        self.horizontalLayout_7.addWidget(self.episodeTimer)
        self.startEpisodeButton = QtGui.QPushButton(self.episodes_groupbox)
        self.startEpisodeButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.startEpisodeButton.setObjectName("startEpisodeButton")
        self.horizontalLayout_7.addWidget(self.startEpisodeButton)
        self.verticalLayout_10.addWidget(self.episodes_groupbox)
        self.stress_groupbox = QtGui.QGroupBox(self.dockWidgetContents)
        self.stress_groupbox.setObjectName("stress_groupbox")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.stress_groupbox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.stress_level = QtGui.QProgressBar(self.stress_groupbox)
        self.stress_level.setMouseTracking(True)
        self.stress_level.setProperty("value", 0)
        self.stress_level.setObjectName("stress_level")
        self.verticalLayout_6.addWidget(self.stress_level)
        self.stress_slider = QtGui.QSlider(self.stress_groupbox)
        self.stress_slider.setOrientation(QtCore.Qt.Horizontal)
        self.stress_slider.setObjectName("stress_slider")
        self.verticalLayout_6.addWidget(self.stress_slider)
        self.verticalLayout_10.addWidget(self.stress_groupbox)
        self.task_context_groupbox = QtGui.QGroupBox(self.dockWidgetContents)
        self.task_context_groupbox.setObjectName("task_context_groupbox")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.task_context_groupbox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.current_context = QtGui.QComboBox(self.task_context_groupbox)
        self.current_context.setObjectName("current_context")
        self.verticalLayout_5.addWidget(self.current_context)
        self.verticalLayout_10.addWidget(self.task_context_groupbox)
        self.widget_attention = QtGui.QGroupBox(self.dockWidgetContents)
        self.widget_attention.setObjectName("widget_attention")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.widget_attention)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.current_widget = QtGui.QLabel(self.widget_attention)
        self.current_widget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.current_widget.setFrameShadow(QtGui.QFrame.Raised)
        self.current_widget.setObjectName("current_widget")
        self.verticalLayout_7.addWidget(self.current_widget)
        self.verticalLayout_10.addWidget(self.widget_attention)
        self.robot_status = QtGui.QGroupBox(self.dockWidgetContents)
        self.robot_status.setObjectName("robot_status")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.robot_status)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.wifi_groupbox = QtGui.QGroupBox(self.robot_status)
        self.wifi_groupbox.setObjectName("wifi_groupbox")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.wifi_groupbox)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.wifi_level = QtGui.QProgressBar(self.wifi_groupbox)
        self.wifi_level.setMouseTracking(True)
        self.wifi_level.setProperty("value", 100)
        self.wifi_level.setObjectName("wifi_level")
        self.verticalLayout_8.addWidget(self.wifi_level)
        self.wifi_slider = QtGui.QSlider(self.wifi_groupbox)
        self.wifi_slider.setMaximum(100)
        self.wifi_slider.setProperty("value", 100)
        self.wifi_slider.setOrientation(QtCore.Qt.Horizontal)
        self.wifi_slider.setObjectName("wifi_slider")
        self.verticalLayout_8.addWidget(self.wifi_slider)
        self.verticalLayout_2.addWidget(self.wifi_groupbox)
        self.battery_groupbox = QtGui.QGroupBox(self.robot_status)
        self.battery_groupbox.setObjectName("battery_groupbox")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.battery_groupbox)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.battery_level = QtGui.QProgressBar(self.battery_groupbox)
        self.battery_level.setMouseTracking(True)
        self.battery_level.setProperty("value", 100)
        self.battery_level.setObjectName("battery_level")
        self.verticalLayout_9.addWidget(self.battery_level)
        self.battery_slider = QtGui.QSlider(self.battery_groupbox)
        self.battery_slider.setMaximum(100)
        self.battery_slider.setProperty("value", 100)
        self.battery_slider.setOrientation(QtCore.Qt.Horizontal)
        self.battery_slider.setObjectName("battery_slider")
        self.verticalLayout_9.addWidget(self.battery_slider)
        self.verticalLayout_2.addWidget(self.battery_groupbox)
        self.verticalLayout_10.addWidget(self.robot_status)
        self.AUIParameters.setWidget(self.dockWidgetContents)
        self.horizontalLayout_4.addWidget(self.AUIParameters)

        #self.retranslateUi(self)
        QtCore.QObject.connect(self.battery_slider, QtCore.SIGNAL("valueChanged(int)"), self.battery.setValue)
        QtCore.QObject.connect(self.wifi_slider, QtCore.SIGNAL("valueChanged(int)"), self.wifi.setValue)
        QtCore.QObject.connect(self.battery_slider, QtCore.SIGNAL("valueChanged(int)"), self.battery_level.setValue)
        QtCore.QObject.connect(self.wifi_slider, QtCore.SIGNAL("valueChanged(int)"), self.wifi_level.setValue)
        QtCore.QObject.connect(self.stress_slider, QtCore.SIGNAL("valueChanged(int)"), self.stress_level.setValue)
        QtCore.QMetaObject.connectSlotsByName(self)    
        
        '''
        self.show()
        
   
        
def main():
    app = QtGui.QApplication(sys.argv)
    main = AUI()
    
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()
