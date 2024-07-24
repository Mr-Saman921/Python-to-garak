

class Boolean:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        print(f"Qiymat o'zgartirildi: {value}")
        if isinstance(value, bool):
            instance.__dict__[self.name] = value
        else:
            raise ValueError("Value must be a boolean")

class Myclass:
    boolean = Boolean()

    def __init__(self, boolean):
        self.boolean = boolean

# obj = Myclass(True)
# print(obj.boolean)
