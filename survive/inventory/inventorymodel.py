class Inventory(object):

    def __init__(self):
        self.slots = {'Wood': 0, 'Shelter': 0, 'Boat': 0}
        self.slots_max_size = 10

    def add_item(self, item, total_items):
        self.slots.update({item: self.slots.get(item) + total_items})

    def display(self):
        for key, value in self.slots.items():
            print(key, ":", value)
        print("\n")

    def get_item(self, item):
        try:
            return self.slots.get(item)
        except:
            print("Item does not exist")

    def is_slots_full(self):
        if(sum(self.slots.values()) >= self.slots_max_size):
            return True
        else:
            return False

    def remove_item(self, item, total_items):
        self.slots.update({item: self.slots.get(item) - total_items})
