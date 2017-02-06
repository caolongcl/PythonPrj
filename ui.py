# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from appwin import Ui_AppWin

#if __name__ == '__main__':
app = QApplication(sys.argv)
appWindow = QMainWindow()
ui = Ui_AppWin()
ui.setupUi(appWindow)
ui.initial()
appWindow.show()
sys.exit(app.exec_())