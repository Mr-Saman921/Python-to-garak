# Vorislik

# class Animal:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sleep(self):
#         print(f"{self.name} is sleeping")
#
# class Dog(Animal):
#     pass
#
# class Cat(Animal):
#     pass
#
# d = Dog(name = "Jack", age = 1)
# d.sleep()
#
# c = Cat(name = "Simba", age = 2)
# c.sleep()

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def human_info(self):
#         print(f"{self.name} is {self.age} years old")
#
# class Student(Human):
#     def human_info(self):
#         print(f"{self.name} is {self.age} years old")
#         print(f"{self.name} is student")
#
# class People(Human):
#     def human_info(self):
#         print(f"{self.name} is {self.age} years old")
#         print(f"{self.name} is people")
#
# s = Student(name="Ali", age=20)
# s.human_info()
#
# p = People(name="Vali", age=15)
# p.human_info()

from Hero6 import Hero
from War6 import War
import random
import time
class Human(Hero, War):
    pass

class Alian(Hero, War):
    pass

human = Human(name = "John", health = 150, attack_power = 2)


alian = Human(name = "Tumandu", health = 150, attack_power = 3)

players = [human, alian]

while human.health > 0 and alian.health > 0:
    players2 = players.copy()
    attacker = random.choice(players2)
    players2.remove(attacker)
    defender = players2[0]
    attacker.attack(defender)
    time.sleep(1)
