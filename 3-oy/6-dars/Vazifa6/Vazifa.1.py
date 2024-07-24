class Student:

    def __init__(self, name, surname, phone, fakultet, rating):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.fakultet = fakultet
        self.rating = rating

class Person(Student):

    def get_info(self):
        print(f"Name: {self.name}\nSurname: {self.surname}\nPhone: {self.phone}\nFakultet: {self.fakultet}\nRating: {self.rating}")

p=Person(name="Ali", surname="Valiyev", phone=919797979, fakultet="Programming", rating=99)
p.get_info()
