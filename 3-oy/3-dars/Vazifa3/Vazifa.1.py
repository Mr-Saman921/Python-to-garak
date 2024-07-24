class Car:
    def __init__(self, color, price, owner) ->None:
        self.color=color
        self.price=price
        self.owner=owner


    @property
    def color(self):
        return self.__dict__['color']
    @color.setter
    def color(self, value):
        if isinstance(value, str)==True:
            self.__dict__['color']=value
        else:
            return ("Error")


    @property
    def price(self):
        return self.__dict__['price']

    @price.setter
    def price(self, value):
        if isinstance(value, int) == True:
            self.__dict__['price']=value
        else:
            return ("Error")


    @property
    def owner(self):
        return self.__dict__['owner']

    @owner.setter
    def owner(self, value):
        if isinstance(value, str) == True:
            self.__dict__['owner']=value
        else:
            return ("Error")
car=Car("Black", 15000, "Ali")
car.color="White"
car.price=20000
car.owner="Sardor"
print(car.color)
print(car.price)
print(car.owner)