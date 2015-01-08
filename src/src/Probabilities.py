# -*- coding: utf-8 -*-
"""
Created on Mon Jan  5 23:39:53 2015

@author: Argen
"""

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QWidget)
from PyQt4.QtCore import QString
import ProbabilitiesUi 
import csv 
import matplotlib.pyplot as plt
import numpy as np
import decimal

 
class Probabilities(QWidget, ProbabilitiesUi.Ui_probabilities):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.model = QtGui.QStandardItemModel(self)
        
        self.probabilityPath ='../../database_data/probabilities/'
        
        self.probabilityFile = 'probabilities-probabilities.csv'
        self.loadCsv(self.probabilityPath + self.probabilityFile,self.model)
        self.setHeaders(self.model)
        self.probTable.setModel(self.model)
        self.probTable.resizeColumnsToContents()
        self.probTable.resizeRowsToContents()
        
        #Hide columns and rows
        self.hideRowsCols()
        
        
        #self.saveButton.clicked.connect(self.saving)
        self.updateButton.clicked.connect(self.updatePlot)
        self.goalList.activated[str].connect(self.changePlot)
        self.goalList.activated[int].connect(self.setFlags)
        
    def main(self):
        self.show()
        
    def hideRowsCols(self):
        for i in xrange(6):
            self.probTable.hideColumn(i)    
        for i in xrange(28):
            self.probTable.hideRow(i)

    '''
    Load and write methods are based on http://stackoverflow.com/questions/15416663/pyqt-populating-qtablewidget-with-csv-data
    '''    
    def loadCsv(self, fileName, model):
        with open(fileName, "rb") as fileInput:
            for row in csv.reader(fileInput):    
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]
                model.appendRow(items)
                
    def writeCsv(self, fileName, model):
        with open(fileName, "wb") as fileOutput:
            writer = csv.writer(fileOutput)
            for rowNumber in range(model.rowCount()):
                fields = []
                for columnNumber in range(model.columnCount()):
                    data, flag = model.data(model.index(rowNumber, columnNumber),
                                            QtCore.Qt.DisplayRole).toFloat()
                    fields.append(round(decimal.Decimal(data),2))
                writer.writerow(fields)
    
    def changePlot(self,text):
        self.goalList.setItemData(0,QtCore.QVariant(0),QtCore.Qt.UserRole-1)
        self.plotPath = '../../database_data/plots/prob/'
        if text == "<Select>":
            plotname=""
        elif text == "Detect":
            plotname = 'detect.png'
        elif text == "Map":
            plotname = 'mapping.png'        
        elif text == "Navigate":
            plotname = 'navigate.png'        
        elif text == "Review status":
            plotname = 'review.png'        
        elif text == "Inspect current site":
            plotname = 'inspect.png'        
        elif text == "Explore":
            plotname = 'explore.png'
            
        if text == "<Select>":
            self.probPlot.clear()
        else:
            self.probPlot.clear()
            self.probPlot.setPixmap(QtGui.QPixmap(self.plotPath+plotname))
            
    def saving(self):
        self.writeCsv(self.probabilityPath+self.probabilityFile, self.model)
        
        
        
    def updatePlot(self):
        self.saving()
        self.plotPath = '../../database_data/plots/prob/'
        fig = plt.figure()

        if self.goalList.currentText() == "Detect":
            plotname = 'detect.png'
        elif self.goalList.currentText() == "Map":
            plotname = 'mapping.png'        
        elif self.goalList.currentText() == "Navigate":
            plotname = 'navigate.png'        
        elif self.goalList.currentText() == "Review status":
            plotname = 'review.png'        
        elif self.goalList.currentText() == "Inspect current site":
            plotname = 'inspect.png'        
        elif self.goalList.currentText() == "Explore":
            plotname = 'explore.png'
            
        data = np.genfromtxt(self.probabilityPath+self.probabilityFile, delimiter = ",")
        labels = ["On C1", "On C2", "On Map", "On Pointcloud", "On Extraview",
                    "On Main Screenshot", "On Extra Screenshot", "C1 Clicked",
                    "C2 Clicked", "Map Clicked", "Pointcloud Clicked",
                    "Extra Clicked", "On Main  View", "On Add View", 
                    "Main Screenshot Clicked", "Extra Screenshot Clicked",
                    "New Clicked", "Hide Clicked", "On Battery", 
                    "Charge Clicked", "On Wifi", "Repair Clicked",
                    "Up Pressed", "Down Pressed", "Left Pressed",
                    "Right Pressed", "Accept Clicked", "Reject Clicked"]
        x = np.arange(28)
        plt.title(self.goalList.currentText())
        plt.ylabel('Probability')        
        plt.bar(x,data[:,0],label = self.goalList.currentText())
        plt.xticks(x,labels, rotation='vertical')
        plt.subplots_adjust(bottom=0.15)
        plt.legend(loc=2)
        plt.ylim(0,3)
        #plt.bar()
        
        fig.savefig(self.plotPath + plotname)  
        self.probPlot.clear()
        self.probPlot.setPixmap(QtGui.QPixmap(self.plotPath+plotname))

    
    def setHeaders(self,model):
        QString.fromUtf8("Test")
        headersH = ["On C1", "On C2", "On Map", "On Pointcloud", "On Extraview",
                    "On Main Screenshot", "On Extra Screenshot", "C1 Clicked",
                    "C2 Clicked", "Map Clicked", "Pointcloud Clicked",
                    "Extra Clicked", "On Main  View", "On Add View", 
                    "Main Screenshot Clicked", "Extra Screenshot Clicked",
                    "New Clicked", "Hide Clicked", "On Battery", 
                    "Charge Clicked", "On Wifi", "Repair Clicked",
                    "Up Pressed", "Down Pressed", "Left Pressed",
                    "Right Pressed", "Accept Clicked", "Reject Clicked"]
                    
                    
        model.setHeaderData(0,QtCore.Qt.Horizontal,QString.fromUtf8("Detect"))
        model.setHeaderData(1,QtCore.Qt.Horizontal,QString.fromUtf8("Mapping"))
        model.setHeaderData(2,QtCore.Qt.Horizontal,QString.fromUtf8("Navigate"))
        model.setHeaderData(3,QtCore.Qt.Horizontal,QString.fromUtf8("Review status"))
        model.setHeaderData(4,QtCore.Qt.Horizontal,QString.fromUtf8("Inspect"))
        model.setHeaderData(5,QtCore.Qt.Horizontal,QString.fromUtf8("Explore"))
        
        for i in xrange(28):
            model.setHeaderData(i,QtCore.Qt.Vertical,headersH[i])
        
    def setFlags(self,index):
        self.hideRowsCols()

        self.probTable.showColumn(index-1)  
        
        evidence = ["On C1", "On C2", "On Map", "On Pointcloud", "On Extraview",
            "On Main Screenshot", "On Extra Screenshot", "C1 Clicked",
            "C2 Clicked", "Map Clicked", "Pointcloud Clicked",
            "Extra Clicked", "On Main  View", "On Add View", 
            "Main Screenshot Clicked", "Extra Screenshot Clicked",
            "New Clicked", "Hide Clicked", "On Battery", 
            "Charge Clicked", "On Wifi", "Repair Clicked",
            "Up Pressed", "Down Pressed", "Left Pressed",
            "Right Pressed", "Accept Clicked", "Reject Clicked"]
            
        if index == 1:
            #Detect
            influence = ["On C1", "On C2","On Main Screenshot", 
            "On Extra Screenshot", "C1 Clicked","C2 Clicked", 
            "Extra Clicked", "On Main  View", "On Add View"]
        elif index == 2:
            #Map
            influence = ["On Map", "On Pointcloud", "On Extraview",
            "Pointcloud Clicked","On Main  View", "On Add View"]
        elif index == 3:
            #Navigate
            influence = ["On C1", "On C2", "On Map",  "On Main  View", "On Add View", 
            "Up Pressed", "Down Pressed", "Left Pressed", "Right Pressed"]
        elif index == 4:
            #Review
            influence = ["On Battery", "Charge Clicked", 
            "On Wifi", "Repair Clicked"]
        elif index == 5:
            #Inspect
            influence = ["On Main Screenshot", "On Extra Screenshot", 
            "Main Screenshot Clicked", "Extra Screenshot Clicked",
            "New Clicked", "Hide Clicked"]
        elif index == 6:
            #Explore
            influence = ["On Map", "Map Clicked", "On Main  View", 
                         "On Add View"]
        
        for i in influence:
            j = evidence.index(i)
            self.probTable.showRow(j)
         
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    main = Probabilities(None)
    main.main()
    sys.exit(app.exec_())        