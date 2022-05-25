class Pub:
    def __init__(self, name, till, drinks, drunkenness_threshold):
        self.name = name
        self.till = till
        self.drinks = drinks
        self.drunkenness_threshold = drunkenness_threshold
    
    def increase_till(self, amount):
        self.till += amount
    
    def add_drinks_to_pub(self, drink):
        self.drinks.append(drink)
    
    def find_drink_by_name(self, drink_name):
        for current_drink in self.drinks:
            if current_drink.name == drink_name:
                return current_drink
    
    def check_age(self, customer):
        if customer.age >= 25:
            return True
        else:
            return False
    
    def check_drunkenness(self, customer):
        if customer.get_drunkenness() <= self.drunkenness_threshold:
            return True
        else:
            return False
    
    def can_buy_drink(self, customer, drink):
        if self.check_drunkenness(customer) and self.check_age(customer) and customer.check_cash(drink):
            return True
        else:
            return False
    
