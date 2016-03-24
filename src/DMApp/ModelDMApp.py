# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 14:38:44 2016

@author: Jose Molino Ortega
"""

import random

class Coin:
    typeCoin = "" #Platinum, gold, silver or copper
    value = 0
    
    def getTypeCoin(self):
        return self.typeCoin
        
    def getValue(self):
        return self.value
        
    def setTypeCoin(self, coin):
        self.typeCoin = coin
        
    def setValue(self, value):
        self.value = value
        
class Object:
    name = ""
    value = 0
    
    def getName(self):
        return self.name
        
    def getValue(self):
        return self.value
        
    def setName(self, name):
        self.name = name
        
    def setValue(self, value):
        self.value = value
        
class Weapon(Object):
    typeWeapon = ""
    damage = ""
    greatQuality = False
    
    def getTypeWeapon(self):
        return self.typeWeapon
        
    def getDamage(self):
        return self.damage
    
    def isGreatQuality(self):
        return self.greatQuality
        
    def setTypeWeapon(self, typeWeapon):
        self.typeWeapon = typeWeapon
        
    def setDamage(self, damage):
        self.damage = damage
        
    def setQuality(self, quality):
        self.greatQuality = quality
        
class Armor(Object):
    typeArmor = ""
    ca = 0
    penalty = 0
    greatQuality = False
    
    def getTypeArmor(self):
        return self.typeArmor
        
    def getCa(self):
        return self.ca
        
    def getPenalty(self):
        return self.penalty
    
    def isGreatQuality(self):
        return self.greatQuality
        
    def setTypeArmor(self, typeArmor):
        self.typeArmor = typeArmor
        
    def setCa(self, ca):
        self.ca = ca
        
    def setPenalty(self, penalty):
        self.penalty = penalty
        
    def setQuality(self, quality):
        self.greatQuality = quality
        
class MagicObject:
    name = ""
    value = 0
    typeMagic = "" #Minor, medium, major
    propertie = ""
    reference = "" #Manual and page
    
    
    def getName(self):
        return self.name
        
    def getValue(self):
        return self.value
        
    def getTypeMagic(self):
        return self.typeMagic
        
    def getPropertie(self):
        return self.propertie
        
    def getReference(self):
        return self.reference
        
    def setName(self, name):
        self.name = name
        
    def setValue(self, value):
        self.value = value
        
    def setTypeMagic(self, typeMagic):
        self.typeMagic = typeMagic
        
    def setPropertie(self, propertie):
        self.propertie = propertie
        
    def setReference(self, reference):
        self.reference = reference

class Treasure:
    value = 0
    challenge = 0
    items = []
    
    def getValue(self):
        return self.value
        
    def getChallenge(self):
        return self.challenge
        
    def getItems(self):
        return self.items
        
    def setValue(self, value):
        self.value = value
        
    def setChallenge(self, challenge):
        self.challenge = challenge
        
    def setItems(self, items):
        self.items = items
        
    def generateTreasure(self, challenge):
        print ("Generating treasure")

    def generateMagicObject(self, fname, typeMagic):
        print ("Generating magic object")
        
    def classObjectMagic(self, typeMagic):
        print ("Selecting class of magic object")
        
    def generateObject(self, fname, numberOfObjects):
        print ("Generating objects")
        
    def generateWeapon(self, fname):
        print ("Generating weapon")
        
    def generateArmor(self, fname):
        print ("Generating armor")
        
    def generateCoins(self, fname, challenge):
        print ("Generating coins")
        valueCoin = 0        
        infile = open("library/gc"+fname, "r")
        for i in range(challenge):
            line = infile.readline()
        line = line.split(':')
        for i in range(int(line[1])):
            valueCoin = valueCoin + random.randint(1,int(line[2]))
        valueCoin = valueCoin*int(line[3])
        c = Coin()
        c.setTypeCoin(fname)
        c.setValue(valueCoin)
        return c
        
        
    def minimumValue(self, challenge):
        print ("Returning minimum value")
        infile = open("library/mvt", "r")
        for i in range(challenge):
            line = infile.readline()
        line = line.split(':')
        return int((line[1]))
        
    def diferenceValue(self, challenge):
        print ("Calculating diference of actual value with the minimum value")
        rest = self.value - self.minimumValue(challenge)
        if rest < 0:        
            self.setValue(self.value - rest)
        
        
        
if __name__ == "__main__":
    t = Treasure()
    ppt = t.generateCoins("platinum", 20)
    print (ppt.getTypeCoin())
    print (ppt.getValue())
        
        