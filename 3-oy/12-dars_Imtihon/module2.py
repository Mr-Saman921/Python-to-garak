def calculator1(a, b):
    x = a - b
    return x

class Category:
    def __init__(self, title, rating, status, reg_date):
        self.title = title
        self.rating = rating
        self.status = status
        self.reg_date = reg_date


    def __setattr__(self, name, value):
        if name == "title" and isinstance(value, str) and len(value) > 5:
            self.__dict__[name] = value
        elif name == "status" and isinstance(value, bool):
            self.__dict__[name] = value
        elif name == "rating" and isinstance(value, float) and value >= 0.0 and  value <= 100.0:
            self.__dict__[name] = value
        else:
            self.__dict__[name] = value

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        return "Attribute not found"

c = Category(title = "HelloWorld", rating = 99.8, status = False, reg_date = 2010)

c.title = "Python"
c.status = True
c.rating = 99.9

print(c.title)
print(c.status)
print(c.rating)

print(c.reg_date)
