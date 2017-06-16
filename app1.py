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
from cv2 import *

class myApp(QMainWindow,gui_1.Ui_MainWindow):
    def __init__(self,parent=None):
        super(myApp,self).__init__(parent)
        self.setupUi(self)
        
        self.figure1.setTitle("Figure 1 Title")
        self.figure1.setRange(xRange=[0,199])
        self.figure1.setRange(yRange=[-1,1])
        self.p1 = self.figure1.plot()
        self.p1.setData(xdata=np.linspace(0,50,100))
        
        print "Figure 1 is a ", self.figure1.objectName()
        print "Figure 1's parent is ",self.figure1.parent().objectName()
        chs = self.figure1.children()
        for c in chs:
            print "Figure 1' children are: ",c.objectName()
        
        print "Figure 2's parent is ",self.figure2.parent().objectName()
        chs = self.figure2.children()
        for c in chs:
            print "Figure 2's children are: ",c.objectName()
        
        print "Figure 3's parent is ",self.figure3.parent().objectName()
        chs = self.figure3.children()
        for c in chs:
            print "Figure 3's children are: ",c.objectName()
     


        
        
  
    
    def updateImage(self):
        t,fr =self.vid_obj.read()
        self.figure3.setImage(fr.T,autoLevels=False)
        
        
        
        



app=QApplication(sys.argv)
form=myApp()
form.show()
app.exec_()