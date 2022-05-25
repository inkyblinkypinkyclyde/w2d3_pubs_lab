class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        # self.alcohol_level = 0
    
    def add_cash(self, amount):
        self.wallet += amount
    
    def check_cash(self, drink):
        if self.wallet > drink.price:
            return True
        else:
            return False
