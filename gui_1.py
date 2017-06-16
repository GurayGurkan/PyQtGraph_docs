# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_1.ui'
#
# Created: Fri Jun 16 18:50:52 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(587, 489)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.figure2 = GraphicsView(self.centralwidget)
        self.figure2.setGeometry(QtCore.QRect(340, 40, 231, 201))
        self.figure2.setObjectName(_fromUtf8("figure2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 20, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.figure1 = PlotWidget(self.centralwidget)
        self.figure1.setGeometry(QtCore.QRect(60, 40, 261, 131))
        self.figure1.setObjectName(_fromUtf8("figure1"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 20, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.figure3 = ImageView(self.centralwidget)
        self.figure3.setGeometry(QtCore.QRect(60, 210, 256, 192))
        self.figure3.setObjectName(_fromUtf8("figure3"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 190, 71, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 587, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "GraphicsView", None))
        self.label_2.setText(_translate("MainWindow", "PlotWidget", None))
        self.label_3.setText(_translate("MainWindow", "ImageView", None))

from pyqtgraph import ImageView, GraphicsView, PlotWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

