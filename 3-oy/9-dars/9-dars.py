# Abstract class



# class Human:
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __getattribute__(self, __name):
#         return object.__getattribute__(self, __name)
#
#     def __getattr__(self, __name, __value):
#         return "False"
#
#     def __str__(self):
#         return f"Name: {self.name}"
#
# h=Human("John", "Doe")
# h.name = "Ali"
# print(h)

# from abc import ABC, abstractmethod
#
# class Electron(ABC):
#
#     @abstractmethod
#     def on(self):
#         pass
#
#     @abstractmethod
#     def off(self):
#         pass
#
#
# class Iron(Electron):
#     def __init__(self, brand):
#         self.brand = brand
#         self.__state = 'off'
#
#     @staticmethod
#     def check_power():
#         return True
#
#     def on(self):
#         if self.check_power():
#             if self.__state == 'off':
#                 self.__state = 'on'
#                 print('Iron is on')
#             else:
#                 print('Iron is alredy on')
#         else:
#             print('Power is null')
#
#     def off(self):
#         if self.__state == 'on':
#             self.__state = 'off'
#             print('Iron is off')
#         else:
#             print('Iron is alredy off')
#
# iron = Iron('Artel')
#
# iron.on()
# iron.off()
# iron.off()

# class Animal(ABC):
#
#     @abstractmethod
#     def sleap(self):
#         pass
#
#     @abstractmethod
#     def jump(self):
#         pass
#
# class Dog(Animal):
#
#     def __init__(self, name):
#         self.name = name
#
#     def sleap(self):
#         print(f"Dog's name is {self.name}")
#         print(f"{self.name} is slepping.")
#
#     def jump(self):
#         print(f"Dog's name is {self.name}")
#         print(f"{self.name} is jumping.")
#
# class Cat(Animal):
#
#     def __init__(self, name):
#         self.name = name
#
#     def sleap(self):
#         print(f"Cat's name is {self.name}")
#         print(f"{self.name} is slepping.")
#
#     def jump(self):
#         print(f"Cat's name is {self.name}")
#         print(f"{self.name} is jumping.")
#
# d = Dog("David")
# d.sleap()
# d.jump()
#
# c = Cat("Simba")
# c.sleap()
# c.jump()


# from multipledispatch import dispatch
# class Calculator(object):
#     def __init__(self):
#         self.number = 1
#
#     @dispatch(int)
#     def add(self, num):
#         self.number += num
#         return self.number
#
#     @dispatch(int)
#     def add(self, num, num2):
#         self.number = self.number + num + num2
#         return self.number
#
# c=Calculator()
# print(c.add(2, 4))
