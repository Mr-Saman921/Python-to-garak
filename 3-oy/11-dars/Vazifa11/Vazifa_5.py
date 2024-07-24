

class Float:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        print(f"Qiymat o'zgartirildi: {value}")
        if isinstance(value, float):
            instance.__dict__[self.name] = value
        else:
            raise ValueError("Value must be a float")

class Myclass:
    rank = Float()

    def __init__(self, rank):
        self.rank = rank

# obj = Myclass(99.9)
# print(obj.rank)
