""" This is the Player class and it handles data related to the Player instance. """
from Generic.Model import Model

from Entities.Inventory.InventoryModel import InventoryModel
from Entities.Player.Attributes.AttributeModel import AttributeModel


class PlayerModel(Model):

    def __init__(self, playerName):
        self.health = 10
        self.level = 1
        self.name = playerName
        self.stamina = 10
        
        self.inventory = InventoryModel()

        # Attributes
        self.strength = AttributeModel()
        self.woodWorkingSkill = AttributeModel()

        # Attacks
        self.basicAttack = 2
        self.specialAttack = 5


    def checkInventory(self):
        self.inventory.display()


    def checkStats(self):
        print("Player Stats")
        print("Current level: ", self.level)
        print("Current Health: ", self.health)
        print("Strength: ", self.strength.attributeLevel, "\n")

#TODO: Delete this function
    def cutWood(self, woodWorker):
        if(self.inventory.isSlotsFull()):
            print("Your inventory is full!\n")
            print("You didn't pick up any wood.\n")
            return False
        else:
            # TODO Make wood working class give out wood
            if(woodWorker.worker.isWoodGained()):
                print("You got 1 piece of wood!\n")
                self.inventory.addItem('Wood', 1)
                self.playerStrength.gainExp()
                return True
            else:
                print("You failed to cut the tree.\n")
                return False

# TODO: Create a file to hold how much health should increase
# based on what the player eats.
    def eatFood(self):
        self.setHealth(self.getHealth() + 5)

    def gainExperiencePoints(self, experienceGained):
        self.playerExpPoints = (self.playerExpPoints + experienceGained)

    def isPlayerDead(self):
        if(self.getHealth() <= 0):
            return True
        else:
            return False

    def killPlayer(self):
        self.setHealth(0)

    def levelUp(self, levelGained):
        self.setLevel(self.getLevel() + levelGained)

    def reduceHealth(self, damageTaken):
        self.setHealth(self.getHealth() + damageTaken)

    def restoreHealth(self, amountRestored):
        self.setHealth(self.getHealth() + amountRestored)


    """ Getters and Setters """

    def getBasicAttack(self):
        return self.basicAttack

    def getHealth(self):
        return self.health

    def getLevel(self):
        return self.level

    def getSpecialAttack(self):
        return self.specialAttack
    
    def getStamina(self):
        return self.stamina

    def setBasicAttack(self, newBasicAttack):
        self.basicAttack = newBasicAttack

    def setHealth(self, newHealth):
        self.health = newHealth
    
    def setLevel(self, newLevel):
        self.level = newLevel
    
    def setSpecialAttack(self, newSpecialAttack):
        self.specialAttack = newSpecialAttack
    
    def setStamina(self, newStamina):
        self.stamina = newStamina
