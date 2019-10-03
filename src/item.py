class Item:
    def __init__(self, name = 'Placeholder', description='This is an item', item_view = ''''''):
        self.name = name
        self.description = description
        self.item_view = item_view

    def __str__(self):
        return f'{self.name}; {self.description}, \n{self.item_view}\n'

#test = Item("handle", "a handle to the well")
#print(test)