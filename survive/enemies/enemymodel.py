from survive.generic.model import Model

# TODO: Raise error when values are set below zero

class EnemyModel(Model):
    
    def __init__(self):
        # Health 
        self.health = 10
        self.DEFAULT_HEALTH = 10

        # Name
        self.name = "Enemy"
        self.DEFAULT_NAME = "Enemy"

        # Attack Power
        self.basicAttack = 1
        self.DEFAULT_BASIC_ATTACK = 1
        self.specialAttack = 3
        self.DEFAULT_SPECIAL_ATTACK = 3

        self.level = 1
        self.DEFAULT_LEVEL = 1

    def isEnemyAlive(self):
        if(self.health > 1):
            return True
        else:
            return False
    

    # Getters and Setters

    def getBasicAttack(self):
        if(self.basicAttack):
            return self.basicAttack
        else:
            return self.DEFAULT_BASIC_ATTACK

    def getHealth(self):
        return self.health
    
    def getLevel(self):
        if(self.level):
            return self.level
        else:
            return self.DEFAULT_LEVEL

    def getName(self):
        if(self.name):
            return self.name
        else:
            return self.DEFAULT_NAME

    def getSpecialAttack(self):
        if(self.specialAttack):
            return self.specialAttack
        else:
            return self.DEFAULT_SPECIAL_ATTACK

    def setBasicAttack(self, newBasicAttack):
        if(newBasicAttack >= 0):
            self.basicAttack = newBasicAttack
        else:
            try:
                raise Exception('Enemy Basic Attack was attempted to be set below zero')
            except Exception as error:
                print("Error Caught: " + repr(error))
    
    def setHealth(self, newHealth):
        self.health = newHealth

    def setLevel(self, newLevel):
        if(newLevel >= 1):
            self.level = newLevel
        else:
            try:
                raise Exception('Enemy Level was attempted to be set below one.')
            except Exception as error:
                print("Error Caught: " + repr(error))
    
    def setName(self, newName):
        self.name = newName
    
    def setSpecialAttack(self, newSpecialAttack):
        if(newSpecialAttack >= 0):
            self.specialAttack = newSpecialAttack
        else:
            try:
                raise Exception('Enemy Special Attack was attempted to be set below zero.')
            except Exception as error:
                print("Error Caught: " + repr(error))