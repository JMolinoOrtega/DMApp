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
        
    def calculateValue(self):
        self.value = 0        
        for i in self.items:
            if type(i) is Coin:
                if i.getTypeCoin() is "platinum":
                    self.value += i.getValue()*10
                elif i.getTypeCoin() is "gold":
                    self.value += i.getValue()
                elif i.getTypeCoin() is "silver":
                    self.value += i.getValue()/10
                elif i.getTypeCoin() is "copper":
                    self.value += i.getValue()/100
            else:
                self.value += i.getValue()
        
    def generateTreasure(self, challenge):
        print ("Generating treasure")
        if challenge == 1:
            #Coin
            nRandom = random.randint(1,100)
            if nRandom > 14:            
                if nRandom >= 15 and nRandom <= 29:
                    fname = "copper"                
                    c = self.generateCoins(fname, challenge)
                elif nRandom >= 30 and nRandom <= 52:
                    fname = "silver"
                    c = self.generateCoins(fname, challenge)
                elif nRandom >= 53 and nRandom <= 95:
                    fname = "gold"
                    c = self.generateCoins(fname, challenge)
                elif nRandom >= 96 and nRandom <= 100:
                    fname = "platinum"
                    c = self.generateCoins(fname, challenge)
                self.items.append(c)
                        
                
            #Gems and art pieces
            nRandom = random.randint(1,100)
            if nRandom > 90:            
                if nRandom >= 91 and nRandom <= 95:
                    fname = "gemstone"
                    goa = self.generateGemOrArt(fname)
                elif nRandom >= 96 and nRandom <= 100:
                    fname = "artpiece"
                    goa = self.generateGemOrArt(fname)
                self.items.append(goa)
                
            #Mundane and magic objects
            nRandom = random.randint(1,100)
            if nRandom > 71:
                if nRandom >= 72 and nRandom <= 95:
                    o = self.generateObject()
                    self.items.append(o)
                elif nRandom >= 96 and nRandom <= 100:
                    o = self.classObjectMagic("minor")
                    self.items.append(o)
                    
        elif challenge == 2:
            #Coin
            nRandom = random.randint(1,100)
            if nRandom > 13:            
                if nRandom >= 14 and nRandom <= 23:
                    fname = "copper"                
                    c = self.generateCoins(fname, challenge)
                elif nRandom >= 24 and nRandom <= 43:
                    fname = "silver"
                    c = self.generateCoins(fname, challenge)
                elif nRandom >= 44 and nRandom <= 95:
                    fname = "gold"
                    c = self.generateCoins(fname, challenge)
                elif nRandom >= 96 and nRandom <= 100:
                    fname = "platinum"
                    c = self.generateCoins(fname, challenge)
                self.items.append(c)
                        
                
            #Gems and art pieces
            nRandom = random.randint(1,100)
            if nRandom > 81:            
                if nRandom >= 82 and nRandom <= 95:
                    for i in range(random.randint(1,3)):
                        fname = "gemstone"
                        goa = self.generateGemOrArt(fname)
                        self.items.append(goa)
                elif nRandom >= 96 and nRandom <= 100:
                    for i in range(random.randint(1,3)):
                        fname = "artpiece"
                        goa = self.generateGemOrArt(fname)
                        self.items.append(goa)
                
            #Mundane and magic objects
            nRandom = random.randint(1,100)
            if nRandom > 49:
                if nRandom >= 50 and nRandom <= 85:
                    o = self.generateObject()
                    self.items.append(o)
                elif nRandom >= 86 and nRandom <= 100:
                    o = self.classObjectMagic("minor")
                    self.items.append(o)
                    
        elif challenge == 3:
            #Coin
            nRandom = random.randint(1,100)
            if nRandom > 11:            
                if nRandom >= 12 and nRandom <= 21:
                    fname = "copper"                
                    c = self.generateCoins(fname, challenge)
                elif nRandom >= 22 and nRandom <= 41:
                    fname = "silver"
                    c = self.generateCoins(fname, challenge)
                elif nRandom >= 42 and nRandom <= 95:
                    fname = "gold"
                    c = self.generateCoins(fname, challenge)
                elif nRandom >= 96 and nRandom <= 100:
                    fname = "platinum"
                    c = self.generateCoins(fname, challenge)
                self.items.append(c)
                        
                
            #Gems and art pieces
            nRandom = random.randint(1,100)
            if nRandom > 77:            
                if nRandom >= 78 and nRandom <= 95:
                    for i in range(random.randint(1,3)):
                        fname = "gemstone"
                        goa = self.generateGemOrArt(fname)
                        self.items.append(goa)
                elif nRandom >= 96 and nRandom <= 100:
                    for i in range(random.randint(1,3)):
                        fname = "artpiece"
                        goa = self.generateGemOrArt(fname)
                        self.items.append(goa)
                
            #Mundane and magic objects
            nRandom = random.randint(1,100)
            if nRandom > 49:
                if nRandom >= 50 and nRandom <= 79:
                    for i in range(random.randint(1,3)):
                        o = self.generateObject()
                        self.items.append(o)
                elif nRandom >= 80 and nRandom <= 100:
                    o = self.classObjectMagic("minor")
                    self.items.append(o)
                    
        elif challenge == 4:
            #Coin
            nRandom = random.randint(1,100)
            if nRandom > 11:            
                if nRandom >= 12 and nRandom <= 21:
                    fname = "copper"                
                    c = self.generateCoins(fname, challenge)
                elif nRandom >= 22 and nRandom <= 41:
                    fname = "silver"
                    c = self.generateCoins(fname, challenge)
                elif nRandom >= 42 and nRandom <= 95:
                    fname = "gold"
                    c = self.generateCoins(fname, challenge)
                elif nRandom >= 96 and nRandom <= 100:
                    fname = "platinum"
                    c = self.generateCoins(fname, challenge)
                self.items.append(c)
                        
                
            #Gems and art pieces
            nRandom = random.randint(1,100)
            if nRandom > 70:            
                if nRandom >= 71 and nRandom <= 95:
                    for i in range(random.randint(1,4)):
                        fname = "gemstone"
                        goa = self.generateGemOrArt(fname)
                        self.items.append(goa)
                elif nRandom >= 96 and nRandom <= 100:
                    for i in range(random.randint(1,3)):
                        fname = "artpiece"
                        goa = self.generateGemOrArt(fname)
                        self.items.append(goa)
                
            #Mundane and magic objects
            nRandom = random.randint(1,100)
            if nRandom > 42:
                if nRandom >= 43 and nRandom <= 62:
                    for i in range(random.randint(1,4)):
                        o = self.generateObject()
                        self.items.append(o)
                elif nRandom >= 63 and nRandom <= 100:
                    o = self.classObjectMagic("minor")
                    self.items.append(o)
                    
        elif challenge == 5:
            #Coin
            nRandom = random.randint(1,100)
            print
            print
            print (nRandom)
            print
            print
            if nRandom > 10:            
                if nRandom >= 11 and nRandom <= 19:
                    fname = "copper"                
                    c = self.generateCoins(fname, challenge)
                elif nRandom >= 20 and nRandom <= 38:
                    fname = "silver"
                    c = self.generateCoins(fname, challenge)
                elif nRandom >= 39 and nRandom <= 95:
                    fname = "gold"
                    c = self.generateCoins(fname, challenge)
                elif nRandom >= 96 and nRandom <= 100:
                    fname = "platinum"
                    c = self.generateCoins(fname, challenge)
                self.items.append(c)
                        
                
            #Gems and art pieces
            nRandom = random.randint(1,100)
            print
            print
            print (nRandom)
            print
            print
            if nRandom > 60:            
                if nRandom >= 61 and nRandom <= 95:
                    for i in range(random.randint(1,4)):
                        fname = "gemstone"
                        goa = self.generateGemOrArt(fname)
                        self.items.append(goa)
                elif nRandom >= 96 and nRandom <= 100:
                    for i in range(random.randint(1,4)):
                        fname = "artpiece"
                        goa = self.generateGemOrArt(fname)
                        self.items.append(goa)
                
            #Mundane and magic objects
            nRandom = random.randint(1,100)
            print
            print
            print (nRandom)
            print
            print
            if nRandom > 57:
                if nRandom >= 58 and nRandom <= 67:
                    for i in range(random.randint(1,4)):
                        o = self.generateObject()
                        self.items.append(o)
                elif nRandom >= 68 and nRandom <= 100:
                    for i in range(random.randint(1,3)):
                        o = self.classObjectMagic("minor")
                        self.items.append(o)
                        
        elif challenge == 6:
            #Coin
            nRandom = random.randint(1,100)
            if nRandom > 10:            
                if nRandom >= 11 and nRandom <= 18:
                    fname = "copper"                
                    c = self.generateCoins(fname, challenge)
                elif nRandom >= 19 and nRandom <= 37:
                    fname = "silver"
                    c = self.generateCoins(fname, challenge)
                elif nRandom >= 38 and nRandom <= 95:
                    fname = "gold"
                    c = self.generateCoins(fname, challenge)
                elif nRandom >= 96 and nRandom <= 100:
                    fname = "platinum"
                    c = self.generateCoins(fname, challenge)
                self.items.append(c)
                        
                
            #Gems and art pieces
            nRandom = random.randint(1,100)
            if nRandom > 56:            
                if nRandom >= 57 and nRandom <= 92:
                    for i in range(random.randint(1,4)):
                        fname = "gemstone"
                        goa = self.generateGemOrArt(fname)
                        self.items.append(goa)
                elif nRandom >= 93 and nRandom <= 100:
                    for i in range(random.randint(1,4)):
                        fname = "artpiece"
                        goa = self.generateGemOrArt(fname)
                        self.items.append(goa)
                
            #Mundane and magic objects
            nRandom = random.randint(1,100)
            if nRandom > 54:
                if nRandom >= 55 and nRandom <= 59:
                    for i in range(random.randint(1,4)):
                        o = self.generateObject()
                        self.items.append(o)
                elif nRandom >= 60 and nRandom <= 99:
                    for i in range(random.randint(1,3)):
                        o = self.classObjectMagic("minor")
                        self.items.append(o)
                elif nRandom == 100:
                    for i in range(random.randint(1,1)):
                        o = self.classObjectMagic("medium")
                        self.items.append(o)
        elif challenge == 7:
            #Coin
            nRandom = random.randint(1,100)
            print
            print
            print (nRandom)
            print
            print
            if nRandom > 11:            
                if nRandom >= 12 and nRandom <= 18:
                    fname = "copper"                
                    c = self.generateCoins(fname, challenge)
                elif nRandom >= 19 and nRandom <= 35:
                    fname = "silver"
                    c = self.generateCoins(fname, challenge)
                elif nRandom >= 36 and nRandom <= 93:
                    fname = "gold"
                    c = self.generateCoins(fname, challenge)
                elif nRandom >= 94 and nRandom <= 100:
                    fname = "platinum"
                    c = self.generateCoins(fname, challenge)
                self.items.append(c)
                        
                
            #Gems and art pieces
            nRandom = random.randint(1,100)
            print
            print
            print (nRandom)
            print
            print
            if nRandom > 48:            
                if nRandom >= 49 and nRandom <= 88:
                    for i in range(random.randint(1,4)):
                        fname = "gemstone"
                        goa = self.generateGemOrArt(fname)
                        self.items.append(goa)
                elif nRandom >= 89 and nRandom <= 100:
                    for i in range(random.randint(1,4)):
                        fname = "artpiece"
                        goa = self.generateGemOrArt(fname)
                        self.items.append(goa)
                
            #Mundane and magic objects
            nRandom = random.randint(1,100)
            print
            print
            print (nRandom)
            print
            print
            if nRandom > 51:
                if nRandom >= 52 and nRandom <= 97:
                    for i in range(random.randint(1,3)):
                        o = self.classObjectMagic("minor")
                        self.items.append(o)
                elif nRandom >= 98 and nRandom <= 100:
                    for i in range(random.randint(1,1)):
                        o = self.classObjectMagic("medium")
                        self.items.append(o)
                        
        elif challenge == 8:
            #Coin
            nRandom = random.randint(1,100)
            print
            print
            print (nRandom)
            print
            print
            if nRandom > 10:            
                if nRandom >= 11 and nRandom <= 15:
                    fname = "copper"                
                    c = self.generateCoins(fname, challenge)
                elif nRandom >= 16 and nRandom <= 29:
                    fname = "silver"
                    c = self.generateCoins(fname, challenge)
                elif nRandom >= 30 and nRandom <= 87:
                    fname = "gold"
                    c = self.generateCoins(fname, challenge)
                elif nRandom >= 88 and nRandom <= 100:
                    fname = "platinum"
                    c = self.generateCoins(fname, challenge)
                self.items.append(c)
                        
                
            #Gems and art pieces
            nRandom = random.randint(1,100)
            print
            print
            print (nRandom)
            print
            print
            if nRandom > 45:            
                if nRandom >= 46 and nRandom <= 85:
                    for i in range(random.randint(1,6)):
                        fname = "gemstone"
                        goa = self.generateGemOrArt(fname)
                        self.items.append(goa)
                elif nRandom >= 86 and nRandom <= 100:
                    for i in range(random.randint(1,4)):
                        fname = "artpiece"
                        goa = self.generateGemOrArt(fname)
                        self.items.append(goa)
                
            #Mundane and magic objects
            nRandom = random.randint(1,100)
            print
            print
            print (nRandom)
            print
            print
            if nRandom > 48:
                if nRandom >= 49 and nRandom <= 96:
                    for i in range(random.randint(1,3)):
                        o = self.classObjectMagic("minor")
                        self.items.append(o)
                elif nRandom >= 97 and nRandom <= 100:
                    for i in range(random.randint(1,1)):
                        o = self.classObjectMagic("medium")
                        self.items.append(o)
        
        self.calculateValue()
        self.diferenceValue(challenge)
            

    def generateMagicObject(self, fname, typeMagic):
        print ("Generating magic object")
        listOMagic = []
        infile = open("library/" + fname, "r")
        line = infile.readline()
        for line in infile:
            listOMagic.append(line)
        
        #Select a random object
        mObject = random.sample(listOMagic, 1)
        mObject = mObject[0].split(':')
        
        #Create a return object
        o = MagicObject()
        o.setName(mObject[0])
        o.setValue(int(mObject[1]))
        o.setTypeMagic(typeMagic)
        o.setPropertie(mObject[2])
        o.setReference(mObject[3])
        
        return o
        
        
    def classObjectMagic(self, typeMagic):
        print ("Selecting class of magic object")
        nRandom = random.randint(1,100)        
        
        #Select type object depends magic power
        if typeMagic is "minor":
            if nRandom >= 1 and nRandom <= 4:
                #Magic armor
                fname = "minorArmor"
                print ("Armadura/Escudo menor")
                
                a = self.generateArmor()
                a.setValue(0)
                return a                
                
            elif nRandom >= 5 and nRandom <= 9:
                #Magic weapon
                fname = "minorWeapon"
                weaponBase = self.generateWeapon(True)
                
                #Random
                flag = False
                while flag is False:
                    nRandom = random.randint(1,100)
                    if nRandom >= 1 and nRandom <= 70:
                        name = "+1"
                        value = 2000
                        newName = weaponBase.getName() + ' ' + name
                        weaponBase.setName(newName)
                        weaponBase.setValue(weaponBase.getValue() + value)
                        flag = True
                        
                    elif nRandom >= 71 and nRandom <= 85:
                        name = "+2"
                        value = 8000
                        newName = weaponBase.getName() + ' ' + name
                        weaponBase.setName(newName)
                        weaponBase.setValue(weaponBase.getValue() + value)
                        flag = True
                        
                    elif nRandom >= 86 and nRandom <= 90:
                        fname = "minorSpecificWeapon"
                        weaponBase = self.generateMagicObject(fname, typeMagic)
                        flag = True
                        
                    elif nRandom >= 91 and nRandom <= 100:
                        if "distancia" in weaponBase.getTypeWeapon():
                            fname = "minorDistanceWeapon"
                        magicWeapon = self.generateMagicObject(fname, typeMagic)
                        newName = weaponBase.getName() + ' ' + name
                        weaponBase.setName(newName)
                        weaponBase.setValue(weaponBase.getValue() + magicWeapon.getValue)
                        
                
                return weaponBase
                
            elif nRandom >= 10 and nRandom <= 44:
                #Potion
                fname = "minorPotion"
                potion = self.generateMagicObject(fname, typeMagic)
                newName = potion.getName() + ' ' + "potion"
                potion.setName(newName)
                
                return potion
                
            elif nRandom >= 45 and nRandom <= 46:
                #Ring
                fname = "minorRing"
                ring = self.generateMagicObject(fname, typeMagic)
                newName = ring.getName() + ' ' + "ring"
                ring.setName(newName)                
                
                return ring
                
            elif nRandom >= 47 and nRandom <= 81:
                #Scroll
                fname = "minorScroll"
                print ("pergamino menor")                
                a = self.generateWeapon()
                a.setValue(0)
                return a                
                
            elif nRandom >= 82 and nRandom <= 91:
                #Wand
                fname = "minorWand"
                wand = self.generateMagicObject(fname, typeMagic)
                newName = wand.getName() + ' ' + "wand"
                wand.setName(newName)
                
                return wand
            elif nRandom >= 92 and nRandom <= 100:
                #Wonderful item
                fname = "minorWonderful"
                wonder = self.generateMagicObject(fname, typeMagic)
                
                return wonder
                
        elif typeMagic is "medium":
            if nRandom >= 1 and nRandom <= 10:
                #Magic armor
                fname = "mediumArmor"
                print ("Armadura/Escudo intermedio")                
                a = self.generateArmor()
                a.setValue(0)
                return a    
                
            elif nRandom >= 11 and nRandom <= 20:
                #Magic weapon
                fname = "mediumWeapon"
                weaponBase = self.generateWeapon(True)
                
                #Random
                flag = False
                while flag is False:
                    nRandom = random.randint(1,100)
                    if nRandom >= 1 and nRandom <= 10:
                        name = "+1"
                        value = 2000
                        newName = weaponBase.getName() + ' ' + name
                        weaponBase.setName(newName)
                        weaponBase.setValue(weaponBase.getValue() + value)
                        flag = True
                        
                    elif nRandom >= 11 and nRandom <= 20:
                        name = "+2"
                        value = 8000
                        newName = weaponBase.getName() + ' ' + name
                        weaponBase.setName(newName)
                        weaponBase.setValue(weaponBase.getValue() + value)
                        flag = True
                    
                    elif nRandom >= 21 and nRandom <= 58:
                        name = "+3"
                        value = 18000
                        newName = weaponBase.getName() + ' ' + name
                        weaponBase.setName(newName)
                        weaponBase.setValue(weaponBase.getValue() + value)
                        flag = True                    
                    
                    elif nRandom >= 59 and nRandom <= 62:
                        name = "+4"
                        value = 32000
                        newName = weaponBase.getName() + ' ' + name
                        weaponBase.setName(newName)
                        weaponBase.setValue(weaponBase.getValue() + value)
                        flag = True                    
                    
                    elif nRandom >= 63 and nRandom <= 68:
                        fname = "mediumSpecificWeapon"
                        weaponBase = self.generateMagicObject(fname, typeMagic)
                        flag = True
                        
                    elif nRandom >= 69 and nRandom <= 100:
                        if "distancia" in weaponBase.getTypeWeapon():
                            fname = "minorDistanceWeapon"
                        magicWeapon = self.generateMagicObject(fname, typeMagic)
                        newName = weaponBase.getName() + ' ' + name
                        weaponBase.setName(newName)
                        weaponBase.setValue(weaponBase.getValue() + magicWeapon.getValue)
                        
                
                return weaponBase
                
            elif nRandom >= 21 and nRandom <= 30:
                #Potion
                fname = "mediumPotion"
                potion = self.generateMagicObject(fname, typeMagic)
                newName = potion.getName() + ' ' + "potion"
                potion.setName(newName)
                
                return potion
                
            elif nRandom >= 31 and nRandom <= 40:
                #Ring
                fname = "mediumRing"
                ring = self.generateMagicObject(fname, typeMagic)
                newName = ring.getName() + ' ' + "ring"
                ring.setName(newName)                 
                
                return ring
                
            elif nRandom >= 41 and nRandom <= 50:
                #Rod
                fname = "mediumRod"
                rod = self.generateMagicObject(fname, typeMagic)
                newName = rod.getName() + ' ' + "rod"
                rod.setName(newName)
                
                return rod
            elif nRandom >= 51 and nRandom <= 65:
                #Scroll
                fname = "mediumScroll"
                print ("pergamino intermedio")                
                a = self.generateArmor()
                a.setValue(0)
                return a
                
            elif nRandom >= 66 and nRandom <= 68:
                #Staff
                fname = "mediumStaff"
                staff = self.generateMagicObject(fname, typeMagic)
                newName = staff.getName() + ' ' + "staff"
                staff.setName(newName)
                
                return staff
                
            elif nRandom >= 69 and nRandom <= 83:
                #Wand
                fname = "mediumWand"
                wand = self.generateMagicObject(fname, typeMagic)
                newName = wand.getName() + ' ' + "wand"
                wand.setName(newName)
                
                return wand
                
            elif nRandom >= 84 and nRandom <= 100:
                #Wonderful item
                fname = "mediumWonderful"
                wonder = self.generateMagicObject(fname, typeMagic)
                
                return wonder
            
        elif typeMagic is "major":
            if nRandom >= 1 and nRandom <= 10:
                #Magic armor
                fname = "majorArmor"
                print ("Armadura/Escudo mayor")                
                a = self.generateArmor()
                a.setValue(0)
                return a    
                
            elif nRandom >= 11 and nRandom <= 20:
                #Magic weapon
                fname = "majorWeapon"
                weaponBase = self.generateWeapon(True)
                
                #Random
                flag = False
                while flag is False:
                    nRandom = random.randint(1,100)
                    if nRandom >= 1 and nRandom <= 20:
                        name = "+3"
                        value = 18000
                        newName = weaponBase.getName() + ' ' + name
                        weaponBase.setName(newName)
                        weaponBase.setValue(weaponBase.getValue() + value)
                        flag = True
                        
                    elif nRandom >= 21 and nRandom <= 38:
                        name = "+4"
                        value = 32000
                        newName = weaponBase.getName() + ' ' + name
                        weaponBase.setName(newName)
                        weaponBase.setValue(weaponBase.getValue() + value)
                        flag = True
                    
                    elif nRandom >= 39 and nRandom <= 49:
                        name = "+5"
                        value = 50000
                        newName = weaponBase.getName() + ' ' + name
                        weaponBase.setName(newName)
                        weaponBase.setValue(weaponBase.getValue() + value)
                        flag = True                    
                    
                    elif nRandom >= 50 and nRandom <= 63:
                        fname = "majorSpecificWeapon"
                        weaponBase = self.generateMagicObject(fname, typeMagic)
                        flag = True
                        
                    elif nRandom >= 64 and nRandom <= 100:
                        if "distancia" in weaponBase.getTypeWeapon():
                            fname = "minorDistanceWeapon"
                        magicWeapon = self.generateMagicObject(fname, typeMagic)
                        newName = weaponBase.getName() + ' ' + name
                        weaponBase.setName(newName)
                        weaponBase.setValue(weaponBase.getValue() + magicWeapon.getValue)
                        
                
                return weaponBase
                
            elif nRandom >= 21 and nRandom <= 25:
                #Potion
                fname = "majorPotion"
                potion = self.generateMagicObject(fname, typeMagic)
                newName = potion.getName() + ' ' + "potion"
                potion.setName(newName)
                
                return potion
                
            elif nRandom >= 26 and nRandom <= 35:
                #Ring
                fname = "majorRing"
                ring = self.generateMagicObject(fname, typeMagic)
                newName = ring.getName() + ' ' + "ring"
                ring.setName(newName)                 
                
                return ring
                
            elif nRandom >= 36 and nRandom <= 45:
                #Rod
                fname = "majorRod"
                rod = self.generateMagicObject(fname, typeMagic)
                rod.setName(rod.getName() + ' ' + "rod")
                
                return rod
                
            elif nRandom >= 46 and nRandom <= 55:
                #Scroll
                fname = "majorScroll"
                print ("pergamino mayor")                
                a = self.generateArmor()
                a.setValue(0)
                return a
                
            elif nRandom >= 56 and nRandom <= 75:
                #Staff
                fname = "majorStaff"
                staff = self.generateMagicObject(fname, typeMagic)
                newName = staff.getName() + ' ' + "staff"
                staff.setName(newName)
                
                return staff
                
            elif nRandom >= 76 and nRandom <= 80:
                #Wand
                fname = "majorWand"
                wand = self.generateMagicObject(fname, typeMagic)
                newName = wand.getName() + ' ' + "wand"
                wand.setName(newName)
                
                return wand
                
            elif nRandom >= 81 and nRandom <= 100:
                #Wonderful item
                fname = "majorWonderful"
                wonder = self.generateMagicObject(fname, typeMagic)
                
                return wonder
                
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
            c = Coin()
            c.setTypeCoin("gold")
            c.setValue(self.value - rest)
            self.items.append(c)            
            self.setValue(self.value - rest)
            
        
        #8, 8, 7, 5, 8
        
if __name__ == "__main__":
    t = Treasure()
    t.generateTreasure(5)
    
    tesoro = t.getItems()
    for i in tesoro:
        if type(i) is Coin:
            print (i.getTypeCoin())
            print (i.getValue())
        else:
            print (i.getName())
            print (i.getValue())
    print ("Hasta aqui sin ningun fallo")