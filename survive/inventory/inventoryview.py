from survive.generic.view import View

class InventoryView(View):
    
    def __init__(self):
        pass

    def displayStart(self):
        print("Possible Actions:\n")
        print("(1)  Display Inventory")
        print("(2)  Eat Food")  
        print("(3)  Craft") # Point to CrafterView
        print("(9)  Use Boat") # End Game choice
        print("(10) Clear Screen")
        print("(0)  Back To Game\n")


    def displayEnd(self):
        print("Moving back to game.\n")

    def displayRequestAction(self):
        print("Enter an action.\n")