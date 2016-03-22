# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 12:37:38 2016

@author: Jose Molino Ortega (Debian)
"""
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui

class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        #Define the layouts        
        mainLayout = QtGui.QHBoxLayout(self)
        leftLayout = QtGui.QVBoxLayout(self)
        rigthLayout = QtGui.QVBoxLayout(self)
        buttomLayout = QtGui.QHBoxLayout(self)
        
        #Join the layouts
        mainLayout.addLayout(leftLayout)
        mainLayout.addSpacing(50)
        mainLayout.addLayout(rigthLayout)
        
        
        #-------------leftLayout----------------------
        #Combobox
        #A Challenge is important for determine the min value treasure
        selectChallenge = QtGui.QComboBox(self)
        for i in range(20):
            selectChallenge.addItem(str(i+1))
       
        #ListWidget
        #Display items of the generated treasure
        listObjects = QtGui.QListWidget(self)
        listObjects.addItem("Espada de plata | 200po")
        listObjects.addItem("Espada de bronce (100po)")
        
        #Joint the widgets in the leftLayout
        leftLayout.addWidget(selectChallenge)
        leftLayout.addWidget(listObjects)
        
        
        #-------------rigthLayout-----------------------
        #Label
        #Display the value of the generated treasure
        labelValueTreasure = QtGui.QLabel("Treasure value: ",self)
        labelValueTreasure.setFont(QtGui.QFont('Arial', 22))
        
        #TextEdit
        #Display more information for item selected in listObjects        
        textTreasure = QtGui.QTextEdit(self)
        
        #Join the widgets in the rigthLayout
        rigthLayout.addWidget(labelValueTreasure)
        rigthLayout.addWidget(textTreasure)
        rigthLayout.addSpacing(20)
        rigthLayout.addLayout(buttomLayout)
        
        
        #--------------buttomLayout-----------------------
        #buttoms
        exportButtom = QtGui.QPushButton("Export treasure")
        generateButtom = QtGui.QPushButton("Generate treasure")
        printButtom = QtGui.QPushButton("Print")        
        
        #Joint the widgets in the buttomLayout
        buttomLayout.addWidget(exportButtom)
        buttomLayout.addWidget(generateButtom)
        buttomLayout.addWidget(printButtom)
        
        
        
        #Definition window
        self.setGeometry(100,100,800,350)
        self.setWindowTitle(u"DMApp")
        self.show()
        
        
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = MainWindow()
    sys.exit(app.exec_())    
