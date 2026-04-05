class Array:
    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def delete(self, item):
        if item in self.items:
            self.items.remove(item)

    def print_array(self):
        print(self.items)