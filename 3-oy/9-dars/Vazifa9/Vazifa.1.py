from abc import ABC, abstractmethod

class Electron(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass
    
class Velo(Electron):

    def __init__(self, age):
        self.age = age
        self.__state = 'turn_off'

    def turn_on(self):
        if self.__state == 'turn_off':
            self.__state = 'turn_on'
            print('Velo turned on')
        else:
            print('Velo alredy turned on')

    def turn_off(self):
        if self.__state == 'turn_on':
            self.__state = 'turn_off'
            print('Velo turned off')
        else:
            print('Velo alredy turned off')

class Car(Electron):

    def __init__(self, age):
        self.age = age
        self.__state = 'turn_off'

    def turn_on(self):
        if self.__state == 'turn_off':
            self.__state = 'turn_on'
            print('Car turned on')
        else:
            print('Car alredy turned on')

    def turn_off(self):
        if self.__state == 'turn_on':
            self.__state = 'turn_off'
            print('Car turned off')
        else:
            print('Car alredy turned off')

v = Velo(2)

v.turn_on()
v.turn_on()

v.turn_off()
v.turn_off()

c = Car(3)

c.turn_on()
c.turn_on()

c.turn_off()
c.turn_off()