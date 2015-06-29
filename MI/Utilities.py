# -*- coding: utf-8 -*-
"""
Created on Sun Jan  4 02:05:08 2015

@author: Argen
"""

import sys
import csv

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QWidget)
from PyQt4.QtCore import QString
import matplotlib.pyplot as plt
import numpy as np

from mi import ui_utilities


class Utilities(QWidget, ui_utilities.Ui_utilities):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.detectmodel = QtGui.QStandardItemModel(self)
        self.inspectmodel = QtGui.QStandardItemModel(self)
        self.mappingmodel = QtGui.QStandardItemModel(self)
        self.navigatemodel = QtGui.QStandardItemModel(self)
        self.reviewmodel = QtGui.QStandardItemModel(self)
        self.exploremodel = QtGui.QStandardItemModel(self)
        
        self.utilityPath ='resources/database_data/utilities/'
        
        self.utilityFile = 'detect-detect.csv'
        self.loadCsv(self.utilityPath + self.utilityFile,self.detectmodel)
        self.setHeaders(self.detectmodel)
        self.detectTable.setModel(self.detectmodel)
        self.detectTable.resizeColumnsToContents()
        self.detectTable.resizeRowsToContents()
        
        self.utilityFile = 'explore-explore.csv'
        self.loadCsv(self.utilityPath + self.utilityFile, self.exploremodel)
        self.setHeaders(self.exploremodel)
        self.exploreTable.setModel(self.exploremodel)
        self.exploreTable.resizeColumnsToContents()
        self.exploreTable.resizeRowsToContents()

        self.utilityFile = 'inspect-inspect.csv'
        self.loadCsv(self.utilityPath + self.utilityFile, self.inspectmodel)
        self.setHeaders(self.inspectmodel)
        self.inspectTable.setModel(self.inspectmodel)
        self.inspectTable.resizeColumnsToContents()
        self.inspectTable.resizeRowsToContents()

        self.utilityFile = 'mapping-mapping.csv'
        self.loadCsv(self.utilityPath + self.utilityFile, self.mappingmodel)
        self.setHeaders(self.mappingmodel)
        self.mappingTable.setModel(self.mappingmodel)
        self.mappingTable.resizeColumnsToContents()
        self.mappingTable.resizeRowsToContents()

        self.utilityFile = 'navigate-navigate.csv'
        self.loadCsv(self.utilityPath + self.utilityFile, self.navigatemodel)
        self.setHeaders(self.navigatemodel)
        self.navigateTable.setModel(self.navigatemodel)
        self.navigateTable.resizeColumnsToContents()
        self.navigateTable.resizeRowsToContents()

        self.utilityFile = 'review-review.csv'        
        self.loadCsv(self.utilityPath + self.utilityFile, self.reviewmodel)
        self.setHeaders(self.reviewmodel)
        self.reviewTable.setModel(self.reviewmodel)
        self.reviewTable.resizeColumnsToContents()
        self.reviewTable.resizeRowsToContents()
        
        self.saveButton.clicked.connect(self.saving)
        self.updateButton.clicked.connect(self.updatePlot)
        self.goalList.activated[str].connect(self.changePlot)
        
    def main(self):
        self.show()
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
                    fields.append(data)
                writer.writerow(fields)
    
    def changePlot(self,text):
        self.goalList.setItemData(0,QtCore.QVariant(0),QtCore.Qt.UserRole-1)
        #self.goalList.setItemData(0,QtCore.QVariant(33),QtCore.Qt.UserRole-1)
        self.plotPath = 'resources/plots/utilities/'
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
            self.utilityPlot.clear()
        else:
            self.utilityPlot.clear()
            self.utilityPlot.setPixmap(QtGui.QPixmap(self.plotPath+plotname))
            
    def saving(self):
        if self.goalList.currentText() == "Detect":
            self.utilityFile = 'detect-detect.csv'
            self.writeCsv(self.utilityPath+self.utilityFile, self.detectmodel)
        elif self.goalList.currentText() == "Map":
            self.utilityFile = 'mapping-mapping.csv'        
            self.writeCsv(self.utilityPath+self.utilityFile, self.mappingmodel)
        elif self.goalList.currentText() == "Navigate":
            self.utilityFile = 'navigate-navigate.csv'        
            self.writeCsv(self.utilityPath+self.utilityFile, self.navigatemodel)
        elif self.goalList.currentText() == "Review status":
            self.utilityFile = 'review-review.csv'        
            self.writeCsv(self.utilityPath+self.utilityFile, self.reviewmodel)
        elif self.goalList.currentText() == "Inspect current site":
            self.utilityFile = 'inspect-inspect.csv'        
            self.writeCsv(self.utilityPath+self.utilityFile, self.inspectmodel)
        elif self.goalList.currentText() == "Explore":
            self.utilityFile = 'explore-explore.csv'
            self.writeCsv(self.utilityPath+self.utilityFile, self.exploremodel)
        
        
        
    def updatePlot(self):
        self.plotPath = 'resources/plots/utilities/'
        fig = plt.figure()

        if self.goalList.currentText() == "Detect":
            filename = 'detect-detect.csv'
            plotname = 'detect.png'
        elif self.goalList.currentText() == "Map":
            filename = 'mapping-mapping.csv'        
            plotname = 'mapping.png'        
        elif self.goalList.currentText() == "Navigate":
            filename = 'navigate-navigate.csv'        
            plotname = 'navigate.png'        
        elif self.goalList.currentText() == "Review status":
            filename = 'review-review.csv'        
            plotname = 'review.png'        
        elif self.goalList.currentText() == "Inspect current site":
            filename = 'inspect-inspect.csv'        
            plotname = 'inspect.png'        
        elif self.goalList.currentText() == "Explore":
            filename = 'explore-explore.csv'
            plotname = 'explore.png'
            
        data = np.genfromtxt(self.utilityPath+filename, delimiter = ",")
        labels = ["Fwd","Fwd+turn","Back",
                    "Back+turn","Turn","Charge battery",
                    "Repair wifi", "New ss", "Change ss",
                    "Ch map","Chpointcloud","Ch extra",
                    "Ch C1","Ch C2","Zoom"]
        x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        plt.title(self.goalList.currentText())
        plt.ylabel('Utility')        
        plt.plot(data[:,0],'ro-',label = r'$u(A,G)$')
        plt.plot(data[:,1],'go-',label = r'$u(A,\neg{G})$')
        plt.plot(data[:,2],'co-',label = r'$u(\neg{A},G)$')
        plt.plot(data[:,3],'bo-',label = r'$u(\neg{A},\neg{G})$')
        plt.plot(data[:,4],'ko-',label = r'$u(D,G)$')
        plt.plot(data[:,5],'yo-',label = r'$u(D,\ne{G})$')
        plt.xticks(x,labels, rotation='vertical')
        plt.subplots_adjust(bottom=0.15)
        plt.legend(loc=2)
        plt.ylim(0,3)
        
        fig.savefig(self.plotPath + plotname)  
        self.utilityPlot.clear()
        self.utilityPlot.setPixmap(QtGui.QPixmap(self.plotPath+plotname))

    
    def setHeaders(self,model):
        QString.fromUtf8("Test")
        headersH = ["Move forward","Move front and turn","Move backward",
                    "Move backward and turn","Turn","Charge battery",
                    "Repair wifi", "New screenshot", "Change screenshot",
                    "Change to map","Change to pointcloud","Change to extra view",
                    "Change to C1","Change to C2","Zoom"]
                    
        model.setHeaderData(0,QtCore.Qt.Horizontal,QString.fromUtf8("u(A,G)"))
        model.setHeaderData(1,QtCore.Qt.Horizontal,QString.fromUtf8("u(A,¬G)"))
        model.setHeaderData(2,QtCore.Qt.Horizontal,QString.fromUtf8("u(¬A,G)"))
        model.setHeaderData(3,QtCore.Qt.Horizontal,QString.fromUtf8("u(¬A,¬G)"))
        model.setHeaderData(4,QtCore.Qt.Horizontal,QString.fromUtf8("u(D,G)"))
        model.setHeaderData(5,QtCore.Qt.Horizontal,QString.fromUtf8("u(D,¬G)"))
        
        for i in xrange(15):
            model.setHeaderData(i,QtCore.Qt.Vertical,headersH[i])
        
        
        
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    main = Utilities(None)
    main.main()
    sys.exit(app.exec_())        