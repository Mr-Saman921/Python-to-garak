class Soda:

    def __init__(self):
        self.__thing = ""

    def show_my_drink(self, thing1: str):
        if thing1.lower() == "mevasiz":
            self.__thing = "Oddiy gazli suv"

        else:
            self.__thing = f"{thing1}li suv"

    def __str__(self):
        return str(self.__thing)

s = Soda()

s.show_my_drink("Mevasiz")
print(s)
