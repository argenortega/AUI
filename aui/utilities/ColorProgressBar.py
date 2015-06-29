__author__ = 'Argen'

from PyQt4.QtGui import QProgressBar

DEFAULT_STYLE = """
QProgressBar{
    border: 1px solid black;
    border-radius: 2px;
}

QProgressBar::chunk {
    background-color: rgb(0,128,0);
    width: 1px;
}
"""


class CProgressBar (QProgressBar):
    def __init__(self, parent):
        QProgressBar.__init__(self, parent)
        #self.setStyleSheet('border: 2px solid grey')
        self.setStyleSheet(DEFAULT_STYLE)
        #print 'This stuff has been done'
        self.setMaximumHeight(7)

    def setValue(self, p_int):
        QProgressBar.setValue(self, p_int)
        if p_int > 70:
            self.change_color('rgb(76, 175, 80)')
        elif p_int <= 70 and p_int > 50:
            self.change_color('rgb(255, 193, 7)')
        elif p_int <= 50:
            self.change_color('rgb(244, 67, 54)')



    def change_color(self, color):
        template_css = """
        QProgressBar{
            border: 1px solid gray;
            border-radius: 2px;
            }
        QProgressBar::chunk {
            background: %s;
            width: 1px;
            }
        """
        css = template_css % color
        self.setStyleSheet(css)