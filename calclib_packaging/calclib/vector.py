"""
    calclib.vector
    ~~~~~~~~~~~~~~~~~~

    Vector calculator.
"""

import typing
from functools import reduce
import operator


class VecCalc():
    """
    A class with the functions required to operate with vectors.
    Ensures that input is valid and then returns the result.
    Maximum output decimal places may be changed to any non negative integer.
    """

    def __init__(self, precision=2):
        assert(self.__vector_precision_safe_check(precision) == True)

        # decimal result precision
        self.prec = precision

    def addition(self, vector1: typing.List[float], vector2: typing.List[float]) -> typing.List[float]:
        """
        Adds element-wise two float number list.

        :param vector1: first list of numbers.
        :type vector1: list[float]
        :param vector2: second list of numbers.
        :type vector2: list[float]
        :raise AssertionError: If the input is invalid.
        :return: The operation result.
        :rtype: list[float]
        """
        vector_list = [vector1, vector2]
        assert(self.addition_safe_check(*vector_list) == True)
        
        return self.__addition_calc(vector_list)

    def subtraction(self, vector1: typing.List[float], vector2: typing.List[float]) -> typing.List[float]:
        """
        Subtracts element-wise one float number list from another.

        :param vector1: first list of numbers. The minuend.
        :type vector1: list[float]
        :param vector2: second list of numbers. The subtrahend.
        :type vector2: list[float]
        :raise AssertionError: If the input is invalid.
        :return: The operation result. Also, the difference.
        :rtype: list[float]
        """
        vector_list = [vector1, vector2]
        assert(self.subtraction_safe_check(*vector_list) == True)
        
        return self.__subtraction_calc(vector_list)

    def multiplication(self, vector1: typing.List[float], vector2: typing.List[float]) -> typing.List[float]:
        """
        Multiplies element-wise one float number list by another.

        :param vector1: first list of numbers. The multiplicand.
        :type vector1: list[float]
        :param vector2: second list of numbers. The multiplier.
        :type vector2: list[float]
        :raise AssertionError: If the input is invalid.
        :return: The operation result.
        :rtype: list[float]
        """
        vector_list = [vector1, vector2]
        assert(self.multiplication_safe_check(*vector_list) == True)
        
        return self.__multiplication_calc(vector_list)

    def division(self, vector1: typing.List[float], vector2: typing.List[float]) -> typing.List[float]:
        """
        Divides element-wise one float number list by another.

        :param vector1: first list of numbers. The divisor.
        :type vector1: list[float]
        :param vector2: second list of numbers. The dividend.
        :type vector2: list[float]
        :raise AssertionError: If the input is invalid.
        :return: The operation result. Also, the quotient.
        :rtype: list[float]
        """
        vector_list = [vector1, vector2]
        assert(self.division_safe_check(*vector_list) == True)
        
        return self.__division_calc(vector_list)

    ### Safe Check Functions:
    #########################

    def addition_safe_check(self, vector1: list, vector2: list) -> bool:
        """
        Checks if the lists are a valid input to apply addition.

        :param vector1: first list.
        :type vector1: list
        :param vector2: second list.
        :type vector2: list
        :return: returns True if the lists are a valid input.
        :rtype: bool
        """
        safe = self.__basic_safe_check(vector1, vector2)
        return safe

    def subtraction_safe_check(self, vector1: list, vector2: list) -> bool:
        """
        Checks if the lists are a valid input to apply subtraction.

        :param vector1: first list. The minuend.
        :type vector1: list
        :param vector2: second list. The subtrahend.
        :type vector2: list
        :return: returns True if the lists are a valid input.
        :rtype: bool
        """
        safe = self.__basic_safe_check(vector1, vector2)
        return safe

    def multiplication_safe_check(self, vector1: list, vector2: list) -> bool:
        """
        Checks if the lists are a valid input to apply multiplication.

        :param vector1: first list. The multiplicand.
        :type vector1: list
        :param vector2: second list. The multiplier.
        :type vector2: list
        :return: returns True if the lists are a valid input.
        :rtype: bool
        """
        safe = self.__basic_safe_check(vector1, vector2)
        return safe

    def division_safe_check(self, vector1: list, vector2: list) -> bool:
        """
        Checks if the lists are a valid input to apply division.

        :param vector1: first list. The divisor.
        :type vector1: list
        :param vector2: second list. The dividend.
        :type vector2: list
        :return: returns True if the lists are a valid input.
        :rtype: bool
        """
        safe = (self.__basic_safe_check(vector1, vector2) and
                self.__vector_zero_safe_check(vector2)
            )
        return safe

    def __basic_safe_check(self, vector1: list, vector2: list) -> bool:
        safe = (self.__vector_is_list_safe_check(vector1) and
                self.__vector_is_list_safe_check(vector2) and
                self.__vector_not_empty_safe_check(vector1) and
                self.__vector_not_empty_safe_check(vector2) and
                self.__vector_type_safe_check(vector1) and
                self.__vector_type_safe_check(vector2) and
                self.__vector_length_safe_check(vector1, vector2)
            )
        return safe

    @staticmethod
    def __vector_is_list_safe_check(element) -> bool:
        return True if type(element) is list else False

    @staticmethod
    def __vector_not_empty_safe_check(vector: list) -> bool:
        return True if len(vector)>0 else False

    @staticmethod
    def __vector_type_safe_check(vector: list) -> bool:
        return True if all(isinstance(x, float) for x in vector) else False

    @staticmethod
    def __vector_length_safe_check(vector1: list, vector2: list) -> bool:
        return True if len(vector1) == len(vector2) else False

    @staticmethod
    def __vector_zero_safe_check(vector: typing.List[float]) -> bool:
        return True if 0.0 not in vector else False
    
    @staticmethod
    def __vector_precision_safe_check(prec) -> bool:
        return True if (type(prec) is int and prec >= 0) else False

    ### Vector Calc Functions:
    ##########################

    def __addition_calc(self, vector_list: typing.List[typing.List[float]]) -> typing.List[float]:
        return [round(self.__add(x), self.prec) for x in zip(*vector_list)]

    def __subtraction_calc(self, vector_list: typing.List[typing.List[float]]) -> typing.List[float]:
        return [round(self.__sub(x), self.prec) for x in zip(*vector_list)]

    def __multiplication_calc(self, vector_list: typing.List[typing.List[float]]) -> typing.List[float]:
        return [round(self.__mul(x), self.prec) for x in zip(*vector_list)]

    def __division_calc(self, vector_list: typing.List[typing.List[float]]) -> typing.List[float]:
        return [round(self.__div(x), self.prec) for x in zip(*vector_list)]
    
    @staticmethod
    def __add(iterable):
        return reduce(operator.add, iterable)

    @staticmethod
    def __sub(iterable):
        return reduce(operator.sub, iterable)

    @staticmethod
    def __mul(iterable):
        return reduce(operator.mul, iterable)
    
    @staticmethod
    def __div(iterable):
        return reduce(operator.truediv, iterable)
