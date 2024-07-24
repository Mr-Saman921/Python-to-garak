from Vazifa_1 import String

from Vazifa_2 import Int

from Vazifa_3 import Mylist

from Vazifa_4 import Boolean

from Vazifa_5 import Float

class User:
    username = String()
    name = String()
    surname = String()
    age = Int()
    groups = Mylist()
    status = Boolean()
    rating = Float()

    def __init__(self, username, name, surname, age, groups, rating):
        self.username = username
        self.name = name
        self.surname = surname
        self.age = age
        self.groups = groups
        self.rating = rating

obj = User("John", "Ali", "Valiyev", 14, ["fn_24", "fn_23", "fn_22"], 99.9)
print(obj.username)
print(obj.name)
print(obj.surname)
print(obj.age)
print(obj.groups)
print(obj.rating)
