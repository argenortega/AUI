# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 03:33:10 2014

@author: Argen
@version: 2.0


Timer function is based on the stopwatch found here: 
http://thecodeinn.blogspot.de/2013/08/pyqt-stopwatch-and-timer.html
"""


from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QDockWidget, QSizePolicy, QLabel, QVBoxLayout, QFrame,
                         QTabWidget)
import sys

import Utilities
import Probabilities

s = 0
m = 0
h = 0


class AUIParameters(QDockWidget):
    '''
    Parameters related to the GUI's adaptivity simulation. 
    '''
    def __init__(self,parent):
        QtGui.QWidget.__init__(self,parent)
        self.initUI()
        
    def initUI(self):        
        self.setObjectName("AUIParameters")
        self.setWindowTitle("AUI Parameters")
        
        self.contents = QTabWidget()
        self.contents.setTabPosition(QTabWidget.South)
        
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName("Tab 1")
        
        self.tab2 = Utilities.Utilities(self)
        #self.tab2.setObjectName("Tab 2")
        
        self.tab3 = Probabilities.Probabilities(self)
        #self.tab3.setObjectName("Tab 3")
        
        self.tab1Layout = QVBoxLayout(self.tab1)
        self.tab1Layout.setObjectName("tab1Layout")
        self.tab1Layout.setSpacing(0)
        self.tab1Layout.setMargin(1)
        self.tab1.setLayout(self.tab1Layout)
        
        self.episodes = QtGui.QGroupBox("Episodes",self.tab1)
        self.episodes.setObjectName("episodes")
        self.episodesLayout = QtGui.QGridLayout()
        self.episodesLayout.setObjectName("episodesLayout")
        self.episodesLayout.setMargin(1)
        #self.episodesLayout.setSpacing(0)
        self.episodes.setLayout(self.episodesLayout)
        #self.episodesLayout.addStretch()
        
        self.episodeTimer = QtGui.QLCDNumber(self.episodes)
        self.episodeTimer.setMinimumSize(QtCore.QSize(80, 30))
        #self.episodeTimer.setMaximumSize(QtCore.QSize(16777215, 60))
        self.episodeTimer.setFrameShape(QtGui.QFrame.StyledPanel)
        self.episodeTimer.setFrameShadow(QtGui.QFrame.Plain)
        self.episodeTimer.setObjectName("episodeTimer")
        self.episodeTimer.setStyleSheet('color: black')
        self.episodesLayout.addWidget(self.episodeTimer,2,0,1,3)
        #self.episodesLayout.setAlignment(QtCore.Qt.AlignVCenter)
        
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.Time)
        time = "%d:%02d:%02d"%(h,m,s) 
        self.episodeTimer.setDigitCount(len(time))
        self.episodeTimer.display(time)
        
        self.startEpisodeButton = QtGui.QPushButton("Start", self.episodes)
        self.startEpisodeButton.setMinimumSize(QtCore.QSize(60, 32))
        self.startEpisodeButton.setObjectName("startEpisodeButton")
        #self.startEpisodeButton.setCheckable(True)
        self.episodesLayout.addWidget(self.startEpisodeButton,1,0)
        
        self.stopEpisodeButton = QtGui.QPushButton("Stop", self.episodes)
        self.stopEpisodeButton.setMinimumSize(QtCore.QSize(60, 32))
        self.stopEpisodeButton.setObjectName("stopEpisodeButton")
        #self.stopEpisodeButton.setCheckable(True)
        self.episodesLayout.addWidget(self.stopEpisodeButton,1,1)
        
        self.resetEpisodeButton = QtGui.QPushButton("New", self.episodes)
        self.resetEpisodeButton.setMinimumSize(QtCore.QSize(60, 32))
        self.resetEpisodeButton.setObjectName("resetEpisodeButton")
        self.episodesLayout.addWidget(self.resetEpisodeButton,1,2)
        
        self.startEpisodeButton.clicked.connect(self.Start)
        self.stopEpisodeButton.clicked.connect(lambda: self.timer.stop())
        self.resetEpisodeButton.clicked.connect(self.Reset)
        
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(False)
        self.episodes.setSizePolicy(sizePolicy)        
        
        self.tab1Layout.addWidget(self.episodes)
        
        self.userStatus = QtGui.QGroupBox("User status", self.tab1)
        self.userStatus.setObjectName("userStatus")
        
        self.userStatusLayout = QtGui.QVBoxLayout(self.userStatus)
        self.userStatusLayout.setObjectName("userStatusLayout")
        self.userStatusLayout.setSpacing(0)
        self.userStatusLayout.setMargin(1)
        self.userStatus.setLayout(self.userStatusLayout)
        
        self.stress = QtGui.QGroupBox("Stress level", self.userStatus)
        self.stress.setObjectName("stress")
        self.stress.setFlat(True)
        self.stressLayout = QtGui.QVBoxLayout(self.stress)
        self.stressLayout.setObjectName("stressLayout")
        self.stressLayout.setSpacing(0)
        self.stressLayout.setMargin(1)
        self.stress.setLayout(self.stressLayout)
        
        self.stressLevel = QtGui.QProgressBar(self.stress)
        self.stressLevel.setMouseTracking(True)
        self.stressLevel.setProperty("value", 0)
        self.stressLevel.setMaximum(10)
        self.stressLevel.setObjectName("stressLevel")
        self.stressLevel.setTextVisible(True)
        self.stressLayout.addWidget(self.stressLevel)
        
        self.stressSlider = QtGui.QSlider(self.stress)
        self.stressSlider.setOrientation(QtCore.Qt.Horizontal)
        self.stressSlider.setObjectName("stressSlider")
        self.stressSlider.setMaximum(10)
        self.stressSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.stressSlider.setTickInterval(1)
        self.stressLayout.addWidget(self.stressSlider)
        
        self.userStatusLayout.addWidget(self.stress)
        
        self.cognitiveLoad = QtGui.QGroupBox("Cognitive load", self.userStatus)
        self.cognitiveLoad.setObjectName("Cognitive Load")
        self.cognitiveLoad.setFlat(True)
        self.cognitiveLoadLayout = QtGui.QVBoxLayout(self.cognitiveLoad)
        self.cognitiveLoadLayout.setObjectName("stressLayout")
        self.cognitiveLoadLayout.setSpacing(0)
        self.cognitiveLoadLayout.setMargin(1)
        self.cognitiveLoad.setLayout(self.cognitiveLoadLayout)
        
        self.cognitiveLoadLevel = QtGui.QProgressBar(self.cognitiveLoad)
        self.cognitiveLoadLevel.setMouseTracking(True)
        self.cognitiveLoadLevel.setProperty("value", 0)
        self.cognitiveLoadLevel.setMaximum(10)
        self.cognitiveLoadLevel.setObjectName("cognitiveLoadLevel")
        self.cognitiveLoadLevel.setTextVisible(True)
        self.cognitiveLoadLayout.addWidget(self.cognitiveLoadLevel)
        
        self.cognitiveLoadSlider = QtGui.QSlider(self.cognitiveLoad)
        self.cognitiveLoadSlider.setOrientation(QtCore.Qt.Horizontal)
        self.cognitiveLoadSlider.setObjectName("cognitiveLoadSlider")
        self.cognitiveLoadSlider.setMaximum(10)
        self.cognitiveLoadSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.cognitiveLoadSlider.setTickInterval(1)
        self.cognitiveLoadLayout.addWidget(self.cognitiveLoadSlider)
        
        self.userStatusLayout.addWidget(self.cognitiveLoad)
        
        self.tab1Layout.addWidget(self.userStatus)
        
        self.taskContext = QtGui.QGroupBox("Task context", self.tab1)
        self.taskContext.setObjectName("taskContext")
        self.taskLayout = QtGui.QVBoxLayout(self.taskContext)
        self.taskLayout.setObjectName("taskLayout")
        self.taskLayout.setMargin(1)
        #self.taskLayout.setSpacing(0)
        self.currentContext = QtGui.QComboBox(self.taskContext)
        self.currentContext.setObjectName("currentContext")
        self.currentContext.addItem("<Select task>")
        self.currentContext.addItem("Forward Navigation")
        self.currentContext.addItem("Backward Navigation")
        self.currentContext.addItem("Camera inspection")
        self.currentContext.addItem("Map review")
        self.currentContext.addItem("New Screenshot")        
        self.taskLayout.addWidget(self.currentContext)
        
        
        self.currentWidget = QtGui.QLabel("<No Widget>",self.taskContext)
        self.currentWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.currentWidget.setFrameShadow(QtGui.QFrame.Raised)
        self.currentWidget.setObjectName("currentWidget")
        self.taskLayout.addWidget(self.currentWidget)
        self.tab1Layout.addWidget(self.taskContext)
        
        self.robotStatus = QtGui.QGroupBox("Robot status", self.tab1)
        self.robotStatus.setObjectName("robotStatus")
        
        self.AUIStatusLayout = QtGui.QVBoxLayout(self.robotStatus)
        self.AUIStatusLayout.setObjectName("AUIStatusLayout")
        self.AUIStatusLayout.setSpacing(0)
        self.AUIStatusLayout.setMargin(1)
        self.robotStatus.setLayout(self.AUIStatusLayout)
        
        self.AUIwifiLevel = QtGui.QGroupBox("Wifi level", self.robotStatus)
        self.AUIwifiLevel.setObjectName("AUIwifiLevel")
        self.AUIwifiLevelLayout = QtGui.QVBoxLayout(self.AUIwifiLevel)
        self.AUIwifiLevelLayout.setObjectName("AUIwifiLevelLayout")
        self.AUIwifiLevelLayout.setSpacing(0)
        self.AUIwifiLevelLayout.setMargin(1)
        self.AUIwifiLevel.setFlat(True)
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
        self.wifiSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.wifiSlider.setTickInterval(10)
        self.wifiSlider.setOrientation(QtCore.Qt.Horizontal)
        self.wifiSlider.setObjectName("wifiSlider")
        self.AUIwifiLevelLayout.addWidget(self.wifiSlider)
        self.AUIStatusLayout.addWidget(self.AUIwifiLevel)
        
        self.AUIbatteryLevel = QtGui.QGroupBox("Battery level", self.robotStatus)
        self.AUIbatteryLevel.setObjectName("AUIbatteryLevel")
        self.AUIbatteryLayout = QtGui.QVBoxLayout(self.AUIbatteryLevel)
        self.AUIbatteryLayout.setObjectName("AUIbatteryLayout")
        self.AUIbatteryLayout.setSpacing(0)
        self.AUIbatteryLayout.setMargin(1)
        self.AUIbatteryLevel.setFlat(True)
        self.AUIbatteryLevel.setLayout(self.AUIbatteryLayout)
        
        self.AUIbattery = QtGui.QProgressBar(self.AUIbatteryLevel)
        self.AUIbattery.setMouseTracking(True)
        self.AUIbattery.setProperty("value", 100)
        self.AUIbattery.setObjectName("AUIbattery")
        self.AUIbattery.setTextVisible(True)
        self.AUIbatteryLayout.addWidget(self.AUIbattery)
        
        self.batterySlider = QtGui.QSlider(self.AUIbatteryLevel)
        self.batterySlider.setMaximum(100)
        self.batterySlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.batterySlider.setTickInterval(10)
        self.batterySlider.setProperty("value", 100)
        self.batterySlider.setOrientation(QtCore.Qt.Horizontal)
        self.batterySlider.setObjectName("batterySlider")
        self.AUIbatteryLayout.addWidget(self.batterySlider)
        self.AUIStatusLayout.addWidget(self.AUIbatteryLevel)
        
        self.tab1Layout.addWidget(self.robotStatus)
        #self.setWidget(self.tab1)
        
        self.contents.addTab(self.tab1, "Control")
        self.contents.addTab(self.tab2, "Utilities")
        self.contents.addTab(self.tab3, "Probabilities")
        self.setWidget(self.contents)
        
        QtCore.QObject.connect(self.batterySlider, QtCore.SIGNAL("valueChanged(int)"), self.AUIbattery.setValue)
        QtCore.QObject.connect(self.wifiSlider, QtCore.SIGNAL("valueChanged(int)"), self.AUIwifi.setValue)
        QtCore.QObject.connect(self.stressSlider, QtCore.SIGNAL("valueChanged(int)"), self.stressLevel.setValue)
        QtCore.QObject.connect(self.cognitiveLoadSlider, QtCore.SIGNAL("valueChanged(int)"), self.cognitiveLoadLevel.setValue)
        QtCore.QMetaObject.connectSlotsByName(self)        
        

    def Reset(self):
        global s,m,h
 
        self.timer.stop()
 
        s = 0
        m = 0
        h = 0
 
        time = "%d:%02d:%02d"%(h,m,s)
 
        self.episodeTimer.setDigitCount(len(time))
        self.episodeTimer.display(time)
 
    def Start(self):
        global s,m,h
         
        self.timer.start(1000)
     
    def Time(self):
        global s,m,h
 
        if s < 59:
            s += 1
        else:
            if m < 59:
                s = 0
                m += 1
            elif m == 59 and h < 24:
                h += 1
                m = 0
                s = 0
            else:
                self.timer.stop()
 
        time = "%d:%02d:%02d"%(h,m,s)
 
        self.episodeTimer.setDigitCount(len(time))
        self.episodeTimer.display(time)



        
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