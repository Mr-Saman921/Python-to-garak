from typing import Any

class Dog:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __setattr__(self, _name: str, value: Any):
        if _name == "name" and isinstance(value, str) and len(value)>2:
            self.__dict__[_name] = value
        self.__dict__[_name] = value

dog=Dog(name = "Million", age = 5, color = "black")
dog.name = "Maygo"
print(dog.name)
