class InventoryModel(object):

    def __init__(self):
        self.slots = {'Wood': 0, 'Shelter': 0, 'Boat': 0}
        self.slotsMaxSize = 10

    def addItem(self, item, numberOfItems):
        self.slots.update({item: self.slots.get(item) + numberOfItems})

    def display(self):
        for key, value in self.slots.items():
            print(key, ":", value)
        print("\n")

    def getItem(self, item):
        try:
            return self.slots.get(item)
        except:
            print("Item does not exist")

    def isSlotsFull(self):
        if(sum(self.slots.values()) >= self.slotsMaxSize):
            return True
        else:
            return False

    def removeItem(self, item, numberOfItems):
        self.slots.update({item: self.slots.get(item) - numberOfItems})