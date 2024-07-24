class Person:
    def __init__(self, first_name, last_name, age, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
    def person_info(self):
        print(f"Name: {self.first_name}\nSurname: {self.last_name}\nAge: {self.age}\nPhone Number: {self.phone_number}")
person=Person(first_name=input("Enter your first name: "), last_name=input("Enter your last name: "),age=int(input("Enter your age: ")),phone_number=input("Enter your phone number: "))
person.person_info()