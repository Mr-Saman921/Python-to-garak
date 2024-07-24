from typing import Any

class Cat:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __setattr__(self, name: str, name1: Any):
        if name == "name" and isinstance(name1, str):
            self.__dict__[name] = name1
        elif name == "age" and isinstance(name1, int):
            self.__dict__[name] = name1
        elif name == "color" and isinstance(name1, str):
            self.__dict__[name] = name1
        else:
            raise AttributeError(f"Cannot set attribute '{name}'")

    def __getattribute__(self, name: str):
        return object.__getattribute__(self, name)

    def __getattr__(self, name: str):
        return f"No such attribute: '{name}'"

    def __delattr__(self, name: str):
        if name in self.__dict__:
            del self.__dict__[name]
        else:
            raise AttributeError(f"No such attribute: '{name}'")

cat = Cat("Simba", 3, "black")
cat.name = "Mufassa"
cat.age = 5
cat.color = "grey"
del cat.age
print(cat.name)
print(cat.age)
print(cat.color)
