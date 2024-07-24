class Home:

    def __init__(self, number, price, adress):
        self.number = number
        self.price = price
        self.adress = adress

    def __getattr__(self, name: str):
        return f"No such attribute: '{name}'"

    def __delattr__(self, name: str):
        if name in self.__dict__:
            del self.__dict__[name]
        else:
            raise AttributeError(f"No such attribute: '{name}'")

    @staticmethod
    def calculate_tax(price, tax_rate):
        return price * tax_rate

    @classmethod
    def create_from_string(cls, home_string):
        number, price, address = home_string.split(',')
        return cls(int(number), float(price), address)

home = Home(1, 500000000, "Rohat ko'chasi")
home.number = 100
home.price = 550000000
home.adress = "Binokorlar ko'ckasi"
del home.price
print(home.number)
print(home.price)
print(home.adress)

tax = Home.calculate_tax(250000, 0.05)
print(f"Tax: {tax}")

home2 = Home.create_from_string("102,500000000,Rohat")
print(home2.number)
print(home2.price)
print(home2.address)
