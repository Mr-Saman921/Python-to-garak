from random import randint
class RandomSimvols:
    def __init__(self, number):
        self.number=number
    def rand(self):
        print(self.number)
randomsimvols=RandomSimvols(number=randint(1,100))
randomsimvols.rand()