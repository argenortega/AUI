# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 16:55 2015

@author: Argen
"""

import sys

from PyQt4.QtCore import Qt, QMimeData
from PyQt4.QtGui import (QFrame, QSizePolicy, QApplication, QDrag, QPixmap)

from aui.gui.views.sources import ui_map


class GlobalMap(QFrame, ui_map.Ui_Map):
    def __init__(self,parent,type='global'):
        QFrame.__init__(self,parent)
        self.setupUi(self)
        self.type = type
        self.initUI()

    def initUI(self):
        #if self.type == 'global':
            #self.map.setText('Global Map')
        #else:
            #self.map.setText('Local Map')
        pass

def main():
    app = QApplication(sys.argv)
    main = GlobalMap(None)

    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()