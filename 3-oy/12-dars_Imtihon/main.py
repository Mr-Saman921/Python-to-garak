from module1 import calculator
from module2 import calculator1

print(calculator(25, 15))
print(calculator1(25, 15))

class Product:
    def __init__(self, title, price, category,  rating):
        self.title = title
        self.price = price
        self.category = category
        self.rating = rating

    @property
    def price(self):
        return self.__dict__['price']

    @price.setter
    def price(self, value):
        if isinstance(value, int) and value > 0:
            self.__dict__['price'] = value
        else:
            raise ValueError('Price must be an integer')

    @price.deleter
    def price(self):
        raise ValueError("You can't delete the price")
        # del self.__dict__['price']

    def add_comment(self, comment: str):
        try:
            f = open(f"{self.title}_comments", "r")
        except:
            f = open(f"{self.title}_comments", "a")
            f.write(comment)
            f.close()
        else:
            f = f = open(f"{self.title}_comments", "a")
            f.write(comment)
        finally:
            f.close()

p = Product('title', 15000, 'category', 99.9)

p.price = 20000
print(p.price)

# del p.price
# print(p.price)

p.add_comment("My first comment")
