class Calculate:

    def __init__(self):
        self.__calculate = 0

    def summa(self, number: int, number2: int):
        self.__calculate = number + number2

    def difference(self, number: int, number2: int):
        self.__calculate = abs(number - number2)

    def multiple(self, number: int, number2: int):
        self.__calculate = number * number2

    def division(self, number: int, number2: int):
        if number > number2:
            self.__calculate = number / number2
        else:
            self.__calculate = number2 / number

    def __str__(self):
        return str(self.__calculate)
    
c = Calculate()

c.summa(15, 5)
print(c)

c.difference(15, 5)
print(c)

c.multiple(15, 5)
print(c)

c.division(15, 5)
print(c)
