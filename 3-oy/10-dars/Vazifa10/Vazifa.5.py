class Car:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def car(cls, name, age):
        return f"{name} is {age} years old"

    @staticmethod
    def car1(name):
        return f"{name} is very popular car"

c = Car("Lacetti", "2")

c1 = Car.car("Bugatti", "3")
print(c1)

c2 = Car.car1("Supra")
print(c2)
