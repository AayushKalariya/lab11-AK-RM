#https://github.com/AayushKalariya/lab11-AK-RM
# Partner 1: Aayush Kalariya
# Partner 2: Rayan Mubarak

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(0,0),0)
        self.assertEqual(add(-10,5),-5)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(7,6), 1)
        self.assertEqual(sub(14,0), 14)
        self.assertEqual(sub(-4,4), -8)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2,3),6)
        self.assertEqual(mul(4,3),12)
        self.assertEqual(mul(8,3),24)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(5,10),2)
        self.assertEqual(div(2,10),5)
        self.assertEqual(div(10,100),10)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0,10)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(2,8),3)
        self.assertEqual(log(2,16),4)
        self.assertEqual(log(2,32),5)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            log(67,0)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(1,10)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4),5)
        self.assertEqual(hypotenuse(6,8),10)
        self.assertEqual(hypotenuse(5,12),13)

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(4),2)
        self.assertEqual(square_root(9),3)
        self.assertEqual(square_root(16),4)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
    