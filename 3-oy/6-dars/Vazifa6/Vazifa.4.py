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

class Converter(Calculate):

    def km_to_metr(self, km: int):
        self.__calculate = km * 1000

    def metr_to_sm(self, metr: int):
        self.__calculate = metr * 100

    def sm_to_mm(self, sm: int):
        self.__calculate = sm * 10

    def __str__(self):
        return str(self.__calculate)

c=Converter()

c.km_to_metr(1)
print(c)

c.metr_to_sm(1)
print(c)

c.sm_to_mm(1)
print(c)