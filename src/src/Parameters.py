# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 03:33:10 2014

@author: Argen
@version: 2.0
"""


from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QSizePolicy, QLabel, QVBoxLayout, QFrame)
import sys

class AUIParameters(QtGui.QDockWidget):
    '''
    Parameters related to the GUI's adaptivity simulation. 
    '''
    def __init__(self,parent):
        QtGui.QWidget.__init__(self,parent)
        self.initUI()
        
    def initUI(self):        
        self.setObjectName("AUIParameters")
        self.setWindowTitle("AUI Parameters")
        self.contents = QtGui.QWidget()
        self.contents.setObjectName("contents")
        
        self.contentsLayout = QtGui.QVBoxLayout(self.contents)
        self.contentsLayout.setObjectName("contentsLayout")
        self.contents.setLayout(self.contentsLayout)
        
        self.episodes = QtGui.QGroupBox("Episodes",self.contents)
        self.episodes.setObjectName("episodes")
        self.episodesLayout = QtGui.QHBoxLayout(self.episodes)
        self.episodesLayout.setObjectName("episodesLayout")
        self.episodes.setLayout(self.episodesLayout)
        #self.episodesLayout.addStretch()
        
        self.episodeTimer = QtGui.QLCDNumber(self.episodes)
        self.episodeTimer.setMinimumSize(QtCore.QSize(60, 0))
        self.episodeTimer.setMaximumSize(QtCore.QSize(16777215, 60))
        self.episodeTimer.setFrameShape(QtGui.QFrame.StyledPanel)
        self.episodeTimer.setFrameShadow(QtGui.QFrame.Plain)
        self.episodeTimer.setObjectName("episodeTimer")
        self.episodesLayout.addWidget(self.episodeTimer)
        self.episodesLayout.setAlignment(QtCore.Qt.AlignVCenter)
        
        self.startEpisodeButton = QtGui.QPushButton("Start", self.episodes)
        self.startEpisodeButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.startEpisodeButton.setObjectName("startEpisodeButton")
        self.startEpisodeButton.setCheckable(True)
        self.episodesLayout.addWidget(self.startEpisodeButton)
        
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(False)
        self.episodes.setSizePolicy(sizePolicy)        
        
        self.contentsLayout.addWidget(self.episodes)
        
        self.stress = QtGui.QGroupBox("Stress level", self.contents)
        self.stress.setObjectName("stress")
        self.stressLayout = QtGui.QVBoxLayout(self.stress)
        self.stressLayout.setObjectName("stressLayout")
        self.stress.setLayout(self.stressLayout)
        
        self.stressLevel = QtGui.QProgressBar(self.stress)
        self.stressLevel.setMouseTracking(True)
        self.stressLevel.setProperty("value", 0)
        self.stressLevel.setObjectName("stressLevel")
        self.stressLevel.setTextVisible(True)
        self.stressLayout.addWidget(self.stressLevel)
        
        self.stressSlider = QtGui.QSlider(self.stress)
        self.stressSlider.setOrientation(QtCore.Qt.Horizontal)
        self.stressSlider.setObjectName("stressSlider")
        self.stressLayout.addWidget(self.stressSlider)
        self.contentsLayout.addWidget(self.stress)
        
        self.taskContext = QtGui.QGroupBox("Task context", self.contents)
        self.taskContext.setObjectName("taskContext")
        self.taskLayout = QtGui.QVBoxLayout(self.taskContext)
        self.taskLayout.setObjectName("taskLayout")
        self.currentContext = QtGui.QComboBox(self.taskContext)
        self.currentContext.setObjectName("currentContext")
        self.currentContext.addItem("<Select task>")
        self.currentContext.addItem("Forward Navigation")
        self.currentContext.addItem("Backward Navigation")
        self.currentContext.addItem("Camera inspection")
        self.currentContext.addItem("Map review")
        self.currentContext.addItem("New Screenshot")        
        self.taskLayout.addWidget(self.currentContext)
        
        
        self.currentWidget = QtGui.QLabel(self.taskContext)
        self.currentWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.currentWidget.setFrameShadow(QtGui.QFrame.Raised)
        self.currentWidget.setObjectName("currentWidget")
        self.taskLayout.addWidget(self.currentWidget)
        self.contentsLayout.addWidget(self.taskContext)
        
        self.robotStatus = QtGui.QGroupBox("Robot status", self.contents)
        self.robotStatus.setObjectName("robotStatus")
        
        self.AUIStatusLayout = QtGui.QVBoxLayout(self.robotStatus)
        self.AUIStatusLayout.setObjectName("AUIStatusLayout")
        self.robotStatus.setLayout(self.AUIStatusLayout)
        
        self.AUIwifiLevel = QtGui.QGroupBox("Wifi level", self.robotStatus)
        self.AUIwifiLevel.setObjectName("AUIwifiLevel")
        self.AUIwifiLevelLayout = QtGui.QVBoxLayout(self.AUIwifiLevel)
        self.AUIwifiLevelLayout.setObjectName("AUIwifiLevelLayout")
        self.AUIwifiLevel.setLayout(self.AUIwifiLevelLayout)
        
        self.AUIwifi = QtGui.QProgressBar(self.AUIwifiLevel)
        self.AUIwifi.setMouseTracking(True)
        self.AUIwifi.setProperty("value", 100)
        self.AUIwifi.setObjectName("AUIwifi")
        self.AUIwifi.setTextVisible(True)
        self.AUIwifiLevelLayout.addWidget(self.AUIwifi)
        
        self.wifiSlider = QtGui.QSlider(self.AUIwifiLevel)
        self.wifiSlider.setMaximum(100)
        self.wifiSlider.setProperty("value", 100)
        self.wifiSlider.setOrientation(QtCore.Qt.Horizontal)
        self.wifiSlider.setObjectName("wifiSlider")
        self.AUIwifiLevelLayout.addWidget(self.wifiSlider)
        self.AUIStatusLayout.addWidget(self.AUIwifiLevel)
        
        self.AUIbatteryLevel = QtGui.QGroupBox("Battery level", self.robotStatus)
        self.AUIbatteryLevel.setObjectName("AUIbatteryLevel")
        self.AUIbatteryLayout = QtGui.QVBoxLayout(self.AUIbatteryLevel)
        self.AUIbatteryLayout.setObjectName("AUIbatteryLayout")
        self.AUIbatteryLevel.setLayout(self.AUIbatteryLayout)
        
        self.AUIbattery = QtGui.QProgressBar(self.AUIbatteryLevel)
        self.AUIbattery.setMouseTracking(True)
        self.AUIbattery.setProperty("value", 100)
        self.AUIbattery.setObjectName("AUIbattery")
        self.AUIbattery.setTextVisible(True)
        self.AUIbatteryLayout.addWidget(self.AUIbattery)
        
        self.batterySlider = QtGui.QSlider(self.AUIbatteryLevel)
        self.batterySlider.setMaximum(100)
        self.batterySlider.setProperty("value", 100)
        self.batterySlider.setOrientation(QtCore.Qt.Horizontal)
        self.batterySlider.setObjectName("batterySlider")
        self.AUIbatteryLayout.addWidget(self.batterySlider)
        self.AUIStatusLayout.addWidget(self.AUIbatteryLevel)
        
        self.contentsLayout.addWidget(self.robotStatus)
        self.setWidget(self.contents)
        
        QtCore.QObject.connect(self.batterySlider, QtCore.SIGNAL("valueChanged(int)"), self.AUIbattery.setValue)
        QtCore.QObject.connect(self.wifiSlider, QtCore.SIGNAL("valueChanged(int)"), self.AUIwifi.setValue)
        QtCore.QObject.connect(self.stressSlider, QtCore.SIGNAL("valueChanged(int)"), self.stressLevel.setValue)
        QtCore.QMetaObject.connectSlotsByName(self)        
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    minSize = QtCore.QSize(100, 100)
    maxSize = QtCore.QSize(300, 300)
    stretch = 3
    main = AUIParameters(None)
    
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()