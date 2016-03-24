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
        
        
    #Define actions
    def createActions(self):
        #File
        self.openAct = QtGui.QAction("&Open treasure", self, shortcut="Ctrl+O", statusTip="Open a existing treasure", triggered=self.openFile)        
        
        #No magic        
        self.objectAct = QtGui.QAction("&Mundane object", self, shortcut="Ctrl+M", statusTip="Generate mundane object", triggered=self.objectGen)
        self.gemAct = QtGui.QAction("&Gemstone", self, shortcut="Ctrl+G", statusTip="Generate gemstone", triggered=self.gemGen)
        self.artAct = QtGui.QAction("&Art piece", self, shortcut="Ctrl+A", statusTip="Generate art piece", triggered=self.artGen)
        self.weaponAct = QtGui.QAction("&Weapon", self, shortcut="Ctrl+W", statusTip="Generate non magical weapon", triggered=self.weaponGen)
        self.armorAct = QtGui.QAction("&Armor", self, shortcut="Ctrl+D", statusTip="Generate non magical armor", triggered=self.armorGen)
        self.coinAct = QtGui.QAction("&Coins", self, shortcut="Ctrl+C", statusTip="Generate coins", triggered=self.coinGen)
        
        #Magic
        self.potionOrOilAct = QtGui.QAction("&Potion or Oil", self, shortcut="Ctrl+Shift+P", statusTip="Generate potion or oil", triggered=self.pOOilGen)
        self.scrollAct = QtGui.QAction("&Scroll", self, shortcut="Ctrl+Shift+S", statusTip="Generate scroll", triggered=self.scrollGen)
        self.wandAct = QtGui.QAction("&Wand", self, shortcut="Ctrl+Shift+V", statusTip="Generate wand", triggered=self.wandGen)
        self.ringAct = QtGui.QAction("&Ring", self, shortcut="Ctrl+Shift+R", statusTip="Generate magic ring", triggered=self.ringGen)
        self.rodAct = QtGui.QAction("&Rod", self, shortcut="Ctrl+Shift+B", statusTip="Generate magic rod", triggered=self.rodGen)
        self.staffAct = QtGui.QAction("&Staff", self, shortcut="Ctrl+Shift+F", statusTip="Generate magic staff", triggered=self.staffGen)
        self.wonderfulAct = QtGui.QAction("&Wonderful item", self, shortcut="Ctrl+Shift+M", statusTip="Generate magic wonderful object", triggered=self.wonderGen)
        self.magicWeaponAct = QtGui.QAction("&Weapon", self, shortcut="Ctrl+Shift+W", statusTip="Generate magic weapon", triggered=self.magicWeaponGen)   
        self.magicArmorAct = QtGui.QAction("&Armor", self, shortcut="Ctrl+Shift+D", statusTip="Generate a magic armor", triggered=self.magicArmorGen)
     
        #Tools
        self.preferenceAct = QtGui.QAction("&Preferences", self, shortcut="Ctrl+Alt+Shift+P", statusTip="Open preferences window", triggered=self.preferenceMenu)
             
    #Define menus
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
        self.MenuNoMagic.addAction(self.coinAct)
        
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
        
    #Open a treasure file and load it items
    def openFile(self):
        print ("openFile is pushed")
    
    #Generate a mundane object
    def objectGen(self):
        print ("objectGen is pushed")
        
    #Generate a gemstone
    def gemGen(self):
        print ("gemGen is pushed")
        
    #Generate a art piece
    def artGen(self):
        print ("artGen is pushed")
    
    #Generate a non magical weapon
    def weaponGen(self):
        print ("weaponGen is pushed")
    
    #Generate a non magical armor
    def armorGen(self):
        print ("armorGen is pushed")
        
    #Generate random value for the type of coins
    def coinGen(self):
        print ("coinGen is pushed")
        
    #Generate potions or magic oils
    def pOOilGen(self):
        print ("Potion or Oil is pushed")
        
    #Generate scroll
    def scrollGen(self):
        print ("scrollGen is pushed")
        
    #Generate wand
    def wandGen(self):
        print ("wandGen is pushed")
        
    #Generate ring 
    def ringGen(self):
        print ("ringGen is pushed")        
    
    #Generate rod
    def rodGen(self):
        print ("rodGen is pushed")
    
    #Generate staff
    def staffGen(self):
        print ("staffGen is pushed")
    
    #Generate wonderful item
    def wonderGen(self):
        print ("wonderGen is pushed")
        
    #Generate magic weapon
    def magicWeaponGen(self):
        print ("magicWeaponGen is pushed")
        
    #Generate magic armor
    def magicArmorGen(self):
        print ("magicArmorGen is pushed")
        
    #Display the preference window
    def preferenceMenu(self):
        print ("preferenceMenu is pushed")
            
   
        
        
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = MainWindow()
    sys.exit(app.exec_())    
