# """
# Polimarfizm, inkapsulatsiya
# OOP Vorislik, abstractsiya, polimarfizm, inkapsulatsiya
#
# """
#
# # Polimarfizm
# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#
#     @abstractmethod
#     def perm(self):
#         pass
#
# class Rect(Shape):
#     def __init__(self, width, length):
#         self.__width = width
#         self.__length = length
#
#     def perm(self):
#         return 2 * (self.__length + self.__width)
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.__radius = radius
#
#     def perm(self):
#         return 2 * 3.14 * self.__radius
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def perm(self):
#         return self.a + self.b + self.c
#
# r = Rect(5, 10)
# r1 = Rect(6, 12)
#
# c = Circle(5)
# c1 = Circle(7)
#
# t = Triangle(3, 5, 7)
# t1 = Triangle(2, 4, 6)
#
# objects = [r, r1, c, c1, t, t1]
#
# for obj in objects:
#     print(obj.perm())
#
#
#
#
# from abc import ABC, abstractmethod
# class Car(ABC):
#     @abstractmethod
#     def start(self):
#         pass
#
# class Bugatti(Car):
#     def __init__(self, name, color, brand):
#         self.name = name
#         self.color = color
#         self.brand = brand
#
#     def start(self):
#         return f"{self.name} start"
#
#
# class Mybach(Car):
#     def __init__(self, name, color, brand):
#         self.name = name
#         self.color = color
#         self.brand = brand
#
#     def start(self):
#         return f"{self.name} start"
#
# class Supra(Car):
#     def __init__(self, name, color, brand):
#         self.name = name
#         self.color = color
#         self.brand = brand
#
#     def start(self):
#         return f"{self.name} start"
#
# b = Bugatti("Bugatti", "black", "bugatti")
#
# m = Mybach("Mybach", "black", "mybach")
#
# s = Supra("Supra", "red", "tayota")
#
# o = [b, m, s]
# for obj in o:
#     print(obj.start())
#
#
#
# # inkapsulatsiya
# class User:
#     def __init__(self, name, surname, age):
#         self.__name = name  # private
#         self.__surname = surname
#         self.__age = age
#
#     def set_name(self, __name):
#         if isinstance(__name, str):
#             self.__name = __name
#         else:
#             raise ValueError("Name must be a string")
#
# u = User("Samandar", "Siddiqov", 14)
#
# u.set_name("Ali")
# print(u.name)
#
# u._User__name = "Ali"
# print(u.__dict__)
