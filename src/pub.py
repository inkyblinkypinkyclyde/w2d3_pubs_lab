class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
    
    def increase_till(self, amount):
        self.till += amount
    
    def add_drinks_to_pub(self, drink):
        self.drinks.append(drink)