# class Men:
#     def __init__(self, name, surname, age, phone, email):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.phone = phone
#         self.email = email
#     def men_info(self):
#         print(f"Name: {self.name}\nSurname: {self.surname}\nAge: {self.age}\nPhone: {self.phone}\nEmail: {self.email}")
#
# men=Men("Samandar","Siddiqov",14, 911213375, "siddikovs477@gmail.com")
# men.men_info()

# from typing import Any

# class Majmua:
#     def __init__(self):
#         self.ombor = []   # Public
#         self._ombor = []  # Protect
#         self.__ombor = []  # Private
#
#     def biriktirish(self, other: Any):
#         self.__ombor.append(other)
#
#     def chopish(self):
#         if len(self.__ombor) > 0:
#             self.__ombor.remove("Hello world")
#         else:
#             self.__ombor="Ma'lumot yo'q"
#
#     def tozalash(self):
#         self.__ombor.clear()
#
#     def almashtirish(self,_index: int, _value: Any):
#         if isinstance(_index, int) and len(self.__ombor) > _index:
#             self.__ombor[_index] = _value
#         else:
#             pass
#
#     def __str__(self):
#         return str(self.__ombor)
#
# m=Majmua()
# m.biriktirish("Hello world")
# m.biriktirish(121)
# m.almashtirish(1,125)
# m.ombor.append(15)
# m.tozalash()
# m.chopish()
# print(m)

# class Kalitlimajmua:
#     def __init__(self):
#         self.__ombor={}
#
#     def biriktirish(self, other: Any, other1: Any):
#         self.__ombor[other]=other1
#
#     def chopish(self, other: Any):
#         if other in self.__ombor:
#             self.__ombor.pop("name")
#         else:
#             self.__ombor="Ma'lumotlar yo'q"
#
#
#     def tozalash(self):
#         self.__ombor={}
#
#     def __str__(self):
#         return str(self.__ombor)
#
#
# d=Kalitlimajmua()
# d.biriktirish("Name","Samandar")
# d.chopish()
# print(d)