__author__ = 'Argen'

import sys

from PyQt4 import QtGui
from PyQt4.QtGui import QWidget

from aui.gui.status import ui_statusbar


class StatusBar(QWidget, ui_statusbar.Ui_statusBarWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        # self.batteryBar.setValue.connect(self.update_bar)

    def update_bar(self, value, bar, to_add_number):
        if value > 70:
            self.change_color(bar,'rgb(76, 175, 80)')
        elif value <= 70 and value > 30:
            self.change_color(bar, 'rgb(255, 193, 7)')
        elif value <= 30:
            self.change_color(bar, 'rgb(244, 67, 54)')

    def change_color(self, bar, color):
        template_css = """QProgressBar::chunk { background-color: %s; }"""
        css = template_css % color
        bar.setStyleSheet(css)

    def example(self):
        self.wifiBar.setValue(63)
        self.batteryBar.setValue(49)


def main():
    app = QtGui.QApplication(sys.argv)
    main = StatusBar(None)
    main.example()
    main.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()