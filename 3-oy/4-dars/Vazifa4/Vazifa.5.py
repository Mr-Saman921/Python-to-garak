class Convertor:
    def __init__(self):
        self.__convertor = 0

    def usd_to_uzs(self, usd: int):
        self.__convertor = usd * 12500

    def uzs_to_usd(self, uzs: int):
        self.__convertor = uzs / 12500

    def __str__(self):
        return str(self.__convertor)

convertor = Convertor()
convertor.usd_to_uzs(10)
print(convertor)
convertor.uzs_to_usd(125000)
print(convertor)