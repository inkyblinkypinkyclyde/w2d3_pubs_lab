class Pub:
    def __init__(self, name, till, drinks, foods, drunkenness_threshold):
        self.name = name
        self.till = till
        self.drinks = drinks
        self.foods = foods
        self.drunkenness_threshold = drunkenness_threshold
    
    def increase_till(self, drink):
        self.till += drink.price
    
    def add_drinks_to_pub(self, drink):
        self.drinks.append(drink)

    def remove_drinks_from_pub(self, drink):
        for drink_ in self.drinks:
            if drink_ == drink:
                self.drinks.remove(drink)
    
    def add_food_to_pub(self, food):
        self.foods.append(food)

    def remove_food_from_pub(self,food):
        for food_ in self.drinks:
            if food_ == food:
                self.foods.remove(food)


    
    def find_drink_by_name(self, drink_name):
        for current_drink in self.drinks:
            if current_drink.name == drink_name:
                return current_drink
    
    def find_drink_in_list(self, drink):
        if drink in self.drinks:
            return True
    
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
        if self.check_drunkenness(customer) and self.check_age(customer) and customer.check_cash(drink) and self.find_drink_in_list(drink):
            return True
        else:
            return False
    
    def buy_drink(self, customer, drink):
        if self.can_buy_drink(customer, drink) == True:
            self.increase_till(drink)
            self.remove_drinks_from_pub(drink)
            customer.subtract_cash(drink)
            customer.increase_drunkenness(drink)
            


    
