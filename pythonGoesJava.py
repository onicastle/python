##pythonGoesJava
##Oni Castillo Ruiz
##Univeristy Of Puerto Rico Recinto de Mayaguez
##December 2018

class Dog:


    def __init__(self, name, age, breed, sex, hasPartner):
        
        self.hasPartner = false
        self.name = name
        self.age = age
        self.sex = sex
        self.breed = breed

    def smallBark(self):
        print("guao... guao.")
        
    def getHasPartner(self):
        return self.hasPartner

    def setTrueHasPartner(self):
        self.hasPartner = true
        return self.hasPartner
    
    def isDogSingle(self):
        if(self.hasPartner != false):
            return true
        else:
            return false
    
    def bigBark(self):
        print("BARK!")

    def oneYearOlder(self):
        self.age = self.age + 1
