class Convertor:
    def __init__(self):
        self.__convertor = 0
    def sm_to_metr(self, sm: int):
        self.__convertor = sm / 100

    def km_to_metr(self, km: int):
        self.__convertor = km * 1000

    def __str__(self):
        return str(self.__convertor)

convertor = Convertor()
convertor.sm_to_metr(150)
print(convertor)
convertor.km_to_metr(2)
print(convertor)
