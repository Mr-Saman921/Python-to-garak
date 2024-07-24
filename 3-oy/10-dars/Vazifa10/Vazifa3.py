
class Home:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __setattr__(self, key, value):
        if key in ('name', 'address') and isinstance(value, str):
            super().__setattr__(key, value)
        else:
            super().__setattr__(key, value)

    def __getattr__(self, item):
        return f"'{item}' atributi mavjud emas"

    def __getattribute__(self, item):
        try:
            return super().__getattribute__(item)
        except AttributeError:
            return self.__getattr__(item)

# home1 = Home("My Home", "123 Street Name")
#
# print(home1.name)
# print(home1.address)
#
# print(home1.city)
#
# home1.name = "New Home Name"
# home1.address = "456 Another Street"
#
# print(home1.name)
# print(home1.address)
