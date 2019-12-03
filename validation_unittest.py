import unittest
from hot_dog_stand import calculate_day_total, calculate_total_profit, add_sale


### Added function to test 'Test 6') ###
def calculate_transaction_total(a, b):
    return a + b



class TestingValues(unittest.TestCase):
    ########## Testing Input Variables #############
    numb_of_hotdogs = 5 # number of hot dogs sold in a transaction
    price = 5           # price of each hot dog sold in transaction

    ### Test 1 ###
    def test_numb_of_hotdogs_is_an_integer(self):
        # Verify number of hotdogs is an integer
        self.assertEqual(self.numb_of_hotdogs, int(self.numb_of_hotdogs))
        
    ### Test 2 ###
    def test_numb_of_hotdogs_is_positive(self):
        # Verify number of hotdogs is positive
        self.assertTrue(self.numb_of_hotdogs > 0)

    ### Test 3 ###
    def test_price_is_a_number(self):
        # Verify price is a number
        self.assertEqual(self.price, float(self.price))

    ### Test 4 ###
    def test_price_is_positive(self):
        # Verify price is positive
        self.assertTrue(self.price > 0)

    ### Test 5 ###
    def test_price_is_two_decimal_places(self):
        self.assertEqual(self.price, round(self.price,2))

    ### Test 6 ###
    ### Name of Function?????? NOT YET DEFINED (calculate_transaction_total)####
    def test_total_of_transaction(self):
        self.assertEqual(self.numb_of_hotdogs + self.price, calculate_transaction_total(self.numb_of_hotdogs, self.price))


if __name__ == '__main__':
    unittest.main(verbosity=2)
