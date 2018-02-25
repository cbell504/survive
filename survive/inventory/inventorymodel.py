class Inventory(object):
    def __init__(self):
        self._slots_max_size = 10
        self._slots = {
            "Wood": 0,
            "Shelter": 0,
            "Boat": 0,
            "Food": 0
        }

    def add_item(self, item, total_items):
        self._slots.update({item: self._slots.get(item) + total_items})

    def display(self):
        for key, value in self._slots.items():
            print(key, ":", value)
        print("\n")

    def get_item(self, item):
        try:
            return self._slots.get(item)
        except:
            print("Item does not exist")

    def get_slots(self):
        return self._slots
    
    def get_slots_max_size(self):
        self._slots_max_size
    
    def increase_max_size(self, max_size):
        self._slots_max_size = max_size

    def is_slots_full(self):
        if(sum(self._slots.values()) >= self._slots_max_size):
            return True
        else:
            return False

    def remove_item(self, item, total_items):
        self._slots.update({item: self._slots.get(item) - total_items})
