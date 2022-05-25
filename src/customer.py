class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0

    
    def add_cash(self, item):
        self.wallet += item.price
    
    def subtract_cash(self, drink):
        self.wallet -= drink.price
        # self.wallet = 18
    
    def check_cash(self, drink):
        if self.wallet >= drink.price:
            return True
        else:
            return False

    def increase_drunkenness(self, drink):
        self.drunkenness += drink.alcohol_level
    
    def get_drunkenness(self):
        return self.drunkenness
    
    def can_buy_food(self, food):
        return self.wallet >= food.price
        
