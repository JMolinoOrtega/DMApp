# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 12:37:38 2016

@author: Jose Molino Ortega (Debian)
"""
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        #Create of a widget
        widget = QtGui.QWidget()
        self.setCentralWidget(widget)
        
        
        #Define the layouts        
        mainLayout = QtGui.QHBoxLayout(self)
        leftLayout = QtGui.QVBoxLayout(self)
        rigthLayout = QtGui.QVBoxLayout(self)
        buttomLayout = QtGui.QHBoxLayout(self)
        widget.setLayout(mainLayout)
        
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
        
        #Creating menus
        self.createActions()        
        self.createMenus()
        
        #Definition window
        self.setGeometry(100,100,800,350)
        self.setWindowTitle(u"DMApp")
        self.show()
        
        
   
    def createActions(self):
        #File
        self.openAct = QtGui.QAction("&Open treasure", self, shortcut=QtGui.QKeySequence.New, statusTip="Open a existing treasure", triggered=self.newFile)        
        
        #No magic        
        self.objectAct = QtGui.QAction("&Mundane object", self, shortcut=QtGui.QKeySequence.New, statusTip="Generate mundane object", triggered=self.newFile)
        self.gemAct = QtGui.QAction("&Gemstone", self, shortcut=QtGui.QKeySequence.New, statusTip="Generate gemstone", triggered=self.newFile)
        self.artAct = QtGui.QAction("&Art piece", self, shortcut=QtGui.QKeySequence.New, statusTip="Generate art piece", triggered=self.newFile)
        self.weaponAct = QtGui.QAction("&Weapon", self, shortcut=QtGui.QKeySequence.New, statusTip="Generate non magical weapon", triggered=self.newFile)
        self.armorAct = QtGui.QAction("&Armor", self, shortcut=QtGui.QKeySequence.New, statusTip="Generate non magical armor", triggered=self.newFile)
        
        #Magic
        self.potionOrOilAct = QtGui.QAction("&Potion or Oil", self, shortcut=QtGui.QKeySequence.New, statusTip="Generate potion or oil", triggered=self.newFile)
        self.scrollAct = QtGui.QAction("&Scroll", self, shortcut=QtGui.QKeySequence.New, statusTip="Generate scroll", triggered=self.newFile)
        self.wandAct = QtGui.QAction("&Wand", self, shortcut=QtGui.QKeySequence.New, statusTip="Generate wand", triggered=self.newFile)
        self.ringAct = QtGui.QAction("&Ring", self, shortcut=QtGui.QKeySequence.New, statusTip="Generate magic ring", triggered=self.newFile)
        self.rodAct = QtGui.QAction("&Rod", self, shortcut=QtGui.QKeySequence.New, statusTip="Generate magic rod", triggered=self.newFile)
        self.staffAct = QtGui.QAction("&Staff", self, shortcut=QtGui.QKeySequence.New, statusTip="Generate magic staff", triggered=self.newFile)
        self.wonderfulAct = QtGui.QAction("&Wonderful item", self, shortcut=QtGui.QKeySequence.New, statusTip="Generate magic wonderful object", triggered=self.newFile)
        self.magicWeaponAct = QtGui.QAction("&Weapon", self, shortcut=QtGui.QKeySequence.New, statusTip="Generate magic weapon", triggered=self.newFile)   
        self.magicArmorAct = QtGui.QAction("&Armor", self, shortcut=QtGui.QKeySequence.New, statusTip="Generate a magic armor", triggered=self.newFile)
     
        #Tools
        self.preferenceAct = QtGui.QAction("&Preferences", self, shortcut=QtGui.QKeySequence.New, statusTip="Open preferences window", triggered=self.newFile)
             
     
    def createMenus(self):
        #File menu
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.openAct)
        
        #No magic objects menu        
        self.MenuNoMagic = self.menuBar().addMenu("&Object")
        self.MenuNoMagic.addAction(self.objectAct)
        self.MenuNoMagic.addAction(self.gemAct)
        self.MenuNoMagic.addAction(self.artAct)
        self.MenuNoMagic.addAction(self.weaponAct)
        self.MenuNoMagic.addAction(self.armorAct)
        
        #Magic objects menu
        self.MenuMagic = self.menuBar().addMenu("&Magic")
        self.MenuMagic.addAction(self.potionOrOilAct)
        self.MenuMagic.addAction(self.scrollAct)
        self.MenuMagic.addAction(self.wandAct)
        self.MenuMagic.addAction(self.ringAct)
        self.MenuMagic.addAction(self.rodAct)
        self.MenuMagic.addAction(self.staffAct)
        self.MenuMagic.addAction(self.wonderfulAct)
        self.MenuMagic.addAction(self.magicWeaponAct)
        self.MenuMagic.addAction(self.magicArmorAct)
        
        #Tools menu
        self.toolsMenu = self.menuBar().addMenu("&Tools")
        self.toolsMenu.addAction(self.preferenceAct)
        
        
    def newFile(self):
        print ("Se ha pulsado nuevo")
            
   
        
        
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = MainWindow()
    sys.exit(app.exec_())    
