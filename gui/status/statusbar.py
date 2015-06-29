__author__ = 'Argen'

import sys

from PyQt4 import QtGui
from PyQt4.QtGui import QWidget

from gui.status import ui_statusbar


class StatusBar(QWidget, ui_statusbar.Ui_statusBarWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        # self.batteryBar.setValue.connect(self.update_bar)

    def update_bar(self, value, bar, to_add_number):
        if value > 70:
            self.change_color(bar,'green')
        elif value <= 70 and value > 30:
            self.change_color(bar, 'yellow')
        elif value <= 30:
            self.change_color(bar, 'red')

    def change_color(self, bar, color):
        template_css = """QProgressBar::chunk { background-color: %s; }"""
        css = template_css % color
        bar.setStyleSheet(css)


def main():
    app = QtGui.QApplication(sys.argv)
    main = StatusBar(None)
    main.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()