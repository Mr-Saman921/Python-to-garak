class Calculate:
    def __init__(self):
        self.__calculate = 0

    def plus(self, number: int, number1: int):
        if isinstance(number, int) and isinstance(number1, int):
            self.__calculate = number+number1
        else:
            pass

    def minus(self, number: int, number1: int):
        if isinstance(number, int) and isinstance(number1, int):
            self.__calculate = abs(number-number1)
        else:
            pass

    def divide(self, number: int, number1: int):
        if isinstance(number, int) and isinstance(number1, int):
            if number > number1:
                self.__calculate = number/number1
            else:
                self.__calculate = number1/number
        else:
            pass

    def multiply(self, number: int, number1: int):
        if isinstance(number, int) and isinstance(number1, int):
            self.__calculate = number*number1
        else:
            pass

    def __str__(self):
        return str(self.__calculate)

c=Calculate()
c.plus(15,5)
print(c)
c.minus(15,5)
print(c)
c.divide(15,5)
print(c)
c.multiply(15,5)
print(c)