__author__ = 'Argen'

import sys
from PyQt4 import QtGui

from PyQt4.QtGui import QProgressBar, QPushButton, QGroupBox, QLabel
from PyQt4.QtCore import pyqtSlot, QTimer, pyqtSignal, QObject

DEFAULT_STYLE = """
QProgressBar{
    border: 1px solid black;
    border-radius: 2px;
}

QProgressBar::chunk {
    background-color: rgb(76, 175, 80);
    width: 25px;
}
"""


class CProgressBar(QProgressBar):
    def __init__(self, parent):
        QProgressBar.__init__(self, parent)
        self.setStyleSheet(DEFAULT_STYLE)
        self.setMaximumHeight(7)

    def setValue(self, p_int):
        QProgressBar.setValue(self, p_int)
        if p_int > 70:
            self.change_color('rgb(76, 175, 80)')  # Green
        elif 70 >= p_int > 50:
            self.change_color('rgb(255, 193, 7)')  # Yellow
        elif p_int <= 50:
            self.change_color('rgb(211, 47, 47)')  # Red

    def change_color(self, color):
        template_css = """
        QProgressBar{
            border: 2px solid rgb(193, 193, 193);
            border-radius: 2px;
            text-align: center;
            }
        QProgressBar::chunk {
            background: %s;
            width: 1px;
            }
        """
        css = template_css % color
        self.setStyleSheet(css)


class CButton(QPushButton):
    green = 'rgb(76, 175, 80)'
    yellow = 'rgb(255, 193, 7)'
    red = 'rgb(211, 47, 47)'
    white = 'rgb(255, 255, 255)'
    black = 'rgb(0, 0, 0)'
    template_css = """
        QPushButton{
            border-style: transparent;
            border-width: 1px;
            border-radius: 6px;
            background-color: %s;
            color: %s;
            }
        QPushButton:pressed {
            border-style: transparent;
            border-width: 1px;
            border-radius: 6px;
            background-color: rgb(76, 175, 80);
            color: rgb(255, 255, 255);
            }
        """

    def __init__(self, parent):
        QPushButton.__init__(self, parent)
        self.setStyleSheet(self.template_css % (self.green, self.white))

    @pyqtSlot(int)
    def set_color(self, p_int):
        if p_int > 70:
            self.change_color(self.green, self.white)  # Green
        elif 70 >= p_int > 50:
            self.change_color(self.yellow, self.black)  # Yellow
        elif p_int <= 50:
            self.change_color(self.red, self.white)  # Red

    def change_color(self, color, text):
        css = self.template_css % (color, text)
        self.setStyleSheet(css)


class ColorGroupBox(QGroupBox):
    green = 'rgb(76, 175, 80)'
    yellow = 'rgb(255, 193, 7)'
    red = 'rgb(211, 47, 47)'
    white = 'rgb(255, 255, 255)'
    black = 'rgb(0, 0, 0)'
    template_css = """
        QGroupBox{
            border-style: transparent;
            border-width: 1px;
            border-radius: 6px;
            background-color: %s;
            color: %s;
            }
        """

    def __init__(self, parent):
        QGroupBox.__init__(self, parent)
        self.setStyleSheet(self.template_css % (self.green, self.white))

    @pyqtSlot(int)
    def set_color(self, p_int):
        if p_int > 70:
            self.change_color(self.green, self.white)  # Green
        elif 70 >= p_int > 50:
            self.change_color(self.yellow, self.black)  # Yellow
        elif p_int <= 50:
            self.change_color(self.red, self.white)  # Red

    def change_color(self, color, text):
        css = self.template_css % (color, text)
        self.setStyleSheet(css)


class FocusGroupBox(QGroupBox):
    inside = pyqtSignal(str, str, name='inside')

    def __init__(self, parent):
        QGroupBox.__init__(self, parent)

    def enterEvent(self, QEvent):
        QTimer.singleShot(3000, self.focusing)

    def focusing(self):
        if self.underMouse():
            self.inside.emit('focus', str(self.accessibleName()))

    def leaveEvent(self, QEvent):
        pass


class View(QLabel, QObject):
    inside = pyqtSignal(str, str, name='inside')
    focus = False
    default_style = 'border-color: rgb(154, 154, 154); border-style: solid; border-width: 2px; border-radius: 6px;'

    def __init__(self, parent):
        QLabel.__init__(self, parent)
        self.outside = pyqtSignal(str)
        self.setStyleSheet(self.default_style)

    def enterEvent(self, event):
        self.setStyleSheet(
            'border-color: rgb(164, 205, 255); border-radius: 6px; border-width: 3px; border-style: solid;')
        QTimer.singleShot(5000, self.focusing)

    def leaveEvent(self, event):
        self.setStyleSheet(self.default_style)
        self.focus = False

    def focusing(self):
        if self.underMouse():
            self.inside.emit('focus', str(self.accessibleName()))
            self.setStyleSheet(
                'border-color: rgb(9, 80, 208); border-radius: 6px; border-width: 4px; border-style: solid;')
            self.focus = True

    def attention(self):
        self.setStyleSheet(
            'border-color: rgb(139, 195, 74); border-radius: 6px; border-width: 4px; border-style: solid;')

    def focused(self):
        return self.focus


def main():
    app = QtGui.QApplication(sys.argv)
    bar = CProgressBar(None)
    bar.example()
    bar.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
