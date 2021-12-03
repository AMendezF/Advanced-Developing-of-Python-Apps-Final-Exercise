import unittest
import calclib.vector as calclib

from functools import reduce


class vecCalcAddTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = calclib.VecCalc()

    def test_that_add_calcs_positive_numbers(self):
        a=[1.0, 2.0]
        b=[3.0, 4.0]
        r=[4.0, 6.0]
        self.assertEqual(self.calc.addition(a, b), r)

    def test_that_add_calcs_negative_numbers(self):
        a=[-1.0, -2.0]
        b=[3.0, 4.0]
        r=[2.0, 2.0]
        self.assertEqual(self.calc.addition(a, b), r)

    def test_that_add_calcs_decimal_numbers(self):
        a=[0.1, 0.2]
        b=[0.3, 0.4]
        r=[0.4, 0.6]
        self.assertEqual(self.calc.addition(a, b), r)

    def test_that_add_bad_input_raises_error1a(self):
        a=[0.3, 0.4]
        b=None
        self.assertRaises(AssertionError, self.calc.addition, a, b)

    def test_that_add_bad_input_raises_error1b(self):
        a=None
        b=[0.1, 0.2]
        self.assertRaises(AssertionError, self.calc.addition, a, b)

    def test_that_add_bad_input_raises_error2(self):
        a=[]
        b=[]
        self.assertRaises(AssertionError, self.calc.addition, a, b)

    def test_that_add_bad_input_raises_error3a(self):
        a=[0.3, 0.4]
        b=[0.1, 2]
        self.assertRaises(AssertionError, self.calc.addition, a, b)

    def test_that_add_bad_input_raises_error3b(self):
        a=[0.3, 4]
        b=[0.1, 0.2]
        self.assertRaises(AssertionError, self.calc.addition, a, b)
    
    def test_that_add_bad_input_raises_error4a(self):
        a=[0.3, 0.4]
        b=[0.1]
        self.assertRaises(AssertionError, self.calc.addition, a, b)

    def test_that_add_bad_input_raises_error4b(self):
        a=[0.3]
        b=[0.1, 0.2]
        self.assertRaises(AssertionError, self.calc.addition, a, b)

class vecCalcSubTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = calclib.VecCalc()

    def test_that_sub_calcs_positive_numbers(self):
        a=[4.0, 6.0]
        b=[3.0, 4.0]
        r=[1.0, 2.0]
        self.assertEqual(self.calc.subtraction(a, b), r)

    def test_that_sub_calcs_negative_numbers(self):
        a=[1.0, 2.0]
        b=[-3.0, -4.0]
        r=[4.0, 6.0]
        self.assertEqual(self.calc.subtraction(a, b), r)

    def test_that_sub_calcs_decimal_numbers(self):
        a=[0.4, 0.6]
        b=[0.3, 0.4]
        r=[0.1, 0.2]
        self.assertEqual(self.calc.subtraction(a, b), r)

    def test_that_sub_bad_input_raises_error1a(self):
        a=[0.3, 0.4]
        b=None
        self.assertRaises(AssertionError, self.calc.subtraction, a, b)

    def test_that_sub_bad_input_raises_error1b(self):
        a=None
        b=[0.1, 0.2]
        self.assertRaises(AssertionError, self.calc.subtraction, a, b)

    def test_that_sub_bad_input_raises_error2(self):
        a=[]
        b=[]
        self.assertRaises(AssertionError, self.calc.subtraction, a, b)

    def test_that_sub_bad_input_raises_error3a(self):
        a=[0.3, 0.4]
        b=[0.1, 2]
        self.assertRaises(AssertionError, self.calc.subtraction, a, b)

    def test_that_sub_bad_input_raises_error3b(self):
        a=[0.3, 4]
        b=[0.1, 0.2]
        self.assertRaises(AssertionError, self.calc.subtraction, a, b)
    
    def test_that_sub_bad_input_raises_error4a(self):
        a=[0.3, 0.4]
        b=[0.1]
        self.assertRaises(AssertionError, self.calc.subtraction, a, b)

    def test_that_sub_bad_input_raises_error4b(self):
        a=[0.3]
        b=[0.1, 0.2]
        self.assertRaises(AssertionError, self.calc.subtraction, a, b)

class vecCalcMulTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = calclib.VecCalc()

    def test_that_mul_calcs_positive_numbers(self):
        a=[1.0, 2.0]
        b=[3.0, 4.0]
        r=[3.0, 8.0]
        self.assertEqual(self.calc.multiplication(a, b), r)

    def test_that_mul_calcs_negative_numbers(self):
        a=[-1.0, -2.0]
        b=[3.0, 4.0]
        r=[-3.0, -8.0]
        self.assertEqual(self.calc.multiplication(a, b), r)

    def test_that_mul_calcs_decimal_numbers(self):
        a=[0.1, 0.2]
        b=[0.3, 0.4]
        r=[0.03, 0.08]
        self.assertEqual(self.calc.multiplication(a, b), r)

    def test_that_mul_bad_input_raises_error1a(self):
        a=[0.3, 0.4]
        b=None
        self.assertRaises(AssertionError, self.calc.multiplication, a, b)

    def test_that_mul_bad_input_raises_error1b(self):
        a=None
        b=[0.1, 0.2]
        self.assertRaises(AssertionError, self.calc.multiplication, a, b)

    def test_that_mul_bad_input_raises_error2(self):
        a=[]
        b=[]
        self.assertRaises(AssertionError, self.calc.multiplication, a, b)

    def test_that_mul_bad_input_raises_error3a(self):
        a=[0.3, 0.4]
        b=[0.1, 2]
        self.assertRaises(AssertionError, self.calc.multiplication, a, b)

    def test_that_mul_bad_input_raises_error3b(self):
        a=[0.3, 4]
        b=[0.1, 0.2]
        self.assertRaises(AssertionError, self.calc.multiplication, a, b)
    
    def test_that_mul_bad_input_raises_error4a(self):
        a=[0.3, 0.4]
        b=[0.1]
        self.assertRaises(AssertionError, self.calc.multiplication, a, b)

    def test_that_mul_bad_input_raises_error4b(self):
        a=[0.3]
        b=[0.1, 0.2]
        self.assertRaises(AssertionError, self.calc.multiplication, a, b)

class vecCalcDivTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = calclib.VecCalc()

    def test_that_div_calcs_positive_numbers(self):
        a=[3.0, 4.0]
        b=[1.0, 2.0]
        r=[3.0, 2.0]
        self.assertEqual(self.calc.division(a, b), r)

    def test_that_div_calcs_negative_numbers(self):
        a=[3.0, 4.0]
        b=[-1.0, -2.0]
        r=[-3.0, -2.0]
        self.assertEqual(self.calc.division(a, b), r)

    def test_that_div_calcs_decimal_numbers(self):
        a=[0.3, 0.4]
        b=[0.1, 0.2]
        r=[3.0, 2.0]
        self.assertEqual(self.calc.division(a, b), r)

    def test_that_div_bad_input_raises_error1a(self):
        a=[0.3, 0.4]
        b=None
        self.assertRaises(AssertionError, self.calc.division, a, b)

    def test_that_div_bad_input_raises_error1b(self):
        a=None
        b=[0.1, 0.2]
        self.assertRaises(AssertionError, self.calc.division, a, b)

    def test_that_div_bad_input_raises_error2(self):
        a=[]
        b=[]
        self.assertRaises(AssertionError, self.calc.division, a, b)

    def test_that_div_bad_input_raises_error3a(self):
        a=[0.3, 0.4]
        b=[0.1, 2]
        self.assertRaises(AssertionError, self.calc.division, a, b)

    def test_that_div_bad_input_raises_error3b(self):
        a=[0.3, 4]
        b=[0.1, 0.2]
        self.assertRaises(AssertionError, self.calc.division, a, b)
    
    def test_that_div_bad_input_raises_error4a(self):
        a=[0.3, 0.4]
        b=[0.1]
        self.assertRaises(AssertionError, self.calc.division, a, b)

    def test_that_div_bad_input_raises_error4b(self):
        a=[0.3]
        b=[0.1, 0.2]
        self.assertRaises(AssertionError, self.calc.division, a, b)
        
    def test_that_div_by_zero_raises_error(self):
        a=[0.3, 0.4]
        b=[0.1, 0.0]
        self.assertRaises(AssertionError, self.calc.division, a, b)
