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
        self.assertEqual(self.calc.addition_calc([a, b]), r)

    def test_that_add_calcs_negative_numbers(self):
        a=[-1.0, -2.0]
        b=[3.0, 4.0]
        r=[2.0, 2.0]
        self.assertEqual(self.calc.addition_calc([a, b]), r)

    def test_that_add_calcs_decimal_numbers(self):
        a=[0.1, 0.2]
        b=[0.3, 0.4]
        r=[0.4, 0.6]
        self.assertEqual(self.calc.addition_calc([a, b]), r)

class vecCalcSubTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = calclib.VecCalc()

    def test_that_sub_calcs_positive_numbers(self):
        a=[4.0, 6.0]
        b=[3.0, 4.0]
        r=[1.0, 2.0]
        self.assertEqual(self.calc.subtraction_calc([a, b]), r)

    def test_that_sub_calcs_negative_numbers(self):
        a=[1.0, 2.0]
        b=[-3.0, -4.0]
        r=[4.0, 6.0]
        self.assertEqual(self.calc.subtraction_calc([a, b]), r)

    def test_that_sub_calcs_decimal_numbers(self):
        a=[0.4, 0.6]
        b=[0.3, 0.4]
        r=[0.1, 0.2]
        self.assertEqual(self.calc.subtraction_calc([a, b]), r)

class vecCalcMulTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = calclib.VecCalc()

    def test_that_mul_calcs_positive_numbers(self):
        a=[1.0, 2.0]
        b=[3.0, 4.0]
        r=[3.0, 8.0]
        self.assertEqual(self.calc.multiplication_calc([a, b]), r)

    def test_that_mul_calcs_negative_numbers(self):
        a=[-1.0, -2.0]
        b=[3.0, 4.0]
        r=[-3.0, -8.0]
        self.assertEqual(self.calc.multiplication_calc([a, b]), r)

    def test_that_mul_calcs_decimal_numbers(self):
        a=[0.1, 0.2]
        b=[0.3, 0.4]
        r=[0.03, 0.08]
        self.assertEqual(self.calc.multiplication_calc([a, b]), r)

class vecCalcDivTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = calclib.VecCalc()

    def test_that_div_calcs_positive_numbers(self):
        a=[3.0, 4.0]
        b=[1.0, 2.0]
        r=[3.0, 2.0]
        self.assertEqual(self.calc.division_calc([a, b]), r)

    def test_that_div_calcs_negative_numbers(self):
        a=[3.0, 4.0]
        b=[-1.0, -2.0]
        r=[-3.0, -2.0]
        self.assertEqual(self.calc.division_calc([a, b]), r)

    def test_that_div_calcs_decimal_numbers(self):
        a=[0.3, 0.4]
        b=[0.1, 0.2]
        r=[3.0, 2.0]
        self.assertEqual(self.calc.division_calc([a, b]), r)


if __name__ == '__main__':
    unittest.main()