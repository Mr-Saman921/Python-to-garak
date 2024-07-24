class Cat:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        raise AttributeError("age atributini o'zgartirish taqiqlangan")

cat = Cat(5)

print(cat.age)

try:
    cat.age = 6
except AttributeError as e:
    print(e)
