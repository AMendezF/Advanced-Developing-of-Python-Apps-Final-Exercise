import typing
from functools import reduce
import operator


class VecCalc():

    def __init__(self):
        self.prec = 2 # decimal result precision

    def addition(self, vector1: typing.List[float], vector2: typing.List[float]) -> typing.List[float]:
        vector_list = [vector1, vector2]
        assert(self.addition_safe_check(*vector_list) == True)
        
        return self.addition_calc(vector_list)

    def subtraction(self, vector1: typing.List[float], vector2: typing.List[float]) -> typing.List[float]:
        vector_list = [vector1, vector2]
        assert(self.subtraction_safe_check(*vector_list) == True)
        
        return self.subtraction_calc(vector_list)

    def multiplication(self, vector1: typing.List[float], vector2: typing.List[float]) -> typing.List[float]:
        vector_list = [vector1, vector2]
        assert(self.multiplication_safe_check(*vector_list) == True)
        
        return self.multiplication_calc(vector_list)

    def division(self, vector1: typing.List[float], vector2: typing.List[float]) -> typing.List[float]:
        vector_list = [vector1, vector2]
        assert(self.division_safe_check(*vector_list) == True)
        
        return self.division_calc(vector_list)

    ### Safe Check Functions:
    #########################

    def addition_safe_check(self, vector1: list, vector2: list) -> bool:
        safe = self.basic_safe_check(vector1, vector2)
        return safe

    def subtraction_safe_check(self, vector1: list, vector2: list) -> bool:
        safe = self.basic_safe_check(vector1, vector2)
        return safe

    def multiplication_safe_check(self, vector1: list, vector2: list) -> bool:
        safe = self.basic_safe_check(vector1, vector2)
        return safe

    def division_safe_check(self, vector1: list, vector2: list) -> bool:
        safe = (self.basic_safe_check(vector1, vector2) and
                self.vector_zero_safe_check(vector2)
            )
        return safe

    def basic_safe_check(self, vector1: list, vector2: list) -> bool:
        safe = (self.vector_not_empty_safe_check(vector1) and
                self.vector_not_empty_safe_check(vector2) and
                self.vector_type_safe_check(vector1) and
                self.vector_type_safe_check(vector2) and
                self.vector_length_safe_check(vector1, vector2)
            )
        return safe

    @staticmethod
    def vector_not_empty_safe_check(vector: list) -> bool:
        return True if len(vector)>0 else False

    @staticmethod
    def vector_type_safe_check(vector: list) -> bool:
        return True if all(isinstance(x, float) for x in vector) else False

    @staticmethod
    def vector_length_safe_check(vector1: list, vector2: list) -> bool:
        return True if len(vector1) == len(vector2) else False

    @staticmethod
    def vector_zero_safe_check(vector: typing.List[float]) -> bool:
        return True if 0.0 not in vector else False

    ### Vector Calc Functions:
    ##########################

    def addition_calc(self, vector_list: typing.List[typing.List[float]]) -> typing.List[float]:
        return [round(self.add(x), self.prec) for x in zip(*vector_list)]

    def subtraction_calc(self, vector_list: typing.List[typing.List[float]]) -> typing.List[float]:
        return [round(self.sub(x), self.prec) for x in zip(*vector_list)]

    def multiplication_calc(self, vector_list: typing.List[typing.List[float]]) -> typing.List[float]:
        return [round(self.mul(x), self.prec) for x in zip(*vector_list)]

    def division_calc(self, vector_list: typing.List[typing.List[float]]) -> typing.List[float]:
        return [round(self.div(x), self.prec) for x in zip(*vector_list)]
    
    @staticmethod
    def add(iterable):
        return reduce(operator.add, iterable)

    @staticmethod
    def sub(iterable):
        return reduce(operator.sub, iterable)

    @staticmethod
    def mul(iterable):
        return reduce(operator.mul, iterable)
    
    @staticmethod
    def div(iterable):
        return reduce(operator.truediv, iterable)
