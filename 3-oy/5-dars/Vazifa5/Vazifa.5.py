class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def make_sound(self):
        print(f"{self.name} is making a sound.")

class Animals(Animal):
    def make_sound(self):
        print(f"{self.name} says: Meow\n{self.name} says: Woof\n{self.name} says: Roar")

cat = Animals("Whiskers", 3)
dog = Animals("Buddy", 5)
lion = Animals("Simba", 7)

cat.eat()
cat.sleep()
cat.make_sound()

dog.eat()
dog.sleep()
dog.make_sound()

lion.eat()
lion.sleep()
lion.make_sound()
