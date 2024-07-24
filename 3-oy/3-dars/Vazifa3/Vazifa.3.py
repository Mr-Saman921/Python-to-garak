class Room:
    def __init__(self, name, price, color, size):
        self.name=name
        self.price=price
        self.color=color
        self.size=size
    @property
    def size(self):
        return self.__dict__['size']
    @size.setter
    def size(self, value):
        if type(value)==int:
            self.__dict__['size']=value
        else:
            return("Error")
    @size.deleter
    def size(self):
        self.__dict__['size']=None
        return "Size deleted"
room=Room("web", 50000, "black", 60)
room.size=100
del room.size
print(room.size)