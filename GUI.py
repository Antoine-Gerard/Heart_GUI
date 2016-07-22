#!/usr/bin/python

"""
This class creates the main
window of the (heart_gui)
"""

import sys
from PyQt4 import QtGui

class Gui(QtGui.QMainWindow):

    def __init__(self):
        super(Gui, self).__init__()

        self.initUI()


    def openFile(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '/home/antoine/')
        return fname

    def initUI(self):

        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&exit', self)
        exitAction.triggered.connect(QtGui.qApp.quit)

        openAction = QtGui.QAction(QtGui.QIcon(''), '&open', self)
        openAction.triggered.connect(self.openFile)

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)


        self.setWindowTitle('heart_gui')
        self.showMaximized()




def main():
    app = QtGui.QApplication(sys.argv)
    gui = Gui()
    sys.exit(app.exec_())

if __name__=='__main__':
        main()
