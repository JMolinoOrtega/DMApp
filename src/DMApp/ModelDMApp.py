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
        
class Alchemist(Object):
    amount = 0
    
    def getAmount(self):
        return self.amount
    
    def setAmount(self, amount):
        self.amount = amount
        
class Weapon(Object):
    typeWeapon = ""
    lDamage = "" #Little damage
    mDamage = "" #Medium damage
    critical = ""
    typeDamage = ""
    greatQuality = False
    
    def getTypeWeapon(self):
        return self.typeWeapon
        
    def getlDamage(self):
        return self.lDamage
        
    def getmDamage(self):
        return self.mDamage
        
    def getCritical(self):
        return self.critical
        
    def getTypeDamage(self):
        return self.typeDamage
    
    def isGreatQuality(self):
        return self.greatQuality
        
    def setTypeWeapon(self, typeWeapon):
        self.typeWeapon = typeWeapon
        
    def setLDamage(self, lDamage):
        self.lDamage = lDamage
        
    def setMDamage(self, mDamage):
        self.mDamage = mDamage
        
    def setCritical(self, critical):
        self.critical = critical
        
    def setTypeDamage(self, typeDamage):
        self.typeDamage = typeDamage
        
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
        nRandom = random.randint(1,100)        
        
        #Select type object depends magic power
        if typeMagic is "minor":
            if nRandom >= 1 and nRandom <= 4:
                #Magic armor
                fname = "minorArmor"
            elif nRandom >= 5 and nRandom <= 9:
                #Magic weapon
                fname = "minorWeapon"
            elif nRandom >= 10 and nRandom <= 44:
                #Potion
                fname = "minorPotion"
            elif nRandom >= 45 and nRandom <= 46:
                #Ring
                fname = "minorRing"
            elif nRandom >= 47 and nRandom <= 81:
                #Scroll
                fname = "minorScroll"
            elif nRandom >= 82 and nRandom <= 91:
                #Wand
                fname = "minorWand"
            elif nRandom >= 92 and nRandom <= 100:
                #Wonderful item
                fname = "minorWonderful"
                
        elif typeMagic is "medium":
            if nRandom >= 1 and nRandom <= 10:
                #Magic armor
                fname = "mediumArmor"
            elif nRandom >= 11 and nRandom <= 20:
                #Magic weapon
                fname = "mediumWeapon"
            elif nRandom >= 21 and nRandom <= 30:
                #Potion
                fname = "mediumPotion"
            elif nRandom >= 31 and nRandom <= 40:
                #Ring
                fname = "mediumRing"
            elif nRandom >= 41 and nRandom <= 50:
                #Rod
                fname = "mediumRod"
            elif nRandom >= 51 and nRandom <= 65:
                #Scroll
                fname = "mediumScroll"
            elif nRandom >= 66 and nRandom <= 68:
                #Staff
                fname = "mediumStaff"
            elif nRandom >= 69 and nRandom <= 83:
                #Wand
                fname = "mediumWand"
            elif nRandom >= 84 and nRandom <= 100:
                #Wonderful item
                fname = "mediumWonderful"
            
        elif typeMagic is "major":
            if nRandom >= 1 and nRandom <= 10:
                #Magic armor
                fname = "majorArmor"
            elif nRandom >= 11 and nRandom <= 20:
                #Magic weapon
                fname = "majorWeapon"
            elif nRandom >= 21 and nRandom <= 25:
                #Potion
                fname = "majorPotion"
            elif nRandom >= 26 and nRandom <= 35:
                #Ring
                fname = "majorRing"
            elif nRandom >= 36 and nRandom <= 45:
                #Rod
                fname = "majorRod"
            elif nRandom >= 46 and nRandom <= 55:
                #Scroll
                fname = "majorScroll"
            elif nRandom >= 56 and nRandom <= 75:
                #Staff
                fname = "majorStaff"
            elif nRandom >= 76 and nRandom <= 80:
                #Wand
                fname = "majorWand"
            elif nRandom >= 81 and nRandom <= 100:
                #Wonderful item
                fname = "majorWonderful"
        return fname
            
            
    def generateObject(self):
        print ("Generating objects")
        #Select a random object type
        nRandom = random.randint(1,100)
        if nRandom >= 1 and nRandom <= 17:
            #Alchemist object
            o = self.generateAlchemist()
            return o
        elif nRandom >= 18 and nRandom <= 50:
            #Armor object
            o = self.generateArmor()
            return o
        elif nRandom >= 51 and nRandom <= 83:
            #Weapon object
            o = self.generateWeapon()
            return o
        elif nRandom >= 84:
            #Mundane object
            fname = "object"
        
        #Generate mundane object            
        listObjects = []
        infile = open("library/" + fname, "r")
        line = infile.readline()
        for line in infile:
            listObjects.append(line)
            
        #Select a random object
        mObject = random.sample(listObjects, 1)
        mObject = o[0].split(':')
        
        #Create return object
        o = Object()
        o.setName(mObject[0])
        o.setValue(mObject[1])
        
        return o
            
        
    def generateAlchemist(self):
        fname = "alchemist" #Library file name
        
        #Generate alchemists
        listAlchemist = []
        infile = open("library/" + fname, "r")
        line = infile.readline()
        for line in infile:
            listAlchemist.append(line)
            
        #Select a random alchemist
        alchemist = random.sample(listAlchemist, 1)
        alchemist = alchemist[0].split(':')
        
        #Number of objects
        nObjects = alchemist[1].split('d')
        num = 0        
        for i in range(nObjects[0]):
            num += random.randint(1, nObjects[1])
        price = alchemist[2]*num
        name = str(num) + " " + alchemist[0]

        #Create return alchemist
        a = Alchemist()
        a.setName(name)
        a.setValue(price)
        a.setAmount(num)            
        
    
    def generateWeapon(self, quality=False):
        print ("Generating weapon")
        #Select a random weapon type
        nRandom = random.randint(1,100)
        if nRandom >= 1 and nRandom <= 70:
            fname = "norareweapons"
        elif nRandom >= 71 and nRandom <= 80:
            fname = "rareweapons"
        else:
            fname = "distanceweapons"
            
        #Generate weapon
        listWeapons = []
        infile = open("library/"+fname, "r")
        line = infile.readline()
        for line in infile:
            listWeapons.append(line)
            
        #Select a random weapon
        weapon = random.sample(listWeapons, 1)
        weapon = weapon[0].split(':')
        
        #Create return weapon
        w = Weapon()
        w.setName(weapon[0])
        w.setTypeWeapon(weapon[1])
        print (w.getName())
        w.setValue(int(weapon[2]))
        w.setLDamage(weapon[3])
        w.setMDamage(weapon[4])
        w.setCritical(weapon[5])
        w.setTypeDamage(weapon[6])
        w.setQuality(quality)
        
        
        #If is great quality the price increases
        if w.isGreatQuality() == True:
            newValue = w.getValue()+300
            w.setValue(int(newValue)) 
        
        return w
            
        
        
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
        s.setValue(int(armor[2]))
        s.setQuality(quality)
        
        
        #If is great quality the price increases
        if s.isGreatQuality() == True:
            s.setValue(s.getValue+150)        
        
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
         
        #If is great quality the price increases
        if s.isGreatQuality() == True:
            s.setValue(s.getValue+150)
        
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
    weapon = t.generateWeapon(True)
    print (weapon.getName())
    print (weapon.getValue())
    print (weapon.getlDamage())
    print (weapon.getmDamage())
    print (weapon.getTypeWeapon())
    print (weapon.getTypeDamage())
    print (weapon.getCritical())