# Multiple Inheritance

# class Rectangle(object):
#     NUmber = 0
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     @classmethod
#     def area(cls, length, width):
#         return length * width
#
#     @staticmethod
#     def perimeter(length, width):
#         return 2 * (length + width)
#
# r = Rectangle.area(15, 25)
# print(r)
#
# r = Rectangle.perimeter(15, 25)
# print(r)

# from Validator7 import UserValidator
# from Db7 import Db
# class User(UserValidator, Db):
#
#     def __init__(self, username: str, password: str, name: str, surname: str):
#         super(). __init__(username, password, name, surname)
#         self.username = username
#         self.password = password
#         self.name = name
#         self.surname = surname
#
# user = User("John_Ali", "1234567", "Alijon", "Valijonov")
# print(user)
# user.save()
# user = Db.get_user(username="John_Ali", password="1234567")
# print(user)
# class Info:
#
#     def __init__(self, username: str, password: str, name: str, surname: str):
#         self.username = username
#         self.password = password
#         self.name = name
#         self.surname = surname
#
#     def __str__(self):
#         return f"Username: {self.username}\nPassword: {len(self.password) * "*"}\nName: {self.name}\nSurname: {self.surname}"
#
# i = Info("Ali", "12345", "Ali", "Valiyev")
# print(i)
