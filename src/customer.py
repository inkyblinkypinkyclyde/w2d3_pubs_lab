class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0

    
    def add_cash(self, amount):
        self.wallet += amount
    
    def check_cash(self, drink):
        if self.wallet >= drink.price:
            return True
        else:
            return False
    
    def increase_drunkennes(self, drink):
        self.drunkenness += drink.alcohol_level
    
    def get_drunkenness(self):
        return self.drunkenness
    
