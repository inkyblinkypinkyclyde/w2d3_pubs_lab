import unittest

from src.pub import Pub
from src.drinks import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100, [])
        self.drink1 = Drink("Miruvor", 50)
        self.drink2 = Drink("Ale", 2)
        self.customer = Customer("Frodo", 20)

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
        self.assertEqual("Frodo", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(20, self.customer.wallet)
    
    def test_customer_add_money(self):
        self.customer.add_cash(-2)
        self.assertEqual(18, self.customer.wallet)

    def test_customer_can_afford__false(self):
        self.pub.add_drinks_to_pub(self.drink1)
        answer = self.customer.check_cash(self.drink1)
        self.assertEqual(False, answer)

    def test_customer_can_afford__true(self):
        self.pub.add_drinks_to_pub(self.drink2)
        answer = self.customer.check_cash(self.drink2)
        self.assertEqual(True, answer)


    