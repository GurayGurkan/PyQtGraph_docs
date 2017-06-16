# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 16:31:47 2017

@author: g.gurkan
"""
import PyQt4
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import gui_1
import pyqtgraph as pg
import numpy as np

class myApp(QMainWindow,gui_1.Ui_MainWindow):
    def __init__(self,parent=None):
        super(myApp,self).__init__(parent)
        self.setupUi(self)
        print self.figure1
        print self.figure2
        print self.figure3
        self.figure3.setImage(np.random.rand(100,100))



app=QApplication(sys.argv)
form=myApp()
form.show()
app.exec_()