import unittest

from src.pub import Pub
from src.drinks import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100, [], 7)
        self.drink1 = Drink("Miruvor", 50, 10)
        self.drink2 = Drink("Ale", 2, 5)
        self.customer1 = Customer("Frodo", 20, 51)
        self.customer2 = Customer("Eowyn", 55, 24)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
    
    def test_pub_has_till100(self):
        self.assertEqual(100, self.pub.till)

    def test_increase_till(self):
        self.pub.increase_till(50)
        self.assertEqual(150, self.pub.till)
    
    def test_can_add_drinks(self):
        self.pub.add_drinks_to_pub(self.drink1)
        self.assertEqual(1, len(self.pub.drinks))
    
    def test_customer_has_name(self):
        self.assertEqual("Frodo", self.customer1.name)

    def test_customer_has_wallet(self):
        self.assertEqual(20, self.customer1.wallet)
    
    def test_customer_add_money(self):
        self.customer1.add_cash(-2)
        self.assertEqual(18, self.customer1.wallet)

    def test_can_find_drink(self):
        self.pub.add_drinks_to_pub(self.drink1)
        self.pub.add_drinks_to_pub(self.drink2)
        found_drink = self.pub.find_drink_by_name("Ale")
        self.assertEqual(self.drink2, found_drink)

    def test_customer_can_afford__false(self):
        self.pub.add_drinks_to_pub(self.drink1)
        answer = self.customer1.check_cash(self.drink1)
        self.assertEqual(False, answer)

    def test_customer_can_afford__true(self):
        self.pub.add_drinks_to_pub(self.drink2)
        answer = self.customer1.check_cash(self.drink2)
        self.assertEqual(True, answer)

    def test_check_age_true(self):
        answer = self.pub.check_age(self.customer1)
        self.assertEqual(True, answer)

    def test_check_age_false(self):
        answer = self.pub.check_age(self.customer2)
        self.assertEqual(False, answer)

    def test_increase_alcohol_level(self):
        self.customer1.increase_drunkennes(self.drink1)
        alc_level = self.customer1.drunkenness
        self.assertEqual(10, alc_level)

    def test_check_drunkenness_true(self):
        self.customer1.increase_drunkennes(self.drink1)
        answer = self.pub.check_drunkenness(self.customer1)
        self.assertEqual(False, answer)

    def test_check_drunkenness_false(self):
        answer = self.pub.check_drunkenness(self.customer1)
        self.assertEqual(True, answer)

    def test_can_buy_drink_true(self):
        answer = self.pub.can_buy_drink(self.customer1, self.drink2)
        self.assertEqual(True, answer)
    
    def test_can_buy_drink_false(self):
        self.customer1.increase_drunkennes(self.drink1)
        answer = self.pub.can_buy_drink(self.customer1, self.drink2)
        self.assertEqual(False, answer)


    