

class Mylist:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        print(f"Qiymat o'zgartirildi: {value}")
        if isinstance(value, list):
            instance.__dict__[self.name] = value
        else:
            raise ValueError("Value must be a list")

class Myclass:
    list1 = Mylist()

    def __init__(self, list1):
        self.list1 = list1

# obj = Myclass(["Samandar", "Siddiqov", "14"])
# print(obj.list1)
