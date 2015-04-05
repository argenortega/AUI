# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 03:33:10 2014

@author: Argen
@version: 2.0


Timer function is based on the stopwatch found here: 
http://thecodeinn.blogspot.de/2013/08/pyqt-stopwatch-and-timer.html
"""


from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QDockWidget
import sys

import Utilities
import Probabilities
import ParametersUI

s = 0
m = 0
h = 0


class AUIParameters(QDockWidget, ParametersUI.Ui_AUIParameters):
    '''
    Parameters related to the GUI's adaptivity simulation. 
    '''
    def __init__(self,parent):
        QtGui.QWidget.__init__(self,parent)
        self.setupUi(self)
        self.initUI()
        
    def initUI(self):
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.Time)
        time = "%d:%02d:%02d"%(h,m,s) 
        self.episodeTimer.setDigitCount(len(time))
        self.episodeTimer.display(time)

        self.startEpisodeButton.clicked.connect(self.Start)
        self.stopEpisodeButton.clicked.connect(lambda: self.timer.stop())
        self.resetEpisodeButton.clicked.connect(self.Reset)

        self.tab2 = Utilities.Utilities(self)

        self.tab3 = Probabilities.Probabilities(self)

        self.contents.addTab(self.tab2, "Utilities")
        self.contents.addTab(self.tab3, "Probabilities")
        self.setWidget(self.contents)


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
    main = AUIParameters(None)
    
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()