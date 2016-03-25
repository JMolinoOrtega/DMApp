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
    desMax = 0
    arcanFail = 0
    greatQuality = False
    
    def getTypeArmor(self):
        return self.typeArmor
        
    def getCa(self):
        return self.ca
        
    def getPenalty(self):
        return self.penalty
    
    def isGreatQuality(self):
        return self.greatQuality
        
    def getDesMax(self):
        return self.desMax
    
    def getArcanFail(self):
        return self.arcanFail
        
    def setTypeArmor(self, typeArmor):
        self.typeArmor = typeArmor
        
    def setCa(self, ca):
        self.ca = ca
        
    def setPenalty(self, penalty):
        self.penalty = penalty
        
    def setQuality(self, quality):
        self.greatQuality = quality
        
    def setDesMax(self, desMax):
        self.desMax = desMax
        
    def setArcanFail(self, arcanFail):
        self.arcanFail = arcanFail
        
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
        
    def generateArmor(self, quality=False):
        print ("Generating armor")
        listArmors = []
        infile = open("library/armor", "r")
        line = infile.readline()
        for line in infile:
            listArmors.append(line)
        
        #Select a random armor
        armor = random.sample(listArmors, 1)
        armor = armor[0].split(':')
        
        #Create return armor
        s = Armor()
        s.setName(armor[1])
        s.setCa(armor[3])
        s.setTypeArmor(armor[0])
        s.setPenalty(armor[5])
        s.setDesMax(armor[4])
        s.setArcanFail(armor[6])
        s.setValue(armor[2])
        s.setQuality(quality)
        return s
        
    def generateShield(self, quality=False):
        print ("Generating shield")
        listShields = []
        infile = open("library/shield", "r")
        line = infile.readline()
        for line in infile:
            listShields.append(line)
        
        #Select a random shield
        shield = random.sample(listShields, 1)
        shield = shield[0].split(':')
        
        #Create return shield
        s = Armor()
        s.setName(shield[1])
        s.setCa(shield[3])
        s.setTypeArmor(shield[0])
        s.setPenalty(shield[5])
        s.setDesMax(shield[4])
        s.setArcanFail(shield[6])
        s.setValue(shield[2])
        s.setQuality(quality)
        return s
        
    def generateGemOrArt(self, fname):
        print ("Generating gemstones or art pieces")
        valueObject = 0
        
        #Generate random int for select the line that read
        intRandom = random.randint(1,100)
        validation = False
        infile = open("library/"+fname, "r")
        line = infile.readline()
        
        #While no match line, the loop continue. The library must have good structure for read
        while validation==False:
            line = line.split(':')            
            if intRandom >= int(line[0]) and intRandom <= int(line[1]):
                validation = True
            else:
                line = infile.readline()
        for i in range(int(line[2])):
            valueObject = valueObject + random.randint(1, int(line[3]))
        valueObject = valueObject*int(line[4])
        lineString = line[5].split(';')
        name = random.sample(lineString, 1)
        
        #Create return object
        b = Object()
        b.setName(name)
        b.setValue(valueObject)
        return b
    def generateCoins(self, fname, challenge):
        print ("Generating coins")
        valueCoin = 0  
        
        #fname is a type coin that generate
        infile = open("library/gc"+fname, "r")
        for i in range(challenge):
            line = infile.readline()
        line = line.split(':')
        for i in range(int(line[1])):
            valueCoin = valueCoin + random.randint(1,int(line[2]))
        valueCoin = valueCoin*int(line[3])
        
        #Create return coin        
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
    shield = t.generateArmor()
    print (shield.getName())
    print (shield.getValue())
    print (shield.getDesMax())
    print (shield.getPenalty())
    print (shield.getTypeArmor())
    print (shield.getArcanFail())
        