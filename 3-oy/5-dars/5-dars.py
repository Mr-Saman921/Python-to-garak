# special methods
# dunder methods  double underscore methods

from typing import Any
# class MyClass:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f"MyClass object, name: {self.name}"
#
#     def __setattr__(self, __name: str, __value: Any):
#         if __name == "age" and isinstance(__value, int):
#             self.__dict__[__name] = __value
#         else:
#             self.__dict__[__name] = __value
#
#     def __getattribute__(self, __name: str):
#         return object.__getattribute__(self, __name)
#
#     def __getattr__(self, __name: str):
#         return "Bunday atribut yo'q"
#
#     def __len__(self):
#         return 0
#
# s = MyClass(name="MyClass")
# # s.age = 15
# s.color = "#fff"
# # s.name = "My class 2"
# print(s.color)
# print(s.colorname)

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setattr__(self, name: Any, value: Any):
        if name == "age" and isinstance(value, int) and 0<value and value<120:
            self.__dict__[name] = value
        elif name == "name" and isinstance(value, str) and len(value)>2:
            self.__dict__[name] = value
        else:
            raise ValueError("Invalid attribute")
        self.__dict__[name] = value

    def __delattr__(self, name: str) -> None:
        return None
        # del self.__dict__[name]

u=User(name="Sardor", age=40)
u.name = "Samandar"
u.age = 14
# del u.name
print(u.name)
print(u.age)
